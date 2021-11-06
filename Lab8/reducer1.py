#!/usr/bin/python3
import sys

for line in sys.stdin:
    line=line.strip().split(',')
    word = line[0]
    print(f'{word}')
       
