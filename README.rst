==========
 barchart
==========

A UNIX-like program to pipe ``du`` output through and gain a bar chart of file sizes.


Description
===========

What's the most used program in the terminal? ``ls``, of course! Yes, it is! *(I don't care if that's not true for you, this is not a survey)*. But ``ls``, good as the antediluvians made it, does not traverse the file-system. It merely gives information it obtains one level deep. Who goes deeper? ``du`` goes as deep as it can, or as deep as you tell it to go... shiny.

I developed ``barchart`` with a very specific ``du`` use case in mind: inspecting a directory one level deep. This is a very recurring pattern in my day to day experience. ``barchart`` leaves its input *almost* as-is; it adorns it with a bar chart of the sizes reported by ``du``, or whatever program laid up in the pipe. The terminal is a very limited canvas (and due to my scarce ascii-art skills, doubly so), but the bar chart is conveniently located on the side of the output, rotated 90-degrees, so that each bar is aligned with the ``du`` reported size to which it corresponds. The results are satisfactory.


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


Compatibility
=============

The program is python2 compatible (2.6 and ahead tested). I have made, however, a python3 version, aided by the 2to3 tool. You should use only one version of the program.  Since you can choose whatever python you have (as long as its python2.6 or ahead) I make it an executable by means of a shebang comment.

The most visible version of the program is for python2, because I found it to be ubiquitous among modern UNIX-like systems. However, I recommend that if you already have python3 installed in your system you use the py3k/barchart.py program instead.


Options
=======

- Change the columns character.
- Change column size.



Limitations
===========

- Why one level deep? what if I break this rule?


License
=======

The ``barchart`` program file is licensed under the GNU GPL version 3.0. A copy of the license is included with the program. For details about the license, visit http://www.gnu.org/licenses/gpl.html.
