from tkinter import *

root = Tk()
root.title('')

lf = LabelFrame(root, text='用户登录')
lf.pack(padx=5, pady=5)


l1 = Label(lf, text='账号：')
l1.grid(row=0, column=0)
l2 = Label(lf, text='密码：')
l2.grid(row=1, column=0)

v1 = StringVar()
v2 = StringVar()

e1 = Entry(lf, textvariable=v1)
e1.grid(padx=5, pady=5, row=0, column=1)
e2 = Entry(lf, textvariable=v2, show='·')
e2.grid(padx=5, pady=5, row=1, column=1)



def callback():
    print(v1.get())
    print(v2.get())
    e1.delete(0, END)
    e2.delete(0, END)

def quitRoot():
    root.quit()

b1 = Button(root, text='登录', width=10, command=callback)
b1.pack(padx=5,pady=5, side=LEFT)
b2 = Button(root, text='取消', width=10, command=quitRoot)
b2.pack(padx=5,pady=5, side=RIGHT)

mainloop()
