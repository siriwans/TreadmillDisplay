import PIL.Image
import PIL.ImageTk
from tkinter import *
import time
import os
import threading
#import RPi.GPIO as GPIO


class Display(Frame):

    def __init__(self):

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

def anotherWindow():

    window2 = Tk()
    window2.wm_attributes('-fullscreen', 'true')

    width = window2.winfo_screenwidth()
    height = window2.winfo_screenheight()
    window2.geometry('%dx%d' % (width, height))

    # window['bg'] = bgColor

    canvas = Canvas(window2, background="#4fa4ef")
    canvas.pack(fill=BOTH, expand=1)

    # Top Buttons (images)

    pil_plane = PIL.Image.open("buttonL.gif")
    width_og, height_og = pil_plane.size
    factor = 1
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_plane1 = pil_plane.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif1 = PIL.ImageTk.PhotoImage(pil_plane1)
    # canvas.create_image((width / 2) - 150, 0, image=gif1, anchor=NE)
    planeButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                         image=gif1, activebackground="#0b5394",
                         activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef")

    planeButton.pack()
    planeButton.place(x=(width / 2) - 150, y=0, anchor=NE)

    pil_run = PIL.Image.open("buttonM.gif")
    width_og, height_og = pil_run.size
    factor = 1
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_run1 = pil_run.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif2 = PIL.ImageTk.PhotoImage(pil_run1)
    # canvas.create_image((width / 2), 0, image=gif2, anchor=N)
    runButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                       image=gif2, activebackground="#0b5394",
                       activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef")

    runButton.pack()
    runButton.place(x=(width / 2), y=0, anchor=N)

    pil_film = PIL.Image.open("buttonR.gif")
    width_og, height_og = pil_film.size
    factor = 1
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_film1 = pil_film.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif3 = PIL.ImageTk.PhotoImage(pil_film1)
    # canvas.create_image((width / 2) + 150, 0, image=gif3, anchor=NW)
    filmButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                        image=gif3, activebackground="#0b5394",
                        activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef")

    filmButton.pack()
    filmButton.place(x=(width / 2) + 150, y=0, anchor=NW)
    window2.mainloop()
    return

