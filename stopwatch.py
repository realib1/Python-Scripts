from time import  *
from tkinter import *



thiking = False

hour, minute, second, millisecond = 0, 0, 0, 0

def start():
    global thiking
    if not thiking:
        update()
        thiking = True 
        

def stop():
    global thiking
    if thiking:
        watch_lbl.after_cancel(update_time)
        thiking =  False
        
        
 
def reset():
    global thiking
    if thiking:
        watch_lbl.after_cancel(update_time)
        thiking =  False
    global hour, minute, second, millisecond
    hour, minute, second, millisecond = 0, 0, 0, 0
    watch_lbl.config(text="00:00:00:00")
  
def update():
    global hour, minute, second, millisecond   
    millisecond += 1
    if millisecond  == 60:
        second +=1
        millisecond = 0
    if second == 60:
        minute +=1
        second = 0
    if minute == 60:
        hour +=1
        minute = 0
    hour_format = f'{hour}'  if hour > 9  else f'0{hour}' 
    minute_format = f'{minute}' if minute > 9 else f'0{minute}'
    second_format = f'{second}'  if second > 9  else f'0{second}'
    millisecond_format = f'{millisecond}'  if millisecond > 9  else f'0{millisecond}'
    
    watch_lbl.config(text=hour_format + ':' + minute_format + ':' + second_format + ':' + millisecond_format)
    
    global update_time
    
    update_time = watch_lbl.after(10, update)
 
 
def lap():
    print(watch_lbl.cget('text'))
    lap_str = watch_lbl.cget('text')
    lbl_lap = Label(frame, text=lap_str, font=("Verdana", 15))
    lbl_lap.pack(side="bottom")
   
window = Tk()
window.title("Stop Clock")
window.geometry("500x300")
window.config(bg="#004080")

frame = Frame(window, bd=5, 
              highlightthickness=5, 
              highlightbackground="black", 
              highlightcolor="black")
frame.config(bg="#004080")
frame.pack(ipadx=20, ipady=10, padx=10, pady=10)


lbl = Label(frame, text="Stop Watch", bg="#004080", font=("Verdana", 35, "bold"))
lbl.pack(ipadx=5)

watch_lbl = Label(frame, text="00:00:00:00", bg="#004080", font=("Fira Code", 50, "bold"))
watch_lbl.pack(ipadx=30, ipady= 10)

btn_start = Button(frame, text="Start", font=("Verdana", 15), command=start)
btn_start.pack(side="left", ipadx=5, padx=20)


btn_lap = Button(frame, text="Lap", font=("Verdana", 15), command=lap)
btn_lap.pack(side="left", ipadx=5, padx=20)

btn_stop = Button(frame, text="Stop", font=("Verdana", 15), command=stop)
btn_stop.pack(side="left", ipadx=5, padx=20)

btn_reset = Button(frame, text="Reset", font=("Verdana", 15), command=reset)
btn_reset.pack(side="left", ipadx=5, padx=20)

window.mainloop()