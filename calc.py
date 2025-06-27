import tkinter as tk
from tkinter import messagebox
import importlib
import Functions as func
importlib.reload(func)
func.clear
def out2():

    func.out()
    exit()
def refresh():
    global label
    label.config(text=func.text)
    root.after(1, refresh) 

root = tk.Tk()
wip = tk.Toplevel(root)
label = tk.Label(wip, text="Hello!, this is in wip so use the exit button")
label.pack(pady=20)
menu_bar = tk.Menu(root)
misc_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Misc", menu=misc_menu)

root.config(menu=menu_bar)

options_submenu = tk.Menu(misc_menu, tearoff=0)
options_submenu.add_command(label="Credits", command=func.credits)
options_submenu.add_command(label="Exit", command=func.out)
options_submenu.add_command(label="Calc version", command=func.ver)

misc_menu.add_cascade(label="Genral", menu=options_submenu)



button_info = [
    ("9",     (1, 0)),
    ("8",     (1, 1)),
    ("7",     (1, 2)),
    ("+",     (1, 3), func.plus),
    ("6",     (2, 0)),
    ("5",     (2, 1)),
    ("4",     (2, 2)),
    ("-",     (2, 3)),
    ("3",     (3, 0)),
    ("2",     (3, 1)),
    ("1",     (3, 2), func.b1),
    ("*",     (3, 3)),
    ("0",     (4, 0)),
    ("/",     (4, 1)),
    ("=",     (4, 2)),
    ("Clear",     (4, 3), func.clear),

]


for item in button_info:
    if len(item) == 3:
        text, (r, c), command = item
        tk.Button(root, text=text, width=8, height=3, command=command).grid(row=r, column=c)
    else:
        text, (r, c) = item
        tk.Button(root, text=text, width=8, height=3).grid(row=r, column=c)

paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned.grid(row=0, column=0, columnspan=5)
label = tk.Label(paned, text=func.text, bg="gray26", width=35, height=3)
paned.add(label)


root.mainloop()


