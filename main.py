from tkinter import Tk, scrolledtext, Menu, filedialog, END, messagebox, simpledialog
import os

root = Tk(className=" TE")
textArea = scrolledtext.ScrolledText(root, width=500, height=70)

#Functions

def newfile():
    if len(textArea.get('1.0', END+'-1c')) > 0:
        if messagebox.askyesno("Save?", "Do you want to save?"):
            savefile()
    textArea.delete('1.0', END+'-1c')
    root.title("Text Editor")

def openfile():
    textArea.delete('1.0', END + '-1c')
    file = filedialog.askopenfile(parent=root, mode='rb', title='Select a file', filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    root.title(os.path.basename(file.name)+"-Text Editor")

    if file != None:
        contents=file.read()
        textArea.insert('1.0', contents)
        file.close()

def savefile():
    file = filedialog.asksaveasfile(mode='w', filetypes=(("Text file", "*.txt"), ("All files", "*.*")))

    if file!=None:
        data=textArea.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def exit1():
    if messagebox.askyesno("Quit","Are you sure you want to quit?"):
        root.destroy()

def findinfile():
    findstring = simpledialog.askstring("Find", "Enter Text")
    textdata = textArea.get('1.0', END)

    occurances=textdata.upper().count(findstring.upper())

    if occurances>0:
        label=messagebox.showinfo("Results", "ocurrances of " + findstring + " = " + str(occurances))

def about():
    label=messagebox.showinfo("About","Python GUI for a text editor")

#Menus


menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)    #Dropdown funtionality
fileMenu.add_command(label="New", command=newfile)
fileMenu.add_command(label="Open", command=openfile)
fileMenu.add_command(label="SaveAs", command=savefile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit1)

editMenu =Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Find", command= findinfile)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)

menu.add_cascade(label="About", command=about)


textArea.pack()
root.mainloop()
