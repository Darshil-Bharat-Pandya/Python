# Python modules = It is a file that contains built-in functions, classes, its and variables. There are many Python modules, each with its specific work. It is a file containing Python definitions and statements. A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use.

# How to Install a Python Module ? = A module is simply a file containing Python code. Functions, groups, and variables can all be described in a module. Runnable code can also be used in a module.

# Python: Pillow(A fork of PIL) = Python Imaging Library (expansion of PIL) is the de facto image processing package for Python Language. It incorporates lightweight image processing tools that aids in editing, creating and saving images. Support for Python Imaging Library got discontinued in 2011, but a project named pillow forked the original PIL project and added Python3.x support to it. Pillow was announced as a replacement for PIL for future usage. Pillow supports a large number of image file formats including BMP, PNG, JPEG, and TIFF. The library encourages adding support for newer formats in the library by creating new file decoders. This module is not preloaded with Python. So to install it execute the following command in the command-line: pip install pillow

import qrcode as qr
img = qr.make("https://www.youtube.com/")
img.save("Youtube.png")