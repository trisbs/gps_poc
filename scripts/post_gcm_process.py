#!/usr/bin/env python
import sys
import os
import RPi.GPIO as GPIO
import time
from threading import Thread

def threadNotify(message):
    os.system("./GCM_Notify '"+message+"'")

if __name__ == "__main__":

    while True:
        sys.stdout.flush()
        line = sys.stdin.readline()
        print ("%s" % line)
        Thread(target = threadNotify, args = (line, )).start()
        
        
