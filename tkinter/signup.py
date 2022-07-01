from  tkinter import *



     


window = Tk()
window.title("Sign Up Form")
window.geometry("600x600")
window.configure(bg="#008080")

def verify():
    acc_ent.config(text="Verify Your account from your email address.")
    
        
    
    
frame = Frame(window, bg="#6ccdd5", bd=5, highlightthickness=5, highlightbackground="black",)
frame.pack(expand=True, fill=BOTH, padx=40, pady=20)

ttl = Label(frame, text="Sign Up For an account", 
            bg="#6ccdd5", font=("Verdana", 20)).pack()

fname_lbl = Label(frame, text="Firstname:", 
            bg="#6ccdd5", font=("Verdana", 15)).place(x= 20, y= 50)

fname_ent = Entry(frame, font=("Verdana", 15), width=25).place(x= 150, y= 50)

lname_lbl = Label(frame, text="Lastname:", 
            bg="#6ccdd5", font=("Verdana", 15)).place(x= 20, y= 100)

lname_ent = Entry(frame, font=("Verdana", 15), width=25).place(x= 150, y= 100)

email_lbl = Label(frame, text="Email:", 
            bg="#6ccdd5", font=("Verdana", 15)).place(x= 20, y= 150)

email_ent = Entry(frame, font=("Verdana", 15), width=25).place(x= 150, y= 150)

password_lbl = Label(frame, text="Password:", 
            bg="#6ccdd5", font=("Verdana", 15),).place(x= 20, y= 200)

password_ent = Entry(frame, font=("Verdana", 15), width=25, show="*").place(x= 150, y= 200)

confirm_lbl = Label(frame, text="Confirm:", 
            bg="#6ccdd5", font=("Verdana", 15)).place(x= 20, y= 250)

confirm_ent = Entry(frame, font=("Verdana", 15), width=25, show="*").place(x= 150, y= 250)


signup_btn = Button(frame, text="Signup", 
                    font=("Verdana", 15),
                    bg="#008080", activebackground="#008080", command=verify).place(x=250, y= 300)

acc_ent = Label(frame, cursor="xterm", font=("Verdana", 15), width=35, bg="#6ccdd5", bd=0)
acc_ent.pack(side=BOTTOM, ipadx=20)

window.mainloop()