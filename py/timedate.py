from tkinter import *
from time import *

def time_update():
    time_string = strftime("%I:%M:%S %p")
    time_lbl.config(text=time_string)
    
    # time_string = strftime("%A")
    # day_lbl.config(text=time_string)
    
    time_string = strftime("%A %B %d, %Y")
    date_lbl.config(text=time_string)
    
    window.after(1000, time_update)
    
window = Tk()
window.title("Time and Date")
window.config(bg="green")

frame = Frame(window, bg="green")
frame.pack(expand=True, fill=BOTH)

time_lbl = Label(frame, font=("Fira Code", 40), bg="black", fg="green")
time_lbl.pack(ipadx=15)

# day_lbl = Label(window, font=("Fia Code", 20))
# day_lbl.pack()

date_lbl = Label(frame, font=("Ubuntu", 20), bg="green")
date_lbl.pack(ipadx=10, ipady=10)

time_update()

window.mainloop()