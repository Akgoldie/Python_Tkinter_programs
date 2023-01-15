from tkinter import *
from tkinter import messagebox
obj=Tk()
obj.geometry("500x500")

def submit():
    messagebox.showinfo("INFO","It's AK")
button=Button(obj,text="Arun Kumar", command=submit)
button.pack()
obj.mainloop()