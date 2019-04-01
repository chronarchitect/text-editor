from tkinter import *
import tkinter.scrolledtext as tkscroll
import tkinter.filedialog as fdialog
import tkinter.messagebox as msgbx
import tkinter.simpledialog as sdialog

def dummy():
    print("Dummy Function Called")

root=Tk()
root.title("Editor")

# Text Area
text = tkscroll.ScrolledText(root)
text.pack()

# Menu Functions
def open_command():
    file = fdialog.askopenfile(parent=root, title='Select a File')
    if file != None:
        contents = file.read()
        text.insert(1.0, contents)
        file.close()

def new_command():
    fname = sdialog.askstring(title="New", prompt="Enter new filename", parent=root)
    if fname != "":
        fname = fname.strip() + ".txt"
        file = open(fname, mode="w+")
        contents = file.read()
        text.insert(1.0, contents)
        file.close()
        
def exit_command():
    if msgbx.askokcancel(title="Quit?", message="Do you really want to Quit?"):
        root.destroy()

def save_command():
    file = fdialog.asksaveasfile(mode='w')
    if file != None:
        data = text.get('1.0', END+'-1c')
        file.write(data)
        file.close()
def about_command():
    msgbx.showinfo(title)
    
#Creating menu

menu = Menu(root)
root.config(menu=menu)
# File
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu=filemenu)
filemenu.add_command(label="New", command=new_command)
filemenu.add_command(label="Open", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
# Help
helpmenu = Menu(menu)
menu.add_cascade(label = "Help", menu=helpmenu)
helpmenu.add_command(label="About", command=dummy)

# button = Button(root, text="Useless")
# button.pack()

root.mainloop()
