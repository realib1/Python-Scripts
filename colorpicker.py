from tkinter import *
from tkinter import colorchooser

        
window = Tk()
window.geometry('420x420')

def color():
    colors = colorchooser.askcolor()
    colorHex = colors[1]
    hexColor.set(colorHex)
    window.config(bg=colorHex)
    # lbl.config(text=colorHex)
    
hexColor = StringVar()

btn = Button(window, 
             text='Choose Color', 
             font=(15), 
             command=color)
btn.pack(pady=20, ipady=5)

lbl = Label(window, text="Hex Color:", font=("Verdana",20)).pack(pady=10)
ent = Entry(window, text=hexColor, width=7, font=("Verdana", 20))
ent.pack(ipadx=10, padx=10)


window.mainloop()