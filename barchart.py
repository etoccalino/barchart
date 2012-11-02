#! /usr/bin/env python

# Copyright 2012 Elvio Toccalino
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Produce a bar chart of file/directory sizes.

Given a stream of lines, this program assumes each line corresponds to a
directory, and is formatted as "directory-size directory-name" (as produced by
the *du* UNIX command), it will adorn the lines with a row of chars. All these
rows can then be interpreted as a 90 degree rotated bar chart, each row
corresponding to the size of that particular file/directory relative to the
total.

The total size (size of the parent directory) is assume to be listed as the
last line in the input stream, just as the *du* UNIX command does.
"""

# Python2.6 and ahead can override the 'print' built-in with a function.
from __future__ import print_function

import re
import io
import sys


# This is used as part of of a regexp, so escape as necessary.
DECIMAL_DOT = r'\.'
CHAR = "#"
WIDTH = 10

SIZEMODS = {
    'k': 1024, 'm': 1024*1024, 'g': 1024*1024*1024, 't': 1024*1024*1024*1024,
    'K': 1024, 'M': 1024*1024, 'G': 1024*1024*1024, 'T': 1024*1024*1024*1024
}


class ImproperLineError(Exception):
    """
    Used to signal that a line being processed did not conform to the schema.
    """
    pass


###############################################################################


class SizeProcessor:
    """
    Produce the barchart-adorned output.

    Since the chart shows relative sizes, all input lines must be processed
    before output. When the last line comes, it is assumed to have the total
    size, which is used to produce the relative values.

    Each line of output is equivalent to its corresponding line of input,
    except it is preceded by WIDTH+1 caracters (blanks and the CHAR), which can
    be read as a 90 degree rotated bar chart of the numbers in the inputed
    lines.
    """

    def __init__(self, decimal_dot=None, char=None, width=None):
        """Initialize the configurable output related variables.

        Keyword parameters:
        decimal_dot -- configure fractional character (default '.').
        char -- character to build the bars with (default %(char)s).
        width -- maximum number of characters for the bar (default %(width)s).
        """

        # Allow for configuration override.
        self.DECIMAL_DOT = decimal_dot or DECIMAL_DOT
        self.CHAR = char or CHAR
        self.WIDTH = width or WIDTH
        # Init inner values.
        self.queue = []
        self.line_count = 0

        # According to the docs, this is not necessary. The re module catches
        # the most recent patterns passed to re.match(), re.search() and
        # re.compile().  It'll be interesting to test.
        self.size_re = re.compile(r'^\s*(?P<integer_part>\d+)'
                       + self.DECIMAL_DOT + r'?'
                       + r'(?P<decimal_part>\d+)?'
                       + r'(?P<mod>[' + ''.join(SIZEMODS.keys()) + r'])?')


    def _size_for_line(self, line, line_number=None):
        """Given a line, which should start with a size, return its absolute
        size value.

        If a line number is passed it will be used in case an error report is
        issued.

        Positional parameters:
        line -- the string to process.

        Keyword paramters:
        line_number -- the line number of the line (default auto-incremental).
        """
        match = self.size_re.match(line)
        if match is None:
            # Report the error.
            errorstring = 'The line does not match the "space-size-mod" schema'
            if line_number:
                errorstring = ('Line number %i does not match the'
                               ' "space-size-mod" schema' % line_number)
                raise ImproperLineError(errorstring)

        # Integer part of the size.
        size = int(match.group('integer_part'))

        # If there is a decimal part, add it.
        size_decimal_part = match.group('decimal_part')
        if size_decimal_part:
            size += float(size_decimal_part)

        # The size may be expressed with a mod-factor.
        mod = match.group('mod')
        if mod:
            return size * SIZEMODS[mod]
        return size

    def _format_line(self, size, line):
        """Build a line appropriate for output, using local configuration.

        Positional parameters:
        size -- the size read from this line.
        line -- the line contents, including the size part.
        """
        relative = size / self.last_size
        chars = int(round(relative * self.WIDTH))
        bar = u' ' * (self.WIDTH - chars) + self.CHAR * chars
        return bar + u' ' + line

    def _format_last_line(self, size, line):
        """Build the last line for the output.

        Positional parameters:
        size -- the size read from this line.
        line -- the line contents, including the size part.
        """
        bar = u'=' * self.WIDTH
        return bar + u' ' + line

    def feed(self, line):
        """Feed a line to the processor.

        Assumes the lines are fed in order, and counts them.


        Positional parameters:
        line -- the entire line to process.
        """
        self.line_count += 1
        line_size = self._size_for_line(line, line_number=self.line_count)
        self.queue.append((line_size, line))

    def getvalue(self):
        """Produce the output, with their bar chart."""
        buffered = io.StringIO()

        # Get the total size and generate the adorned line.
        self.last_size, last_line = self.queue.pop()
        for size, line in self.queue:
            buffered.write(self._format_line(size, line))

        # Add back the last line.
        buffered.write(self._format_last_line(self.last_size, last_line))

        output = buffered.getvalue()
        buffered.close()
        return output


###############################################################################


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--decimal-char", default=DECIMAL_DOT,  help="Character "
                    "which breaks franctions (default is '.').")
parser.add_argument("-c", "--char", help="Which character to use for the "
                    "bars (default is '%s')." % CHAR)
parser.add_argument("-w", "--width", type=int, default=WIDTH, help="Width of "
                    "bars in the chart (default is %i)." % WIDTH)


###############################################################################


if __name__ == "__main__":
    args = parser.parse_args()

    h = SizeProcessor(decimal_dot=args.decimal_char,
                       char=args.char, width=args.width)
    for line in sys.stdin:
        h.feed(line)
    print(h.getvalue())
