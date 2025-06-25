import tkinter as tk
import importlib
import Functions as func
importlib.reload(func)
func.clear
def out2():

    func.out()
    exit()
print("Loaded Functions.py from:", func.__file__)

root = tk.Tk()

button_info = [
    ("9",     (1, 0)),
    ("8",     (1, 1)),
    ("7",     (1, 2)),
    ("+",     (1, 3)),
    ("6",     (2, 0)),
    ("5",     (2, 1)),
    ("4",     (2, 2)),
    ("-",     (2, 3)),
    ("3",     (3, 0)),
    ("2",     (3, 1)),
    ("1",     (3, 2)),
    ("*",     (3, 3)),
    ("0",     (4, 0)),
    ("Clear",     (4, 1),func.clear),
    ("Exit",     (4, 2), func.out),
    ("Credits",     (4, 3), func.credits),

]


for item in button_info:
    if len(item) == 3:
        text, (r, c), command = item
        tk.Button(root, text=text, width=8, height=3, command=command).grid(row=r, column=c)
    else:
        text, (r, c) = item
        tk.Button(root, text=text, width=8, height=3).grid(row=r, column=c)

paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.add(tk.Label(paned, text=func.value, bg="lightyellow", width=20, height=3))
paned.grid(row=0, column=0, columnspan=5)

root.mainloop()


