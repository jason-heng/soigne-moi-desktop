from customtkinter import *
from utils.ui import Colors, font_title
from utils.logic import *

class Dashboard(CTkFrame):
    def __init__(self, master: CTkFrame):
        super().__init__(master, corner_radius = 0, fg_color = Colors.WHITE)

        self.master  =  master
        self.window  =  master.window

        self.view()

    def view(self):
        pass