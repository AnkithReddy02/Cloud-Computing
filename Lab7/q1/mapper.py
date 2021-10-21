#!/usr/bin/python3
import sys
import string
# input comes from STDIN (standard input)
for line in sys.stdin:

    line=line.strip()
# split the line into words
    words=line.split()
    table = str.maketrans('', '', string.punctuation)
    for i in range(len(words)):
        word = words[i].translate(table)
        word = word.lower()
        words[i] = word
# increase counters
    for word in words:
        print(f'{word},1')