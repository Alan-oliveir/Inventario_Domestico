'''from tkinter import*
from tkinter import Tk, StringVar, ttk

from tkcalendar import Calendar

import tkinter.font as tkFont

from tkinter import messagebox
from tkinter import filedialog as fd

import customtkinter as ctk

from PIL import Image, ImageTk

import os

PATH = os.path.dirname(os.path.realpath(__file__)) 

# =========== Window of date pick  ==============
def create_toplevel_date(campo_data):
        
        global date_window

        date_window = ctk.CTkToplevel()
        date_window.geometry("325x365")
        date_window.title("Selecionar Data")
        date_window.resizable(width = "false", height= "false")

        global cal

        frame_calendar = ctk.CTkFrame(master=date_window)
        frame_calendar.pack(padx=15, pady=15)

        # create label on CTkToplevel window
        label = ctk.CTkLabel(frame_calendar, text="Selecionar Data")
        label.pack(side="top", fill="both", padx=20, pady=5)
        
        cal = Calendar(frame_calendar, selectmode='day')
        cal.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        button_ok = ctk.CTkButton(frame_calendar, width=80, text="OK", command=lambda: update_date(campo_data))
        button_ok.pack(side="left", fill="both", expand=True, pady=20, padx=20)

        button_cancel = ctk.CTkButton(frame_calendar, width=80, text="Cancelar", fg_color="white", command=date_window.destroy)
        button_cancel.pack(side="right", fill="both", expand=True, pady=20, padx=20)

    # ================= Update Date Time ============
def update_date( campo_data):

        new_date = cal.get_date()

        if campo_data == "compra":        
            frame_form.e_data_compra.configure(state="normal")
            frame_form.e_data_compra.delete(0, 11)
            frame_form.e_data_compra.insert(0, new_date)
            frame_form.e_data_compra.configure(state="disabled")     
            
        date_window.destroy()'''