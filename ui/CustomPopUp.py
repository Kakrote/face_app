import customtkinter as ctk
import tkinter
# from ui.CustomPopUp import PopUp
# this is the custom pop up

class PopUp(ctk.CTkFrame):
    def __init__(self,master,message="",buttons= [],**kwargs):
        super().__init__(master,**kwargs)
        self.title=ctk.CTkLabel(self,text='coes')

        self.message=ctk.CTkLabel(self,text=message,font=("times new roman",10),text_color='#333')

        # buttons 
        self.button_frame=ctk.CTkFrame(self)
        for buttons_text in buttons:
            button = ctk.CTkButton(self.button_frame, text=buttons_text, command=self.close)  # Default close action on button click
            button.grid( padx=5)

        self.close_func=None
    

    def set_close_function(self, func):
        self.close_func = func

    def close(self):
        if self.close_func:
            self.close_func()
        self.destroy()

    def show(self):
        self.title.grid()
        self.message.grid(padx=10,pady=10)
        # self.bu=self.button_frame(self)
        self.button_frame.grid()
        # self.bu.grid()
        # self.pack(fill=ctk.BOTH, expand=True)
        self.grid()