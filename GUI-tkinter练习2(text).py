from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, 'hello!')

text.tag_add('tag1', '1.1', '1.4')
text.tag_config('tag1', background='yellow', foreground='red')

mainloop()
