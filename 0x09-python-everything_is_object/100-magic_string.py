#!/usr/bin/python3g
def magic_string():
    s = "BestSchool"
    return '\n'.join([s + (', ' + s) * i for i in range(10)]) + '$\n'
