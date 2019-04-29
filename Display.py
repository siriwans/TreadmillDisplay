import PIL.Image
import PIL.ImageTk
from tkinter import *
import time
import os
import threading

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
    pause = False

    window = Tk()
    window.wm_attributes('-fullscreen', 'true')

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%dx%d' % (width, height))

    #window['bg'] = bgColor

    canvas = Canvas(window, background="#4fa4ef")
    canvas.pack(fill=BOTH, expand=1)

    # Top Buttons (images)

    gif1 = PhotoImage(file='buttonL.gif')
    canvas.create_image((width / 2) - 150, 0, image=gif1, anchor=NE)

    gif2 = PhotoImage(file='buttonM.gif')
    canvas.create_image((width / 2), 0, image=gif2, anchor=N)

    gif3 = PhotoImage(file='buttonR.gif')
    canvas.create_image((width / 2) + 150, 0, image=gif3, anchor=NW)

    # Bottom image

#    gif4 = PhotoImage(file='bottom_rectangle.gif')
    pil_image4 = PIL.Image.open("bottom_rectangle.gif")
    width_og, height_og = pil_image4.size
    factor = 1.5
    heighti = int(height_og * factor)
    pil_image42 = pil_image4.resize((width, heighti), PIL.Image.ANTIALIAS)
    tk_image = PIL.ImageTk.PhotoImage(pil_image42)
    canvas.create_image((width / 2), height, image=tk_image, anchor=S)

    rect1 = PhotoImage(file='Rect1.gif')
    canvas.create_image((width / 3), (height / 3), image=rect1, anchor=N)

    rect3 = PhotoImage(file='Rect3.gif')
    canvas.create_image(((2 * width) / 3), (height / 3), image=rect3, anchor=N)

    rect2 = PhotoImage(file='Rect2.gif')
    canvas.create_image((width / 2), (height / 2), image=rect2, anchor=N)

    # Speed Button Labels

    pauseButton = Button(height=0,bd=0,image= rect2,relief=FLAT,bg="#0b5394",activebackground="#0b5394",activeforeground="#0b5394",highlightcolor="#0b5394") #command=lambda:time_count(window, bgColor, width, height))
    pauseButton.pack()
    pauseButton.place(x=(width / 2.35), y=(height / 2))

    labelL = Label(window, text="Low", background=bgColor, font=("Helvetica, 30"))
    labelL.pack()
    labelL.place(x=width / 8 + labelL.winfo_width(), y=(6 * height) / 7 + labelL.winfo_height())


    labelM = Label(window, text="Medium", background=bgColor, font=("Helvetica, 30"))
    labelM.pack()
    labelM.place(x=3 * width / 7 + labelM.winfo_width(), y=(6 * height) / 7 + labelM.winfo_height())


    labelH = Label(window, text="High", background=bgColor, font=("Helvetica, 30"))
    labelH.pack()
    labelH.place(x=(4 * width / 5 + labelH.winfo_width()), y=((6 * height) / 7 + labelH.winfo_height()))


    t1 = threading.Thread(target=time_count, args=(window, width, height))
    t1.start()

    # dis = Display()
    window.mainloop()

# def checkPauseTime(pause):
#     while (pause == True):
#         time.sleep(1)

def time_count(window, width, height):
    sec = int(0)
    min = int(0)
    hrs = int(0)
    while(1):
        if sec > 59:
            sec = 0
            min = min + 1
        if min > 59:
            min = 0
            hrs = hrs + 1
        sec = sec + 1
        timeStr = "{:02d}:{:02d}:{:02d}".format(hrs, min, sec)
        labelTime = Label(window, text=timeStr, background="#0b5394", font=("Helvetica, 20"), fg="#ffffff")
        labelTime.pack()
        labelTime.place(x=(3.9 * width / 6 + labelTime.winfo_width()), y=((2.7 * height) / 7 + labelTime.winfo_height()))
        time.sleep(1)

if __name__ == '__main__':
    main()