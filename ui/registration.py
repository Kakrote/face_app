from typing import Tuple
import customtkinter as ctk
import tkinter
from CustomPopUp import PopUp

# this is the admincam
class AdminCam(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master,width=500,height=500,border_color='#333',border_width=2,**kwargs)
        self.tite=ctk.CTkLabel(self,text='the admin cam will opena here ',fg_color='white',text_color='#333',font=('times new roman',15))
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
    def show(self):
        self.tite.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.grid_propagate(False)

        self.grid(row=1,column=0,padx=(50,0),pady=10)

# this is the usercam

class UserCam(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,width=500,height=500,border_color='#333',border_width=2,**kwargs)
        self.title=ctk.CTkLabel(self,text="the user cam will be open here",fg_color='white',text_color='#333',font=('times new roman',15))
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
    def show(self):
        self.title.grid(row=0,column=0,padx=10,pady=10,sticky='nsew')
        self.grid_propagate(False)

        self.grid(row=1,column=1,padx=(0,50),pady=10)

# footer frame
class Footer(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,border_color='#333',border_width=2,**kwargs)
        self.pop=PopUp(self,message="do you wnat to add a adimin or the user",buttons=['Admin','User'])
        self.b_capture=ctk.CTkButton(self,text='capture',fg_color='green',font=('times new roman',10))
        self.b_try_again=ctk.CTkButton(self,text='try again',fg_color='green',font=('times new roman',10))
        self.b_next=ctk.CTkButton(self,text='next',fg_color='green',font=('times new roman',10),command=self.pop.show)

        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure((0,1,2),weight=1)

    def show(self):
        self.b_capture.grid(row=0,column=0,padx=20,pady=10)
        self.b_try_again.grid(row=0,column=1,padx=20,pady=10)
        self.b_next.grid(row=0,column=2,padx=20,pady=10)

        # self.pack(expand=True,fill=tkinter.X,padx=20,pady=20)
        self.grid(row=2,column=1,sticky='ne',padx=(50,50),pady=0)


# this is the Registation frame

class Registration(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master,border_color='#333',border_width=2,**kwargs)
        self.l_title=ctk.CTkLabel(self,text="Resgistration",fg_color='white',text_color='#333',font=("Lucida Handwriting",15))
        self.admincam=AdminCam(self)
        self.usercam=UserCam(self)
        self.footer=Footer(self)
        self.grid_columnconfigure(0,weight=1)
        # self.grid_rowconfigure(2,weight=1)
        # self.grid_columnconfigure(0,weight=1)
    def show(self):
        self.l_title.grid(row=0,column=0,columnspan=3,sticky='nsew',padx=10,pady=10)
        self.admincam.show()
        self.usercam.show()
        self.footer.show()

        self.grid(row=0,column=0,sticky='nsew',padx=10,pady=10)

if __name__=="__main__":
    app=ctk.CTk()
    reigs=Registration(master=app)
    reigs.show()
    app.mainloop()

