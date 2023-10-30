#!/usr/bin/python3
import time

for i in range(30):
    for j in range(30):
        if (i % 2 == 0):
            print('◉', end=' ')
        else:
            print('◯', end=' ')
        time.sleep(0.05)
    print()


