==========
 barchart
==========

A *UNIX-like program* to pipe ``du`` output through and gain a bar chart of file sizes.


Description
===========

What's the most used program in the terminal? ``ls``, of course! Yes, it is! (I don't care if that's not true for you, this is not a survey). But ``ls``, good as the antediluvians made it, does not traverse the file-system. It merely gives infomation it obtains one level deep. Who goes deeper? ``du`` goes as deep as it can, or as deep as you tell it to go... shiny.

I developed ``barchart`` with a very specific ``du`` usecase in mind: inspecting a directory one level deep. This is a very recurring pattern in my day to day expericience. ``barchart`` leaves its input *almost* as-is; it adorns it with a bar chart of the sizes reported by ``du``, or whatever program laied up in the pipe. The terminal is a very limited canvas (and due to my scarce ascii-art skills, double so), but the bar chart is conveniently located on the side of the output, rotated 90-degrees, so that each bar is aligned with the ``du`` reported size to which it corresponds. The results are satisfactory.


Example Usage
=============

The simplest command which can benefit from ``barchart`` ::

  du -d 1 | python barchart

The output of which reads like this::

             388	./Python
          ## 51652	./imagenesdb-env
             2852	./books-env
             3220	./emacs-for-man
             5244	./C
           # 18508	./grampg-env
          ## 39564	./Haskell
        #### 92068	./artv-env
           # 21644	./prototipo-tazas
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
        #### 90M	./artv-env
           # 22M	./prototipo-tazas
  ========== 235M	.


Options
=======

- Change the columns character.
- Change column size.



Limitations
===========

- Why one level deep? what if I break this rule?