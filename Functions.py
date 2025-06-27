import calc  # This must come after defining globals if there's a circular import

values = []
text = []
current_number = ""
def ver():
    print("BETA")

def credits():
    print("Made by amer spijodic!")

def out():
    print("exiting...")
    import time
    time.sleep(0.1)
    print("Exited!")
    exit()

def clear():
    global values, text, current_number
    print("clear called")
    values.clear()
    text.clear()
    current_number = ""
    calc.refresh()

def b1():
    global current_number, text
    print("b1 pressed")
    current_number += "1"
    text.append("1")
    calc.refresh()

def plus():
    global current_number, values, text
    print("plus pressed")
    if current_number:
        values.append(int(current_number))
        current_number = ""
    text.append("+")
    calc.refresh()
