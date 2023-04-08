#!/usr/bin/python3
import sys
import os
import time

mensaje = input()

sys.stdout.write('\n Proceso hijo A (PID: %d -- PPID: %d) \n'% (os.getpid(), os.getppid()))
time.sleep(5)
sys.stdout.write('Mensaje del padre: ' +mensaje+ '\n')
sys.stdout.flush()
