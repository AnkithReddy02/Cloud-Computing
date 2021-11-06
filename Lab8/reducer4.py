#!/usr/bin/python3
import sys
current_word=None
current_count=0
words={}
offsetlis = [] 
for line in sys.stdin:
    line=line.strip().split(',')            
    word,offset=line[0],line[1]
    if word in words:
        words[word].append(offset)
    else:
        words[word]=[offset]

    if current_word == None:
        offsetlis.append(offset)
        current_word = word
    
    elif current_word == word :
        offsetlis.append(offset)
    else:
        print(f'{current_word},{offsetlis}')
        current_word = word;
        offsetlis = [offset]



print(f'{current_word},{offsetlis}')
    