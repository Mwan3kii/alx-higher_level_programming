0. Run Python file file 0-run
   Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 

1. Run inline File: 1-run_inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 

2. Hello, print
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
File: 2-print.py

3. Print integer
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by Battery street,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings tips
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
File: 3-print_number.py

4. Print float
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
The output of the program should be:
Float:, followed by the float with only 2 digits
followed by a new line
You are not allowed to cast number to string
You have to use f-strings
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
File: 4-print_float.py

5. Print string
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

You can find the source code here
The output of the program should be:
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
You are not allowed to use any loops or conditional statement
Your program should be maximum 5 lines long
guillaume@ubuntu:~/py/0x00$ ./5-print_string.py 
ALX ALX ALX ALX
guillaume@ubuntu:~/py/0x00$ 
File: 5-print_string.py

6. Play with strings
Complete this source code to print Welcome to ALX

You can find the source code here
You are not allowed to use any loops or conditional statements.
You have to use the variables str1 and str2 in your new line of code
Your program should be exactly 5 lines long
guillaume@ubuntu:~/py/0x00$ ./6-concat.py
Welcome to ALX!
guillaume@ubuntu:~/py/0x00$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/0x00$ 
File: 6-concat.py
