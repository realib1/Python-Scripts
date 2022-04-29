from tkinter import  *


window = Tk()
window.title("Sing Up")
window.geometry("500x500")

f_lbl = Label(window, text="First Name:", font=("Verdana", 10), width=20)
f_lbl.place(x=10, y=30)

f_ent = Entry(window, font=("Verdana", 10), width=20)
f_ent.place(x=150, y= 30)


l_lbl = Label(window, text="Last Name:", font=("Verdana", 10), width=20)
l_lbl.place(x=10, y= 60)                 

l_ent = Entry(window, font=("Verdana", 10), width=20)
l_ent.place(x=150, y=60)

s_lbl = Label(window, text="Student ID:", font=("Verdana", 10), width=20 )
s_lbl.place(x=10, y=90)


s_ent = Entry(window, font=("Verdana", 10), width=20)
s_ent.place(x=150, y=90)


btn = Button(window, text="DISPLAY", bg="blue", font=("Verdana", 10), width=20)

btn.place(x=80, y=120)



window.mainloop()