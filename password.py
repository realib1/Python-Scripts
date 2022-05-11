from tkinter import *
import random
   
def copy():
    window.clipboard_clear()
    window.clipboard_append(lbl_screen)
    window.update()
    

window = Tk()
window.geometry("500x350")
window.title("Password Generator")
window.config(bg="#408080")
frame = Frame(window, bg="#804040", 
              highlightbackground="#0080ff",
              highlightthickness=5,)
frame.pack(padx=5, pady=20)

def passwordgen():
    length = 16
    cap_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_case = 'abcdefghijklmnopqrstuvwxyz'
    nums = '1234567890'
    symbols = '!@#$%^&*()_+-=?'
    gen_password = cap_case + small_case + nums + symbols
    password = ''.join(random.sample(gen_password, length)) 
    # passwrd.config(password)
    lbl_screen.config(text=password)
    # print(password)
    
passwrd = ''
    
lbl = Label(frame, text="Password Generator",  font=("Verdana", 25), bg="#804040", fg="white")
lbl.pack(padx=10, pady=20, ipadx=10)

lbl_screen = Label(frame, width=20, height=1,
            font=("Verdana", 20),
            highlightthickness=3,
            highlightbackground="#004080",
            justify="center")
lbl_screen.pack(padx=10, pady=20)

btn = Button(frame, text="Generate Password", 
             font=("Verdana", 15), fg="white", 
             activeforeground="white",
             activebackground="#004080",
             bg="#004080",
             command=passwordgen)
btn.pack(padx=10, pady=10)


copy_btn = Button(frame, 
             text=' Copy Password', 
             font=("Verdana", 15), 
             command=copy)

copy_btn.pack(pady=10)



window.mainloop()

