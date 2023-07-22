import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import tkinter as tk

window = Tk()
window.title("Countdown Timer")
window.geometry('500x200')
window.config(bg='#345')

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")

intro = tk.Label(window, text="This is a countdown timer!", font=("Cambria", 16,), bg="#345", fg="white")
prompt = tk.Label(window, text="How many seconds?", font=("Cambria", 16), bg="#345", fg="white")
hrs = Entry(window, width=3, font=("Arial",18,""), textvariable=hour)
min = Entry(window, width=3, font=("Arial",18,""), textvariable=minute)
sec = Entry(window, width=3, font=("Arial",18,""), textvariable=second)

def countdown():
    try:
        # store the user input
        user_input = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        messagebox.showwarning('', 'Invalid Input!')
    while user_input >-1:
        # divmod(firstvalue = user_input//60, secondvalue = user_input%60)
        mins,secs = divmod(user_input,60)
        # Converting the input entered in mins or secs to hours,
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        # store the value up to two decimal places
        # using the format() method
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        # updating the GUI window 
        window.update()
        time.sleep(1)
        # if user_input value = 0, then a messagebox pop's up
        # with a message
        if (user_input == 0):
            btn.configure(text='Start Again!')
            messagebox.showinfo("Time Countdown", "Done!")
            break
        # decresing the value of temp 
        # after every one sec by one
        user_input -= 1

btn = tk.Button(window, text='Start Countdown!', bd='5', command=countdown)

intro.place(
    x=130, 
    y=5)
prompt.place(
    x=130, 
    y=35)
hrs.place(
    x=130, 
    y=95)
min.place(
    x=180, 
    y=95)
sec.place(
    x=230, 
    y=95)
btn.place(
    x=130, 
    y=145)

window.mainloop()