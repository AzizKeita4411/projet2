from tkinter import *

root = Tk()
root.title("My First GUI App")
root.geometry("300x200")

label = Label(root, text="Hello, Tkinter!")
label.pack()

button = Button(root, text="Click me")
button.pack()

entry = Entry(root)
entry.pack()

text = Text(root)
text.pack()


root.mainloop()
