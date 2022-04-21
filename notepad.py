#iports the neccesary libraries to help with the project
from tkinter import *
# import win32api
from tkinter import filedialog
from tkinter.messagebox import askyesno, INFO, askyesnocancel

# Save button triggers for to save your notes.
def save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[('Text File', '.txt'),
                                               ('HTML', '.html'),
                                               ('Python', '.py'),
                                               ('PDF', '.pdf'),
                                               ('All files', '.*')])
    if file is None:
        return

    savetext = str(text.get("1.0", END))
    file.write(savetext)
    file.close()

# Print Button to print your notes
def file_print():
    print_file = filedialog.askopenfile(
        initialdir="/",
        title="Select File to Print",
        defaultextension=".txt", filetypes=[('Text File', '.txt'),
                                            ('HTML', '.html'),
                                            ('Python', '.py'),
                                            ('PDF', '.pdf'),
                                            ('All files', '.*')])
    # if print_file:
    #     win32api.ShellExecute(0, "print", print_file, None, ".", 0)

# Discard button to dicard or cancle note in progress
def discard():
    answer = askyesno(
        title='Confirmation',
        message='Are you sure you want to discard?',
        icon=INFO)

    if answer:
        window.destroy()

# Open nots button to open an existing note
def open_note():
    open_file = filedialog.askopenfile(title="Open an Existing File", defaultextension=('All files', '.*'),
                                       filetypes=[('Text File', '.txt'),
                                                  ('HTML', '.html'),
                                                  ('Python', '.py'),
                                                  ('PDF', '.pdf')])
    try:
        file_open = open(open_file, "w+")
        file_open.write(open_file)
        file_open.get()
        # return file_open
    except:
        return

# Exit notepad from the file menu

# def file_exit():
#     confirm = askyesnocancel(title="Confirmation", message="Are you sure you want to exit?")

#     if confirm:
#         exit()

    
# window setup

window = Tk()
window.title("Notepad")
window.config(bg='skyblue')

# Adding icon photo of the project
iconphoto = PhotoImage(file="notes.png")
window.iconphoto(False, iconphoto)

# Making frame for the project
frame = Frame(window, bg="skyblue")
frame.pack(pady=10, ipadx=10, ipady=10,padx= 10, expand=True, fill=BOTH)


# Menu bar

# menu_btn = Menu(frame)
# window.config(menu=menu_btn)

# New note from menu bar

# def new_note():
#     top = Toplevel(window)
#     top.config(bg="skyblue")
#     frame = Frame(top, bg="skyblue")
#     frame.pack(pady=5, ipadx=10, ipady=5, expand=True, fill=BOTH)
    
#     lbl = Label(frame,
#             text="Notepad",
#             bg="skyblue",
#             font=("Verdana", 30))
#     lbl.pack()

#     text = Text(frame,
#                 fg="#00274f",
#                 bg="#ffffa4",
#                 font=("Ink free", 15),
#                 height=15,
#                 width=30,
#                 padx=10,
#                 pady=5)
#     text.insert(END, "#Start writing your note here...")
#     text.pack(expand=True, fill=BOTH, pady=5)

#     btn_print = Button(frame,
#                     text="Print",
#                     font=("Verdana", 15),
#                     bg="#1f2291",
#                     fg="black",
#                     activebackground="#1f2291",
#                     activeforeground="black",
#                     command=file_print)
#     btn_print.pack(padx=15, ipadx=15, side=LEFT)

#     btn_save = Button(frame,
#                     text="Save",
#                     font=("Verdana", 15),
#                     bg="#00c161",
#                     fg="black",
#                     activebackground="#00c161",
#                     activeforeground="black",
#                     command=save)
#     btn_save.pack(padx=5, pady=5, ipadx=15, side=LEFT)

#     btn_discard = Button(frame,
#                         text="Discard",
#                         font=("Verdana", 15),
#                         bg="#eb0214",
#                         fg="black",
#                         activebackground="#eb0214",
#                         activeforeground="black",
#                         command=discard)
#     btn_discard.pack(padx=15, ipadx=4, side=LEFT)

    
    
#     top.mainloop()

# Menu bar build

# file_menu = Menu(menu_btn, tearoff=0, font=("Verdana", 10))
# menu_btn.option_add("*Font", "Verdana 20")
# menu_btn.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New note", command=new_note, font=("Verdana", 10))
# file_menu.add_command(label="Open", command=open_note, font=("Verdana", 10))
# file_menu.add_separator()
# file_menu.add_command(label="Exit", font=("Verdana", 10), command=file_exit)

# Project Title

lbl = Label(frame,
            text="Notepad",
            bg="skyblue",
            font=("Verdana", 30))
lbl.pack()

#Project text area/ Notepad

text = Text(frame,
            fg="#00274f",
            bg="#ffffa4",
            font=("Ink free", 15),
            height=15,
            width=30,
            padx=10,
            pady=5)
text.insert(END, "#Start writing your note here...")
text.pack(expand=True, fill=BOTH, pady=5)

# Print button to print Notes

btn_print = Button(frame,
                   text="Print",
                   font=("Verdana", 15),
                   bg="#1f2291",
                   fg="black",
                   activebackground="#1f2291",
                   activeforeground="black",
                   command=file_print)
btn_print.pack(padx=15, ipadx=15, side=LEFT)

#Save button to save new notes

btn_save = Button(frame,
                  text="Save",
                  font=("Verdana", 15),
                  bg="#00c161",
                  fg="black",
                  activebackground="#00c161",
                  activeforeground="black",
                  command=save)
btn_save.pack(padx=5, pady=5, ipadx=15, side=LEFT)

#Discard button to exit note

btn_discard = Button(frame,
                     text="Discard",
                     font=("Verdana", 15),
                     bg="#eb0214",
                     fg="black",
                     activebackground="#eb0214",
                     activeforeground="black",
                     command=discard)
btn_discard.pack(padx=15, ipadx=4, side=LEFT)

# lbl = Label(text="Make a new note").pack()

#Closing wondow
window.mainloop()
