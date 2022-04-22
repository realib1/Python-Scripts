from tkinter import *

def test():
    input = etn.get()
    print(input)

window = Tk()
window.title('test')


etn = Entry(window)
etn.pack()


btn = Button(window, text="Test", command=test)
btn.pack()

window.mainloop()