def main():
    bgColor = "#4fa4ef"

    window = Tk()
    window.wm_attributes('-fullscreen', 'true')

    width = 800 #window.winfo_screenwidth()
    height = 480 #window.winfo_screenheight()
    window.geometry('%dx%d' % (width, height))

    # window['bg'] = bgColor

    canvas = Canvas(window, background="#4fa4ef")
    canvas.pack(fill=BOTH, expand=1)

    # Top Buttons (images)

    pil_plane = PIL.Image.open("buttonL.gif")
    width_og, height_og = pil_plane.size
    factor = .75
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_plane1 = pil_plane.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif1 = PIL.ImageTk.PhotoImage(pil_plane1)
    # canvas.create_image((width / 2) - 150, 0, image=gif1, anchor=NE)
    planeButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                         image=gif1, activebackground="#0b5394",
                         activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                         command=lambda:flight(width, height))

    planeButton.pack()
    planeButton.place(x=(width / 2) - 100, y=0, anchor=NE)

    pil_run = PIL.Image.open("buttonM.gif")
    width_og, height_og = pil_run.size
    factor = .75
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_run1 = pil_run.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif2 = PIL.ImageTk.PhotoImage(pil_run1)
    # canvas.create_image((width / 2), 0, image=gif2, anchor=N)
    runButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                       image=gif2, activebackground="#0b5394",
                       activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef")

    runButton.pack()
    runButton.place(x=(width / 2), y=0, anchor=N)

    pil_film = PIL.Image.open("buttonR.gif")
    width_og, height_og = pil_film.size
    factor = .75
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_film1 = pil_film.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    gif3 = PIL.ImageTk.PhotoImage(pil_film1)
    # canvas.create_image((width / 2) + 150, 0, image=gif3, anchor=NW)
    filmButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                        image=gif3, activebackground="#0b5394",
                        activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                        command=lambda:entertainment(width, height))

    filmButton.pack()
    filmButton.place(x=(width / 2) + 100, y=0, anchor=NW)

    # Bottom image

    #    gif4 = PhotoImage(file='bottom_rectangle.gif')
    pil_image4 = PIL.Image.open("bottom_rectangle.gif")
    width_og, height_og = pil_image4.size
    factor = .85
    heighti = int(height_og * factor)
    pil_image42 = pil_image4.resize((width, heighti), PIL.Image.ANTIALIAS)
    tk_image = PIL.ImageTk.PhotoImage(pil_image42)
    canvas.create_image((width / 2), height, image=tk_image, anchor=S)

    pil_image1 = PIL.Image.open("Rect1.gif")
    width_og, height_og = pil_image1.size
    factor = .25
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_image12 = pil_image1.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    rect1 = PIL.ImageTk.PhotoImage(pil_image12)
    canvas.create_image((width / 3), (height / 3), image=rect1, anchor=N)

    pil_image3 = PIL.Image.open("Rect3.gif")
    width_og, height_og = pil_image3.size
    factor = .25
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_image32 = pil_image3.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    rect3 = PIL.ImageTk.PhotoImage(pil_image32)
    canvas.create_image(((2 * width) / 3), (height / 3), image=rect3, anchor=N)

    # Pause Button

    pil_image2 = PIL.Image.open("Rect2.gif")
    width_og, height_og = pil_image2.size
    factor = .75
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_image22 = pil_image2.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    rect2 = PIL.ImageTk.PhotoImage(pil_image22)
    # canvas.create_image((width / 2), (height / 2), image=rect2, anchor=N)

    pauseButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                         image=rect2, activebackground="#0b5394",
                         activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                         command=setPause)

    # Play button

    pil_play = PIL.Image.open("play.gif")
    width_og, height_og = pil_play.size
    factor = .75
    widthi = int(width_og * factor)
    heighti = int(height_og * factor)
    pil_play2 = pil_play.resize((widthi, heighti), PIL.Image.ANTIALIAS)
    play = PIL.ImageTk.PhotoImage(pil_play2)
    startButton = Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=FLAT,
                         image=play, activebackground="#0b5394",
                         activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                         command=setStart)

    pauseButton.pack()
    pauseButton.place(x=(5 * width / 8), y=(5 * height / 8), anchor=N)

    startButton.pack()
    startButton.place(x=(3 * width / 8), y=(5 * height / 8), anchor=N)

    # Speed Button Labels

    labelL = Label(window, text="Low", background='#073763', font=("Helvetica, 25"), fg="#ffffff")
    labelL.pack()
    labelL.place(x=width / 8 + labelL.winfo_width(), y=(6.75 * height) / 8 + labelL.winfo_height())

    labelM = Label(window, text="Medium", background='#073763', font=("Helvetica, 25"), fg="#ffffff")
    labelM.pack()
    labelM.place(x=3 * width / 7 + labelM.winfo_width(), y=(6.75 * height) / 8 + labelM.winfo_height())

    labelH = Label(window, text="High", background='#073763', font=("Helvetica, 25"), fg="#ffffff")
    labelH.pack()
    labelH.place(x=(4 * width / 5 + labelH.winfo_width()), y=((6.75 * height) / 8 + labelH.winfo_height()))

    t1 = threading.Thread(target=time_count, args=(window, width, height))
    t1.start()
    # dis = Display()
    window.mainloop()


pause = True

def setPause():
    global pause
    pause = True

def setStart():
    global pause
    pause = False

#def checkPauseTime(pause):
#     while (pause == True):
#         time.sleep(1)

def time_count(window, width, height):
    sec = int(0)
    min = int(0)
    hrs = int(0)
    global pause

    while(1):
        if (pause):
            time.sleep(1)
            continue
        else:
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
            labelTime.place(x=(4.95 * width / 7 + labelTime.winfo_width()),
                            y=((3.15 * height) / 7 + labelTime.winfo_height()), anchor=CENTER)
            time.sleep(1)

def entertainment(width, height):
    top = Toplevel(bg="#4fa4ef", width=width, height=height)
    top.wm_attributes('-fullscreen', 'true')
    msg = Message(top, text="Entertainment page coming soon...", bg="#4fa4ef", font=("Helvetica, 20"),
                  width=800, justify="center",anchor="center")
    msg.pack()
    msg.place(x=(width / 2), y=(height / 2), anchor=CENTER)

    button = Button(top, text="Dismiss", command=top.destroy, font=("Helvetica, 20"),
                    anchor=CENTER)
    button.pack()
    button.place(x=(width / 2), y=(height / 2) + 75, anchor=CENTER)

def flight(width, height):
    top = Toplevel(bg="#4fa4ef", width=width, height=height)
    top.wm_attributes('-fullscreen', 'true')
    msg = Message(top, text="Flight Info page coming soon...", bg="#4fa4ef", font=("Helvetica, 20"),
                  width=800, justify="center", anchor=CENTER)
    msg.pack()
    msg.place(x=(width / 2), y=(height / 2), anchor=CENTER)

    button = Button(top, text="Dismiss", command=top.destroy, font=("Helvetica, 20"),
                    anchor=CENTER)
    button.pack()
    button.place(x=(width / 2), y=(height / 2)+ 75, anchor=CENTER)

#def speedbuttons():


if __name__ == '__main__':
    main()


