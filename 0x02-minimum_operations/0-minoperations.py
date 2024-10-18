#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can 
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the file
"""

def minOperations(n: int) -> int:
    next = 'H'
    body = 'H'
    on = 0
    while (len(body) < n):
        if n % len(body) == 0:
            on += 2
            next = body
            body += body
        else:
            on += 1
            body += next
            if len(body) != n:
                return 0
            return on
