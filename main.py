from tkinter import*
from tkinter import Tk, StringVar, ttk

from tkcalendar import Calendar

import tkinter.font as tkFont

from tkinter import messagebox
from tkinter import filedialog as fd

import customtkinter as ctk

from PIL import Image, ImageTk

import os

PATH = os.path.dirname(os.path.realpath(__file__))

# ==================== Frames =========================

class frame_title_bar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Open image:
        app_img = ctk.CTkImage(Image.open(PATH + "/images/cadastre-se.png"), size=(45, 45))

        # Font object:
        font_title = ctk.CTkFont(family="Verdana", size=20, weight="bold")

        # Add widgets onto the frame_title_bar
        label_img = ctk.CTkLabel(self, text="", image=app_img)
        label_img.grid(row=0, column=0, padx=5, pady=5, stick="ne")

        label_title = ctk.CTkLabel(self, text="Inventário Doméstico", font=font_title)
        label_title.grid(row=0, column=1, padx=0, pady=0, stick="e")

class frame_form(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        # Font object:
        font_form = ctk.CTkFont(family="Segoe UI", size=13, weight="normal")

        # Add widgets onto the frame_form
        l_nome = ctk.CTkLabel(self, text="Nome",font=font_form)
        l_nome.grid(row=0, column=0, pady=(10,5), stick="new")
        e_nome = ctk.CTkEntry(self, width=225)
        e_nome.grid(row=0, column=1, padx=10, pady=(10,5), stick="new")

        l_local = ctk.CTkLabel(self, text="Sala/Área", font=font_form)
        l_local.grid(row=1, column=0)
        e_local = ctk.CTkEntry(self, width=225)
        e_local.grid(row=1, column=1, padx=10, pady=5, stick="new")

        l_descricao = ctk.CTkLabel(self, text="Descrição",font=font_form)
        l_descricao.grid(row=2, column=0)
        e_descricao = ctk.CTkEntry(self, width=225)
        e_descricao.grid(row=2, column=1, padx=10, pady=5, stick="new")

        l_model = ctk.CTkLabel(self, text="Marca/Modelo", font=font_form)
        l_model.grid(row=3, column=0)
        e_model = ctk.CTkEntry(self, width=225)
        e_model.grid(row=3, column=1, padx=10, pady=5, stick="new") 

        l_valor = ctk.CTkLabel(self, text="Valor da compra", font=font_form)
        l_valor.grid(row=4, column=0)
        e_valor = ctk.CTkEntry(self, width=225)
        e_valor.grid(row=4, column=1, padx=10, pady=5, stick="ne")

        l_serial = ctk.CTkLabel(self, text="Número de série", font=font_form)
        l_serial.grid(row=5, column=0)
        e_serial = ctk.CTkEntry(self, width=225)
        e_serial.grid(row=5, column=1, padx=10, pady=5, stick="sew")

        l_cal = ctk.CTkLabel(self, text="Data da compra", font=font_form)
        l_cal.grid(row=6, column=0)
        self.e_data_compra = ctk.CTkEntry(self, width=85)
        self.e_data_compra.grid(row=6, column=1, padx=10, stick="w")        
        button_date = ctk.CTkButton(self, width=120, text="Selecionar Data", command=lambda: self.create_toplevel_date("compra"))
        button_date.grid(row=6, column=1, padx=10, pady=5, stick="e")

        l_view = ctk.CTkLabel(self, text="Imagem do item", font=font_form, width=120)
        l_view.grid(row=7, column=0)
        button_view = ctk.CTkButton(self, width=224, text="Carregar Imagem", command=lambda: self.create_toplevel_date("compra"))
        button_view.grid(row=7, column=1, padx=10, pady=(5,10), stick="sew")

    # =========== Window of date pick  ==============
    def create_toplevel_date(self, campo_data):
        
        global date_window

        date_window = ctk.CTkToplevel(self)
        date_window.geometry("325x365")
        date_window.title("Selecionar Data")
        date_window.resizable(width = "false", height= "false")

        global cal

        self.frame_calendar = ctk.CTkFrame(master=date_window)
        self.frame_calendar.pack(padx=15, pady=15)

        # create label on CTkToplevel window
        label = ctk.CTkLabel(self.frame_calendar, text="Selecionar Data")
        label.pack(side="top", fill="both", padx=20, pady=5)
        
        cal = Calendar(self.frame_calendar, selectmode='day')
        cal.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        button_ok = ctk.CTkButton(self.frame_calendar, width=80, text="OK", command=lambda: self.update_date(campo_data))
        button_ok.pack(side="left", fill="both", expand=True, pady=20, padx=20)

        button_cancel = ctk.CTkButton(self.frame_calendar, width=80, text="Cancelar", fg_color="white", command=date_window.destroy)
        button_cancel.pack(side="right", fill="both", expand=True, pady=20, padx=20)

    # ================= Update Date Time ============
    def update_date(self, campo_data):

        new_date = cal.get_date()

        if campo_data == "compra":        
            self.e_data_compra.configure(state="normal")
            self.e_data_compra.delete(0, 11)
            self.e_data_compra.insert(0, new_date)
            self.e_data_compra.configure(state="disabled")     
            
        date_window.destroy()  

class frame_button(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Create 6x1 grid system
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        self.columnconfigure(0, weight=1)

        self.button_add = ctk.CTkButton(self, width=150, text="Adicionar", command=lambda: self.create_toplevel_date("compra"))        
        self.button_add.grid(row=0, column=0, padx=5, pady=5)
        
        self.button_update = ctk.CTkButton(self, width=150, text="Atualizar", command=lambda: self.create_toplevel_date("compra"))
        self.button_update.grid(row=1, column=0, padx=5, pady=5)

        self.button_delete = ctk.CTkButton(self, width=150, text="Delete", command=lambda: self.create_toplevel_date("compra"))
        self.button_delete.grid(row=2, column=0, padx=5, pady=5)

        self.button_confirm = ctk.CTkButton(self, width=150, text="Confirmar", command=lambda: self.create_toplevel_date("compra"))
        self.button_confirm.grid(row=5, column=0, padx=5, pady=5)

        self.button_view = ctk.CTkButton(self, width=150, text="Ver Item", command=lambda: self.create_toplevel_date("compra"))
        self.button_view.grid(row=6, column=0, padx=5, pady=5)

'''class FrameTableInfo(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)'''

class App(ctk.CTk):

    # Geometry constants:
    width = 900
    height = 600
    
    def __init__(self):
        super().__init__()        
        #self.geometry(f"{self.width}x{self.height}")
        #self.resizable(False, False)
        self.title("")

        # Create 3x3 grid system
        self.grid_columnconfigure((0,1,2), weight=0)

        self.frame_title_bar = frame_title_bar(master=self)
        self.frame_title_bar.grid(row=0, column=0, columnspan=3, stick="new")

        self.frame_form = frame_form(master=self)
        self.frame_form.grid(row=1, column=0, pady=2, padx=1, stick="nw")

        self.frame_button = frame_button(master=self)
        self.frame_button.grid(row=1, column=1, pady=2, padx=1, stick="nw")

app = App()
app.mainloop()

