# ECC-ELGAMAL

The code was done as a part of the digital assignment 1 for the course **Cyber Security (CSE 4003)** taken by
Professor: **Ganesan R** at VIT University Chennai!

We did this digital assignment in a group of 2. The contributors are:

+ Hargur Partap Singh Bedi: 15BCE1257
+ Kumar Shubham: 15BCE1283

The project is made using Python 2.7. The GUI has been implemented using the PyQt framework which allows us to have cross platform GUI compatibility.

The project has been broken down into several modules in order to organize the file structure. Here is a brief list of what every file does:

+ **basicfunc.py** : The file basically contains implementations of inverse and square root functions.

+ **elgamal.py**: The file has functions for generating the points and encrypting and decrypting the plain text and ciphertext respectively.

+ **elliptic.py**: This file contains abstractions for basic functioning of the project.

+ **encdec.py**: As the name suggests the file has three main functions:
	+  ``public_key()``
	+  ``encryptiong(public_key, message)``
	+  ``decrytpion(private_key, ciphertext)``

+ **gui.py**: The file contains the code for making the window and other GUI functionalties using the Qt framework for Python!.

**Note:** *The screenshots are put in the screenshot folder.*