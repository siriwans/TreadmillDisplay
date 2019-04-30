from tkinter import *
from tkinter import messagebox
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
C = Canvas(window, bg="blue", height=width, width=300)
window.title("Loading...")
window.geometry('%dx%d' % (width, height))

filename = PhotoImage(file = "Boeing.png") # just check
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
window.mainloop()