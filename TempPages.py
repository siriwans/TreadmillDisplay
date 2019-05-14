import tkinter as tk
import time
import threading
import PIL.Image
import PIL.ImageTk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Flight(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Flight Coming Soon!")
       label.pack(side="top", fill="both", expand=True)

class Entertainment(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="Entertainment Coming Soon!")
       label.pack(side="top", fill="both", expand=True)

class Window(Page):
   def __init__(self, flight, ent, *args, **kwargs):
       width = 800
       height = 480
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="MAIN INIT WINDOW")
       label.pack(side="top", fill="both", expand=True)
       bgColor = "#4fa4ef"

       canvas = tk.Canvas(window, background="#4fa4ef")
       canvas.pack(fill=tk.BOTH, expand=1)

       # Top Buttons (images)

       pil_plane = PIL.Image.open("buttonL.gif")
       width_og, height_og = pil_plane.size
       factor = .5
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_plane1 = pil_plane.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       gif1 = PIL.ImageTk.PhotoImage(pil_plane1)
       # canvas.create_image((width / 2) - 150, 0, image=gif1, anchor=NE)
       planeButton = tk.Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=tk.FLAT,
                            image=gif1, activebackground="#0b5394",
                            activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                            command=flight.lift)

       planeButton.pack()
       planeButton.place(x=(width / 2) - 75, y=0, anchor=tk.NE)

       pil_run = PIL.Image.open("buttonM.gif")
       width_og, height_og = pil_run.size
       factor = .5
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_run1 = pil_run.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       gif2 = PIL.ImageTk.PhotoImage(pil_run1)
       # canvas.create_image((width / 2), 0, image=gif2, anchor=N)
       runButton = tk.Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=tk.FLAT,
                          image=gif2, activebackground="#0b5394",
                          activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                          command=window.lift)

       runButton.pack()
       runButton.place(x=(width / 2), y=0, anchor=tk.N)

       pil_film = PIL.Image.open("buttonR.gif")
       width_og, height_og = pil_film.size
       factor = .5
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_film1 = pil_film.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       gif3 = PIL.ImageTk.PhotoImage(pil_film1)
       # canvas.create_image((width / 2) + 150, 0, image=gif3, anchor=NW)
       filmButton = tk.Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=tk.FLAT,
                           image=gif3, activebackground="#0b5394",
                           activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                           command=ent.lift)

       filmButton.pack()
       filmButton.place(x=(width / 2) + 75, y=0, anchor=tk.NW)

       # Bottom image

       pil_image4 = PIL.Image.open("bottom_rectangle.gif")
       width_og, height_og = pil_image4.size
       factor = 1
       heighti = int(height_og * factor)
       pil_image42 = pil_image4.resize((width, heighti), PIL.Image.ANTIALIAS)
       tk_image = PIL.ImageTk.PhotoImage(pil_image42)
       canvas.create_image((width / 2), height, image=tk_image, anchor=tk.S)

       pil_image1 = PIL.Image.open("Rect1.gif")
       width_og, height_og = pil_image1.size
       factor = .2
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_image12 = pil_image1.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       rect1 = PIL.ImageTk.PhotoImage(pil_image12)
       canvas.create_image((width / 3), (height / 4), image=rect1, anchor=tk.N)

       pil_image3 = PIL.Image.open("Rect3.gif")
       width_og, height_og = pil_image3.size
       factor = .2
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_image32 = pil_image3.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       rect3 = PIL.ImageTk.PhotoImage(pil_image32)
       canvas.create_image(((2 * width) / 3), (height / 4), image=rect3, anchor=tk.N)

       # Pause Button

       pil_image2 = PIL.Image.open("Rect2.gif")
       width_og, height_og = pil_image2.size
       factor = .6
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_image22 = pil_image2.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       rect2 = PIL.ImageTk.PhotoImage(pil_image22)
       # canvas.create_image((width / 2), (height / 2), image=rect2, anchor=N)

       pauseButton = tk.Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=tk.FLAT,
                            image=rect2, activebackground="#0b5394",
                            activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                            command=setPause)

       # Play button

       pil_play = PIL.Image.open("play.gif")
       width_og, height_og = pil_play.size
       factor = .6
       widthi = int(width_og * factor)
       heighti = int(height_og * factor)
       pil_play2 = pil_play.resize((widthi, heighti), PIL.Image.ANTIALIAS)
       play = PIL.ImageTk.PhotoImage(pil_play2)
       startButton = tk.Button(width=widthi, height=heighti, bd=0, highlightthickness=0, bg="#0b5394", relief=tk.FLAT,
                            image=play, activebackground="#0b5394",
                            activeforeground="#0b5394", highlightcolor="#4fa4ef", highlightbackground="#4fa4ef",
                            command=setStart)

       pauseButton.pack()
       pauseButton.place(x=(2 * width / 3), y=(height / 2), anchor=tk.NE)

       startButton.pack()
       startButton.place(x=(width / 3), y=(height / 2))

       # Speed Button Labels

       labelL = tk.Label(window, text="Low", background='#073763', font=("Helvetica, 30"), fg="#ffffff")
       labelL.pack()
       labelL.place(x=width / 8 + labelL.winfo_width(), y=(6 * height) / 7 + labelL.winfo_height())

       labelM = tk.Label(window, text="Medium", background='#073763', font=("Helvetica, 30"), fg="#ffffff")
       labelM.pack()
       labelM.place(x=3 * width / 7 + labelM.winfo_width(), y=(6 * height) / 7 + labelM.winfo_height())

       labelH = tk.Label(window, text="High", background='#073763', font=("Helvetica, 30"), fg="#ffffff")
       labelH.pack()
       labelH.place(x=(4 * width / 5 + labelH.winfo_width()), y=((6 * height) / 7 + labelH.winfo_height()))

       t1 = threading.Thread(target=time_count, args=(window, width, height))
       t1.start()
       # dis = Display()
       #window.mainloop()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        flight = Flight(self)
        ent = Entertainment(self)
        window = Window(flight, ent, self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        flight.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ent.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="FLIGHT", command=flight.lift)
        b2 = tk.Button(buttonframe, text="ENTERTAINMENT", command=ent.lift)
        b3 = tk.Button(buttonframe, text="MAIN", command=window.lift)

        b1.pack()
        b2.pack()
        b3.pack()

        window.show()

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
    global pause;

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
            labelTime = tk.Label(window, text=timeStr, background="#0b5394", font=("Helvetica, 20"), fg="#ffffff")
            labelTime.pack()
            labelTime.place(x=(3.9 * width / 6 + labelTime.winfo_width()),
                            y=((2.7 * height) / 7 + labelTime.winfo_height()))
            time.sleep(1)

if __name__ == "__main__":
    window = tk.Tk()
#    width = window.winfo_screenwidth()
#    height = window.winfo_screenheight()
#    window.wm_attributes('-fullscreen', 'true')

#    main.wm_attributes('-fullscreen', 'true')
    window.wm_geometry("800x480")
    main = MainView(window)
    main.pack(side="top", fill="both", expand=True)
    window.mainloop()