from tkinter import *
import tkinter.scrolledtext as tkscroll
def dummy():
    print("Dummy Function Called")

root=Tk()

# Creating Menu
menu = Menu(root)
root.config(menu=menu)
# File
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="New", command=dummy)
filemenu.add_command(label="Open", command=dummy)
filemenu.add_command(label="Save", command=dummy)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit)
# Help
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label="About F1", command=dummy)

# Text Area
text = tkscroll.ScrolledText(root)
text.pack()

# button = Button(root, text="Useless")
# button.pack()

root.mainloop()
