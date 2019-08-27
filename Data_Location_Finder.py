from os import*
import matplotlib.pyplot as plt
import numpy as np
from tkinter import*
import wikipedia as wiki
import tkinter as tk
import pandas as pd
from tkinter import font, colorchooser, filedialog, messagebox

class Location_Finder:
    def copy(self):
        self.shell.clipboard_clear()
        self.shell.clipboard_append(self.shell.selection_get())
    def cut(self):
        self.copy()
        self.shell.delete('sel.first', 'sel.last')
        self.shell.delete(1.0, END)
    def ans_find_on_wiki(self):
        question_val = self.entry.get()
        answer_val = wiki.summary(question_val)
        self.shell.delete(1.0, END)
        self.shell.insert(INSERT,answer_val)
    def __init__(self,master):
        self.master = master
        master.title("Location Finder")
        self.shell = Text(bg="black",fg="white", bd=2,wrap=WORD,font=('Calibri', 15))
        self.scroll_right = Scrollbar()
        self.scroll_right.pack(side=RIGHT, fill=Y)
        self.scroll_right.config(command=self.shell.yview)
        self.shell.config(yscrollcommand = self.scroll_right.set)
        # self.scroll_right = Scrollbar()
        # self.scroll_right.pack(side=BOTTOM, fill=X)
        # self.scroll_right.config(command=self.shell.xview)
        # self.shell.config(xscrollcommand=self.scroll_right.set)
        ####-------------Frame is Here that means All Button center is Here....-----------#####
        self.frame = Frame(master,bd=5,bg='white')
        self.frame.pack(side=LEFT)
        ####-------------Entry Fild is Here that means Search center is Here....-----------#####
        self.entry = Entry(self.frame,bg='white',fg='black',font=('Calibri',20) )
        self.entry.grid(row=0,column=0)
        self.button = Button(self.frame,text="Search",bg="blue",fg="white", width=10,font=('Calibri',15),command=self.ans_find_on_wiki)
        self.button.grid(row=0, column=1)
        #
        # for i in range(50):
        #     # self.frame.insert(END,'this is all about bachouti',i)
        #     self.shell.insert(END,'this ia something about shell menu...',i)
        self.shell.pack(fill = BOTH, expand=1)
        self.main_menu = Menu(bg="black",fg="white")
        self.master.config(menu=self.main_menu)
        #Creating File
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu = self.file_menu)
        self.file_menu.add_command(label="New Tab")
        self.file_menu.add_command(label="New Window")
        self.file_menu.add_command(label="Close Tab")
        self.file_menu.add_command(label="Close Window")
        #creating Edit Menu
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Copy as HTML5")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Paste", command=lambda: self.shell.insert(INSERT, self.shell.clipboard_get()))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.shell.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.shell.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Sellect All")
        self.edit_menu.add_command(label="Prefrences")
        #creating View Menu
        self.View_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="View", menu=self.View_menu)
        self.View_menu.add_command(label="Open")
        self.View_menu.add_command(label="Show Menubar")
        self.View_menu.add_command(label="Zoom")
        self.View_menu.add_command(label="Zoom Out")
       #creating Tools Menu
        self.tools_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Tools", menu=self.tools_menu)
        self.tools_menu.add_command(label="Import others lib")
        self.tools_menu.add_command(label="Kali Tools")
        #creating Search Menu
        self.Search_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Search", menu=self.Search_menu)
        self.Search_menu.add_command(label="Find...")
        self.Search_menu.add_command(label="Find Next!")
        self.Search_menu.add_command(label="Find Previous")
        self.Search_menu.add_command(label="Clear History")
        # creating Terminal----------------------------------------------------------
        self.Terminal_menu = Menu(self.main_menu, font=('Calibri', 15), tearoff=False)
        self.main_menu.add_cascade(label="Terminal", menu=self.Terminal_menu)
        self.Terminal_menu.add_command(label="Set Terminal Sizes")
        self.Terminal_menu.add_separator()
        self.Terminal_menu.add_command(label="800*300", command=lambda: self.master.geometry('800x300+200+30'))
        self.Terminal_menu.add_command(label="800*430", command=lambda: self.master.geometry('800x430+200+30'))
        self.Terminal_menu.add_command(label="1320*430", command=lambda: self.master.geometry('1320x430+120+30'))
        self.Terminal_menu.add_command(label="1300*530", command=lambda: self.master.geometry('1300x530+120+30'))
        self.Terminal_menu.add_separator()
        self.Terminal_menu.add_command(label="Middle Screen", command=lambda: self.master.geometry('1300x620+120+30'))
        self.Terminal_menu.add_command(label="Full Screen", command=lambda: self.master.geometry('1820x980+-2+0'))

        #creating Help Menu
        self.Help_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Help", menu=self.Help_menu)
        self.Help_menu.add_command(label="Contents")
        self.Help_menu.add_command(label="About")
        self.Help_menu.add_command(label="Commands")

        ####---All The Frame Button is Here that means All Button center is Here for Frame.--#####
        self.button = Button(self.frame, text="Config Target", width=13, font=('Calibri', 13))
        self.button.grid(row=12, column=0)
        self.button = Button(self.frame, text="Import File", width=13, font=('Calibri', 13))
        self.button.grid(row=15, column=0)
        self.button = Button(self.frame, text="Display Config", width=13, font=('Calibri', 13))
        self.button.grid(row=17, column=0)
        self.button = Button(self.frame, text="Display Info", width=13, font=('Calibri', 13))
        self.button.grid(row=20, column=0)
        self.button = Button(self.frame, text="Check on Map", width=13, font=('Calibri', 13))
        self.button.grid(row=22, column=0)
        self.button = Button(self.frame, text="Track Now", width=13, font=('Calibri', 13))
        self.button.grid(row=25, column=0)
        self.button = Button(self.frame, text="Details", width=13, font=('Calibri', 13))
        self.button.grid(row=27, column=0)
        self.button = Button(self.frame, text="Contats", width=13, font=('Calibri', 13))
        self.button.grid(row=30, column=0)
        self.button = Button(self.frame, text="Message Box", width=13, font=('Calibri', 13))
        self.button.grid(row=32, column=0)
        self.button = Button(self.frame, text="DirDrive", width=13, font=('Calibri', 13))
        self.button.grid(row=35, column=0)
        self.button = Button(self.frame, text="Full Controll", width=13, font=('Calibri', 13))
        self.button.grid(row=37, column=0)
        self.button = Button(self.frame, text="Simple Controll", width=13, font=('Calibri', 13))
        self.button.grid(row=40, column=0)
        self.button = Button(self.frame, text="E-mail", width=13, font=('Calibri', 13))
        self.button.grid(row=41, column=0)
        self.button = Button(self.frame, text="FaceBook", width=13, font=('Calibri', 13))
        self.button.grid(row=42, column=0)
        self.button = Button(self.frame, text="Instagram", width=13, font=('Calibri', 13))
        self.button.grid(row=43, column=0)

root = Tk()
root.geometry('1000x605+220+50')
root.resizable(0,0)
RameshKumarDas= Location_Finder(root)

root.mainloop()

inp = input("Enter any key for Exit from program: ")