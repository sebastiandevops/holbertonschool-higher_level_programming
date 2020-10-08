This folder includes all tasks assigned in 0x0B-python-input_output project.

0x0B. Python - Input/Output

Foundations - Higher-level programming ― Python

by Guillaume, CTO at Holberton School

weight: 1

Ongoing second chance project - started 10-07-2020, must end by 10-09-2020 (in about 15 hours) - you're done with 33% of tasks.

QA review fully automated.
In a nutshell…

    Auto QA review: 112.0/163 mandatory & 0.0/30 optional
    Altogether:  68.71%
        Mandatory: 68.71%
        Optional: 0.0%
        Calculation:  68.71% + (68.71% * 0.0%)  == 68.71%

Resources

Read or watch:

    7.2. Reading and Writing Files
    8.7. Predefined Clean-up Actions
    Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))
    JSON encoder and decoder
    Learn to Program 8 : Reading / Writing Files
    Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    Why Python programming is awesome
    How to open a file
    How to write text in a file
    How to read the full content of a file
    How to read a file line by line
    How to move the cursor in a file
    How to make sure a file is closed after using it
    What is and how to use the with statement
    What is JSON
    What is serialization
    What is deserialization
    How to convert a Python data structure to a JSON string
    How to convert a JSON string to a Python data structure

Requirements
Python Scripts

    Allowed editors: vi, vim, emacs
    All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    All your files must be executable
    The length of your files will be tested using wc

Python Test Cases

    Allowed editors: vi, vim, emacs
    All your files should end with a new line
    All your test files should be inside a folder tests
    All your test files should be text files (extension: .txt)
    All your tests should be executed by using this command: python3 -m doctest ./tests/*
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    We strongly encourage you to work together on test cases, so that you don’t miss any edge case

More Info
Shoutouts

Justin Marsh for the “Automate the Boring Stuff with Python” book rec


Tasks

0. Read file mandatory
Score: 0.00% (Checks completed: 0.00%)

Write a function that reads a text file (UTF8) and prints it to stdout:

    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module

```
guillaume@ubuntu:~/0x0B$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$ ./0-main.py
Holberton School offers a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
guillaume@ubuntu:~/0x0B$
```
No test cases needed

Repo:

    GitHub repository: holbertonschool-higher_level_programming
    Directory: 0x0B-python-input_output
    File: 0-read_file.py
