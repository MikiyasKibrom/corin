from tkinter import *
class function:
    def __init__(self, r, photo):
        self.canvas= Canvas(r, width= 600, height= 500)
        self.canvas.create_image(0, 0, image= photo, anchor= 'nw')
        self.canvas.pack(fill= 'both', expand= True)
    def destroy(self, *args):
        self.canvas.destroy()