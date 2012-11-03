.. Copyright 2012 Elvio Toccalino

.. This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.

==========
 barchart
==========

A UNIX-like program to pipe ``du`` output through and gain a bar chart of file sizes.


Description
===========

What's the most used program in the terminal? ``ls``, of course! Yes, it is! *(I don't care if that's not true for you, this is not a survey)*. But ``ls``, good as the antediluvians made it, does not traverse the file-system. It merely gives information it obtains one level deep. Who goes deeper? ``du`` goes as deep as it can, or as deep as you tell it to go... shiny.

I developed ``barchart`` with a very specific ``du`` use case in mind: inspecting a directory one level deep, but still inspecting full directory sizes. This is a very recurring pattern in my day to day experience. ``barchart`` leaves its input *almost* as-is; it adorns it with a bar chart of the sizes reported by ``du``, or whatever program laid up in the pipe. The terminal is a very limited canvas (and due to my scarce ascii-art skills, doubly so), but the bar chart is conveniently located on the side of the output, rotated 90-degrees, so that each bar is aligned with the ``du`` reported size to which it corresponds. The results are satisfactory.


Example Usage
=============

The simplest command which can benefit from ``barchart`` ::

  du -d 1 | barchart

The output of which reads like this::

             388	./Python
          ## 51652	./imagenesdb-env
             2852	./books-env
             3220	./emacs-for-man
             5244	./C
           # 18508	./grampg-env
          ## 39564	./Haskell
        #### 92068	./secret-env
           # 21644	./prototipo-secret
  ========== 240056	.


But usually you don't care about the precise byte count. The helpful **-h** option turns byte numbers into more *human readable* numbers. ``barchart`` can eat that output as well. The example turns into::

  du -d 1 -h | barchart

Which will result in::

             388K	./Python
          ## 51M	./imagenesdb-env
             2.8M	./books-env
             3.2M	./emacs-for-man
             5.2M	./C
           # 19M	./grampg-env
          ## 39M	./Haskell
        #### 90M	./secret-env
           # 22M	./prototipo-secret
  ========== 235M	.

.. note::
  In this README file, the example outputs are indented for convenience. In the wild, you'd see the large "=" bar (showing the total size of the whole directory) without space to the left.


Script it!
==========

If you find the ``barchart`` program attractive, and think it might be useful, I urge you to try it by building a wrapper-script to have ``barchart`` extend ``du``, in the following fashion::

  #! /usr/bin

  du -d 1 $@ | barchart -c :

Hardcoding options to the ``barchart`` program like the ':' bars above. Assuming you call that script ``dub`` you can later just type ``dub some-dir`` and have a prettier output.


Compatibility
=============

The program is python2 compatible (2.6 and ahead tested). I have made, however, a python3 version, aided by the 2to3 tool. You should use only one version of the program.  Since you can choose whatever python you have (as long as its python2.6 or ahead) I make it an executable by means of a shebang comment.

The most visible version of the program is for python2, because I found it to be ubiquitous among modern UNIX-like systems. However, I recommend that if you already have python3 installed in your system you use the py3k/barchart.py program instead.


Options
=======

Help
    The **-h** or **--help** will show all necessary information to use the program, rendering the rest of this section redundant.

Chart width
    Using the **-w** or **--width** options you can allocate any amount of space for the bars, which translates to greater accuracy (and more indentation of original input).

Bars character
    You can select which character to use when building the bars of the chart with the **-c** or **--char** option.

Finalizing line character
    At the bottom of the chart, along the total size reported, a stright line (corresponding to 100%) is drawn using the character selected with the **-t** or **--total-char** option.


Limitations
===========

Why one level deep when calling ``du``? what if I omit the **-d 1** option? In that case the numbers reported by ``du`` correspond to sizes which are added up level by level (e. g. a directory, parent of a nested directory, sums that child directory's size in its own) and the chart is no longer correct.


License
=======

The ``barchart`` program (both its python2 and python3 versions) and this README file are licensed under the GNU GPL version 3.0. A copy of the license is included with the program. For details about the license, visit http://www.gnu.org/licenses/gpl.html.
