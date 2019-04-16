from tkinter import *

bgColor = "#4fa4ef"

window = Tk()
window.wm_attributes('-fullscreen','true')

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry('%dx%d' % (width, height))
window['bg'] = bgColor

labelL = Label(window, text="Low", background = bgColor, font=("Helvetica, 30"))
labelL.pack()
labelL.place(x=width/8 + labelL.winfo_width(), y = (6*height)/7 + labelL.winfo_height())

labelM = Label(window, text="Medium", background = bgColor, font=("Helvetica, 30"))
labelM.pack()
labelM.place(x=3*width/7 + labelM.winfo_width(), y = (6*height)/7 + labelM.winfo_height())

labelH = Label(window, text="High", background = bgColor, font=("Helvetica, 30"))
labelH.pack()
labelH.place(x=4*width/5 + labelH.winfo_width(), y = (6*height)/7 + labelH.winfo_height())


window.mainloop()