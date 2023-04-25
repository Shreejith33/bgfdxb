from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

number = Label(root)
prlist = Label(root)
label_sortedList = Label(root)
label_THING = Label(root)

label_THING['text'] = "1 - 10: Bottle 11 - 20: Tiffin 21 - 30: ID Card31 - 40: Chocolates41 - 50: Chips51 - 60: Tickets61 - 70: Hanky71 - 100: Anything!"

def Start() :
    number['text'] = random.sample(range (1, 100), 1)
    list = random.sample(range (1, 100), 1)
    prlist['text'] = str(list)
    list.sort()
    label_sortedList['text'] = str(list)
    

    number.place(relx = 0.5, rely = 0.5, anchor = CENTER)
    prlist.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    label_sortedList.place(relx = 0.5, rely = 0.7, anchor = CENTER)

Click = Button(root, text = "Random Nunber", command = Start)
Click.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()