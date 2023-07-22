import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk

window = Tk()
window.title("Helix Py App")
window.geometry('500x200')

lbl = Label(window, text="Enter URL here >", font=("Cambria", 16))
lbl2 = Label(window, text="", font=("Cambria", 16))

url_text = Entry(window, width=10)

def clicked():
    html = urllib.request.urlopen(url_text.get()).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        lbl2.configure(tag.get('href', None))

btn = Button(window, text="Enter", command=clicked)

lbl.grid(column=0, row=0)
url_text.grid(column=2, row=0)
btn.grid(column=3, row=0)
lbl2.grid(column=0, row=1)


window.mainloop()