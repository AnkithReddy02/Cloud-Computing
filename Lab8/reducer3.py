#!/usr/bin/python3
import sys
current_word=None
current_count=0
words={}
for line in sys.stdin:
    word,count=line.strip().split(',')
    count = (int)(count)
    if word in words:
        words[word]+=count
    else:
        words[word]=count

for word in words:
    print(f'{word},{words[word]}')
    