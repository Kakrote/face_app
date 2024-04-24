from typing import Tuple
import customtkinter as ctk
import tkinter


from .globals import GLOBAL
from .ui.home import Home
from .ui.registration import Registration
# from ui.CustomPopUp import PopUp

class MainPanel(ctk.CTkFrame):
    activepanel=None
    def setActiveFrame(self,frame):
        self.activeframe.hide()
        self.activeframe=frame
        self.activeframe.show()

    def __init__(self, master, **kwargs):
        super().__init__(master,border_color='#333',border_width=2, **kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.home=Home(self)
        self.registration=Registration(self)

        GLOBAL['mainpanel']=self

        self.activeframe=self.home
        # self.activeframe=self.registration



    def show(self):
        self.activeframe.show()
        self.pack(fill=tkinter.BOTH,expand=True,padx=20,pady=20)

class FaceApp(ctk.CTk):
    height,width=400,800
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry(f'{self.width}x{self.height}')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.mainpanel=MainPanel(self)
        self.after(10, lambda:self.state("zoomed"))


    def show(self):
        self.mainpanel.show()
        self.mainloop()
App=None

def main():
    App=FaceApp()
    App.show()