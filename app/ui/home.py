from typing import Tuple
import customtkinter as ctk
import tkinter
from ..src.opeancam import Cam

from ..globals import GLOBAL

ctk.set_appearance_mode("light")

# detail frames
class DetailFrame(ctk.CTkFrame):


    def __init__(self, master, **kwargs):
        detail=list()
        super().__init__(master, width=400,height=600, fg_color="transparent",border_color='#333',border_width=2,**kwargs)
        self.detail=detail
        # self.scroll=ctk.CTkScrollableFrame(self,width=400,height=800)
        # self.scroll.pack(expand=True,fill=tkinter.BOTH)
        self.l_name=ctk.CTkLabel(self,text='name:- ',fg_color='transparent',font=('times new roman',20),text_color='#333')
        self.l_class=ctk.CTkLabel(self,text='class:- ',fg_color='transparent',font=('times new roman',20),text_color='#333')
        self.l_section=ctk.CTkLabel(self,text='section:- ',fg_color='transparent',font=('times new roman',20),text_color='#333')
        self.l_id=ctk.CTkLabel(self,text='id:- ',fg_color='transparent',font=('times new roman',20),text_color='#333')

        self.detail.append(self.lord_details(self,'unkown'))
        self.detail.append(self.lord_details(self,'unkown'))
        self.detail.append(self.lord_details(self,'unkown'))
        self.detail.append(self.lord_details(self,'unkown'))

        # self.title=ctk.CTkLabel(self,text="Details will be display over here ",font=("times new roman",20),text_color="#333",fg_color="white",anchor="center")
        self.b_add=ctk.CTkButton(self,text="ADD",border_color="#333",border_width=2,fg_color="green",text_color="#333",font=("times new roman",12), command=self.onclick)
        self.b_report=ctk.CTkButton(self,text="REPORT",border_color="#333",border_width=2,fg_color="green",text_color="#333",font=("times new roman",12))
        self.grid_propagate(False)
        self.grid_columnconfigure((0,1,2,3),weight=1)
        self.grid_rowconfigure((0,1,2,3,4),weight=1)

    def lord_details(self,master,text):
        return ctk.CTkLabel(master,text=text,font=('times new roman',20),fg_color='transparent',text_color='#333')
        
    
    # on click
    def onclick(self):
        mainpanel=GLOBAL['mainpanel']
        mainpanel.setActiveFrame(mainpanel.registration)

    def show(self):
        self.l_name.grid(row=0,column=0,sticky='n',pady=10)
        self.l_class.grid(row=1,column=0,sticky='n',pady=10)
        self.l_section.grid(row=2,column=0,sticky='n',pady=10)
        self.l_id.grid(row=3,column=0,sticky='n',pady=10)

        for i,det in enumerate(self.detail):
            det.grid(row=i,column=1,sticky='n',padx=10,pady=10)


        self.b_add.grid(row=4,column=0,padx=10,pady=10,sticky='sw')
        self.b_report.grid(row=4,column=1,padx=10,pady=10,sticky='sw')

        self.grid(row=1,column=1,padx=(0,50),pady=10)
    
    def hide(self):
        self.grid_forget()
        
# live camera frame 
class LiveCamera(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, width=500, height=500,corner_radius=2,border_color="#333",fg_color="transparent",border_width=2, **kwargs)
        self.cam=Cam(self)
        self.title=ctk.CTkLabel(self,text="live camera",font=("times new roman",20),fg_color="white",text_color='#333')
        self.b_start=ctk.CTkButton(self,text="START CAMERA",font=('times new roman',12),border_color="white",border_width=2,fg_color='green',text_color="#333",command=self.cam.toggle_camera)
        GLOBAL['livecam']=self
        self.grid_propagate(False)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
    def show(self):
        self.title.grid(row=0,column=0,sticky='nsew')
        self.b_start.grid(row=1,column=0,padx=100,pady=10)


        self.grid(row=1,column=0,padx=(50,0),pady=10)

# home frame.
class Home(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, border_color='#333',border_width=2,**kwargs)
        self.l_title=ctk.CTkLabel(self,text="HOME",font=('Lucida Handwriting',15),fg_color="white",text_color="#2C5F61",anchor='n')
        self.grid_columnconfigure(0,weight=1)
        # self.rowconfigure(0,weight=1)

        self.livecamera=LiveCamera(self)
        self.detailframe=DetailFrame(self)
    def show(self):
        # attaching into the home frame
        self.l_title.grid(row=0,column=0,sticky='nsew',padx=20,pady=20,columnspan=2)
        self.livecamera.show()
        self.detailframe.show()

        self.pack(expand=True,fill=tkinter.BOTH,padx=10,pady=10)

        
    def hide(self):
        self.pack_forget()

if __name__=="__main__":
    app=ctk.CTk()
    home=Home(master=app)
    home.show()
    app.mainloop()