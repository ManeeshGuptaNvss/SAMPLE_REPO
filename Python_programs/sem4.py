import tkinter
win=tkinter.Tk()
label=tkinter.Label(win,text='enter something')
label.grid(row=0,column=0)
data=tkinter.StringVar()
entry=tkinter.Entry(win)

entry.grid(row=1,column=1)
l=entry.get()
button3=tkinter.Button(win,text='show',bg='#00ff00',fg='#ff0000',command=lambda:print(entry.get()))
button3.grid(row=2,column=2)

win.mainloop()
#print(l)
