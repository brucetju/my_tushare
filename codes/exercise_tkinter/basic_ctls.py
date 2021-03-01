
# Includes:
#
#

from tkinter import Tk,Text,Button,Frame,END
from datetime import datetime

top = Tk()
#top.geometry('1000x1000+1000+1000')

txtInput = Text(top,width=20,height=1)
txtInput.pack()

txtMsg = Text(top)
txtMsg.pack()

def btn1_click():
    txtMsg.insert('end','btn1 clicked.\r\n' + txtInput.get(1.0,END))

btn1 = Button(top,text='btn1',command = btn1_click)
btn1.pack()


txtTime = Text(top)

def txtTime_tick():
    txtTime.delete(1.0,END)
    txtTime.insert('end',datetime.now())
    txtTime.after(1000,txtTime_tick)

txtTime.pack()




if __name__ == '__main__':
    txtTime_tick()
    top.mainloop()
