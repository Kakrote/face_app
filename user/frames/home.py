from typing import Any, Tuple
import customtkinter as ctk
import tkinter

class Home(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master,fg_color='blue',**kwargs)
        self.l_title=ctk.CTkLabel(self,text="Face App",font=('times new roman',12),text_color='#333',fg_color='red')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)
    def show(self):
        self.l_title.grid(row=0, column=0, sticky='n', padx=20, pady=20)
        self.l_title.configure(height=20,width=100)

        # self.pack(fill=tkinter.BOTH,expand=True,padx=20,pady=20)
        self.pack(expand=True,fill=tkinter.BOTH,padx=20,pady=20)
# if __name__=="__main__":
#     app=ctk.CTk()
#     home=Home(master=app)
#     home.show()
#     app.mainloop()