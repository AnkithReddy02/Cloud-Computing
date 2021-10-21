#!/usr/bin/python3
import sys
current_word=None
current_count=0
for line in sys.stdin:
    line=line.strip().split(',')
    word = line[0]
    if current_word == None:
        current_word=word
    elif current_word != word:
        print(f'{current_word}')
        current_word = word
       
print(f'{current_word}')