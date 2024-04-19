from typing import Tuple
import customtkinter as ctk
import tkinter
from frames.home import Home

ctk.set_appearance_mode("dark")

# this is the mainpanel where the all the windows will open

class MainPanel(ctk.CTkFrame):
    home=None
    def setActiveFrame(self,frame):
        app.mainpanel.activeframe.grid_forget()
        app.mainpanel.activeframe=frame
        app.mainpanel.activeframe.show()
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.home=Home(self)

        self.activeFrame=self.home
    def show(self):
        self.activeFrame.show()
        self.pack(fill=tkinter.BOTH,expand=True,padx=20,pady=20)

# this will opean the window and will lord the mainpanel in it
class Clint_Win(ctk.CTk):
    hight,width=400,800
    def __init__(self, fg_color: str | Tuple[str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        self.geometry(f'{self.width}x{self.hight}')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
        self.mainpanel=MainPanel(self)
    def show(self):
        self.mainpanel.show()
        self.mainloop()
app=None
if __name__=="__main__":
    app=Clint_Win()
    app.show()
