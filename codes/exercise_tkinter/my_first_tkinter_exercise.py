#!/usr/bin/python3

from tkinter import *
import tushare as ts

root = Tk("Bruce's Stocks")
pro = ts.pro_api('d2a8b7cc2699fe78afeb938990126811bfa2664b9919082551c33984')

stocks = ['002707','002979.SZ']

listStocks = Listbox(root)

textStock = Text(root,width=800,heigh=500)

for stock in stocks:
    listStocks.insert(0,stock)
#    textStock.insert(END,str(pro.daily(ts_code=stock)))

def listbox_click(event):
    index = listStocks.curselection()
    textStock.insert(END,index)
    textStock.insert(END,listStocks.get(index))
#    textStock.insert(END,"Index:"+listStocks.curselection())
#    textStock.insert(END,listStocks.get(listStocks.curselection()))
    textStock.insert(END,str(pro.daily(ts_code=listStocks.get(index))))
    textStock.insert(END,ts.get_realtime_quotes(['002707']))

listStocks.bind('<<ListboxSelect>>',listbox_click)

listStocks.pack()
textStock.pack()

root.mainloop()