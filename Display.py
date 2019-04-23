from tkinter import *



class Display(Frame):

    def __init__(self):

        super().__init__()

        self.initUI()



    def initUI(self):


        canvas = Canvas(self, background = "#4fa4ef")

        canvas.pack(fill = BOTH, expand = 1)

        gif1 = PhotoImage(file = 'trapezoid.gif')

        canvas.create_image(50, 10, image=gif1, anchor=NW)


       # canvas.create_rectangle(30, 10, 120, 80,

        #                        outline="#fb0", fill="#fb0")

        #canvas.create_rectangle(150, 10, 240, 80,

         #                       outline="#f50", fill="#f50")

        #canvas.create_rectangle(270, 10, 370, 80,

         #                       outline="#05f", fill="#05f")

        canvas.pack(fill = BOTH, expand = 1)


def main():

    bgColor = "#4fa4ef"

    window = Tk()
    window.wm_attributes('-fullscreen', 'true')

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%dx%d' % (width, height))

    #window['bg'] = bgColor

    canvas = Canvas(window, background="#4fa4ef")
    canvas.pack(fill=BOTH, expand=1)

    gif1 = PhotoImage(file='buttonL.gif')
    canvas.create_image(width / 3, 100, image=gif1, anchor=CENTER)

    gif2 = PhotoImage(file='buttonM.gif')
    canvas.create_image((2 * width / 3) - (width / 6) + 60, 100, image=gif2, anchor=CENTER)

    labelL = Label(window, text="Low", background=bgColor, font=("Helvetica, 30"))
    labelL.pack()
    labelL.place(x=width / 8 + labelL.winfo_width(), y=(6 * height) / 7 + labelL.winfo_height())


    labelM = Label(window, text="Medium", background=bgColor, font=("Helvetica, 30"))
    labelM.pack()
    labelM.place(x=3 * width / 7 + labelM.winfo_width(), y=(6 * height) / 7 + labelM.winfo_height())


    labelH = Label(window, text="High", background=bgColor, font=("Helvetica, 30"))
    labelH.pack()
    labelH.place(x=(4 * width / 5 + labelH.winfo_width()), y=((6 * height) / 7 + labelH.winfo_height()))


    #dis = Display()

    window.mainloop()



if __name__ == '__main__':

    main()