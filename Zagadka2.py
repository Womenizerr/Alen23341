import time
import random
for i in range(1,4):
    with open(f'input{i}.txt','r') as file:
        word_line = file.readline().strip()
        print(word_line)
        slovo_line = file.readline().strip()
        print(slovo_line)