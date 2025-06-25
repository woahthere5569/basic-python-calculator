import time

global value ; 0

def credits():
    print("Made by amer spijodic!")

def out():
    print("exiting...")
    time.sleep(0.1)
    print("Exited!")
    exit()

def clear():
    global value
    value = 0
    print("works")
