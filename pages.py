from tkinter import *
import PIL.Image
import PIL.ImageTk

class Page(Frame):
    def __init__(self, *args, **kwargs):
        self.width = 0
        self.height = 0
        Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Flight(Page):
    def __init__(self, *args, **kwargs):
        self.width = 0
        self.height = 0
        Page.__init__(self, *args, **kwargs)
        frame = Frame(self, width=self.width, height=self.height, bg="#4fa4ef")
        frame.pack()
        label = Label(self, text="Coming soon")
        label.pack(side="top", fill="both", expand=True)


class MainPage(Frame):
    def __init__(self, *args, **kwargs):
        self.width = 0
        self.height = 0
        Frame.__init__(self, *args, **kwargs)
        flight = Flight(self)
        flight.width = self.width
        flight.height = self.height

        frame = Frame(self, width=self.width, height=self.height, bg="#4fa4ef")
        frame.pack()
        flight.place(in_=frame, x=0, y=0, relwidth=1, relheight=1)

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
        planeButton.place(x=(self.width / 2) - 150, y=0, anchor=NE)

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
        runButton.place(x=(self.width / 2), y=0, anchor=N)

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
        filmButton.place(x=(self.width / 2) + 150, y=0, anchor=NW)


if __name__ == "__main__":
    window = Tk()
    main = MainPage(window)
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    main.width = width
    main.height = height
    window.wm_attributes('-fullscreen', 'true')
    window.mainloop()