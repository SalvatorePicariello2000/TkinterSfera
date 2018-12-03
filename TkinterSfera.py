from tkinter import *
from tkinter import ttk


def Palla (*args):
    r=msg_Entry.get()
    r=int (raggio)
    volume=(4/3) * 3.14 * r**3
    print(volume)
    msg_Label.set(volume)


root=Tk()
root.title ("È questa la palla?")

mainframe=ttk.Frame(root, padding="20 30 20 30")
mainframe.grid(column=0, row=0)

msg_Label=StringVar()
msg_Entry=StringVar()
rag=ttk.Entry(mainframe, text="inserisci raggio").grid(column=0, row=0)
R=ttk.Entry(mainframe, width=3, textvariable=msg_Entry).grid(column=1, row=0)
Button=ttk.Button (mainframe, text="calcolo=", command=Palla).grid(column=1, row=1)
Vol=ttk.Label(mainframe, text="volume=").grid(column=0, row=2)
V=ttk.Label(mainframe, textvariable=msg_Label).grid(column=1, row=2)

root.mainloop()