#!/usr/bin/python3
import sys
import string
for line in sys.stdin:
    line=line.strip()
    words=line.split()
    table = str.maketrans('', '', string.punctuation)
    for i in range(len(words)):
        word = words[i].translate(table)
        word = word.lower()
        print(f'{word},1')

        