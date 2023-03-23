from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from tkcalendar import Calendar

import customtkinter as ctk

from PIL import Image

import os

from crud import * 

# Constants
PATH = os.path.dirname(os.path.realpath(__file__))

# ==================== Functions ======================

def selecionar_imagem():

    global image_path

    image_path = fd.askopenfilename()
    image = ctk.CTkImage(Image.open(image_path), size=(275,275))
    FrameImage.l_image.configure(image=image)

# Inserir
def inserir():
         
    global image_path, table

    nome = FrameForm.e_nome.get()
    local = FrameForm.e_local.get()
    descricao = FrameForm.e_descricao.get()
    model = FrameForm.e_model.get()
    data = FrameForm.e_data_compra.get()
    valor = FrameForm.e_valor.get()
    serie = FrameForm.e_serial.get()
    imagem = image_path

    lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

    for i in lista_inserir:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    FrameForm.e_nome.delete(0, 'end')
    FrameForm.e_local.delete(0, 'end')
    FrameForm.e_descricao.delete(0, 'end')
    FrameForm.e_model.delete(0, 'end')
    FrameForm.e_data_compra.delete(0, 'end')
    FrameForm.e_valor.delete(0, 'end')
    FrameForm.e_serial.delete(0, 'end')

    for item in table.get_children():
        table.delete(item)

    lista_itens = ver_form()
    for item in lista_itens:
        table.insert('', 'end', values=item)

    quantidade = []

    for item in lista_itens:
        quantidade.append(item[6])

    FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
    FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

# funcao atualizar
def atualizar():
    
    global table_view_list

    try:
        table_view_data = table.focus()
        table_view_dic = table.item(table_view_data)
        table_view_list = table_view_dic['values']

        # Delete previus values
        FrameForm.e_nome.delete(0, 'end')
        FrameForm.e_local.delete(0, 'end')
        FrameForm.e_descricao.delete(0, 'end')
        FrameForm.e_model.delete(0, 'end')
        FrameForm.e_data_compra.delete(0, 'end')
        FrameForm.e_valor.delete(0, 'end')
        FrameForm.e_serial.delete(0, 'end')

        # Get values of item selected
        FrameForm.e_nome.insert(0, table_view_list[1])
        FrameForm.e_local.insert(0, table_view_list[2])
        FrameForm.e_descricao.insert(0, table_view_list[3])
        FrameForm.e_model.insert(0, table_view_list[4])
        FrameForm.e_data_compra.insert(0, table_view_list[5])
        FrameForm.e_valor.insert(0, table_view_list[6])
        FrameForm.e_serial.insert(0, table_view_list[7])      

        # Update state of button_confirm 
        FrameButton.button_confirm.configure(state="normal")        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def update():

    global table_view_list, table

    id = int(table_view_list[0])
    nome = FrameForm.e_nome.get()
    local = FrameForm.e_local.get()
    descricao = FrameForm.e_descricao.get()
    model = FrameForm.e_model.get()
    data = FrameForm.e_data_compra.get()
    valor = FrameForm.e_valor.get()
    serie = FrameForm.e_serial.get()           
    imagem = table_view_list[8]

    if imagem == '':
        imagem = FrameForm.e_serial.insert(0, table_view_list[7])

    lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]
    
    for i in lista_atualizar:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    atualizar_form(lista_atualizar)

    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

    FrameForm.e_nome.delete(0, 'end')
    FrameForm.e_local.delete(0, 'end')
    FrameForm.e_descricao.delete(0, 'end')
    FrameForm.e_model.delete(0, 'end')
    FrameForm.e_data_compra.delete(0, 'end')
    FrameForm.e_valor.delete(0, 'end')
    FrameForm.e_serial.delete(0, 'end')

    for item in table.get_children():
        table.delete(item)

    lista_itens = ver_form()
    for item in lista_itens:
        table.insert('', 'end', values=item)

    quantidade = []

    for item in lista_itens:
        quantidade.append(item[6])

    FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
    FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

# funcao deletar
def deletar():

    global table

    try:
        table_view_data = table.focus()
        table_view_dic = table.item(table_view_data)
        table_view_list = table_view_dic['values']

        id = table_view_list[0]

        deletar_form([id])

        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        for item in table.get_children():
            table.delete(item)

        lista_itens = ver_form()
        for item in lista_itens:
            table.insert('', 'end', values=item)

        quantidade = []

        for item in lista_itens:
            quantidade.append(item[6])

        FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
        FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

# Função para abrir imagem
def visualizar_imagem():

    table_view_data = table.focus()
    table_view_dic = table.item(table_view_data)
    table_view_list = table_view_dic['values']

    id = [int(table_view_list[0])]
    item = ver_item(id)
    image_path = item[0][8]
    image = ctk.CTkImage(Image.open(image_path), size=(275,275))
    FrameImage.l_image.configure(image=image)


# ==================== Frames =========================

class FrameTitleBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Open image:
        app_img = ctk.CTkImage(Image.open(PATH + "/images/cadastre-se.png"), size=(45, 45))

        # Font object:
        font_title = ctk.CTkFont(family="Verdana", size=20, weight="bold")

        # Add widgets onto the FrameTitleBar
        label_img = ctk.CTkLabel(self, text="", image=app_img)
        label_img.grid(row=0, column=0, padx=5, pady=5, stick="ne")

        label_title = ctk.CTkLabel(self, text="Inventário Doméstico", font=font_title)
        label_title.grid(row=0, column=1, padx=0, pady=0, stick="e")


class FrameForm(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.columnconfigure((0, 1), weight=1)

        # Font object:
        font_form = ctk.CTkFont(size=13, weight="normal")

        # Add widgets onto the FrameForm
        l_nome = ctk.CTkLabel(self, text="Nome:",font=font_form)
        l_nome.grid(row=0, column=0, pady=(10,5), stick="new")
        FrameForm.e_nome = ctk.CTkEntry(self, width=225)
        FrameForm.e_nome.grid(row=0, column=1, padx=10, pady=(10,5), stick="new")

        l_local = ctk.CTkLabel(self, text="Área:", font=font_form)
        l_local.grid(row=1, column=0)
        FrameForm.e_local = ctk.CTkEntry(self, width=225)
        FrameForm.e_local.grid(row=1, column=1, padx=10, pady=5, stick="new")

        l_descricao = ctk.CTkLabel(self, text="Descrição:",font=font_form)
        l_descricao.grid(row=2, column=0)
        FrameForm.e_descricao = ctk.CTkEntry(self, width=225)
        FrameForm.e_descricao.grid(row=2, column=1, padx=10, pady=5, stick="new")

        l_model = ctk.CTkLabel(self, text="Marca ou modelo:", font=font_form)
        l_model.grid(row=3, column=0)
        FrameForm.e_model = ctk.CTkEntry(self, width=225)
        FrameForm.e_model.grid(row=3, column=1, padx=10, pady=5, stick="new") 

        l_valor = ctk.CTkLabel(self, text="Valor da compra:", font=font_form)
        l_valor.grid(row=4, column=0)
        FrameForm.e_valor = ctk.CTkEntry(self, width=225)
        FrameForm.e_valor.grid(row=4, column=1, padx=10, pady=5, stick="ne")

        l_serial = ctk.CTkLabel(self, text="Número de série:", font=font_form)
        l_serial.grid(row=5, column=0)
        FrameForm.e_serial = ctk.CTkEntry(self, width=225)
        FrameForm.e_serial.grid(row=5, column=1, padx=10, pady=5, stick="sew")

        l_cal = ctk.CTkLabel(self, text="Data da compra:", font=font_form)
        l_cal.grid(row=6, column=0)
        FrameForm.e_data_compra = ctk.CTkEntry(self, width=85)
        FrameForm.e_data_compra.grid(row=6, column=1, padx=10, stick="w")        
        button_date = ctk.CTkButton(self, width=120, text="Selecionar Data", command=lambda: self.create_toplevel_date("compra"))
        button_date.grid(row=6, column=1, padx=10, pady=5, stick="e")

        l_view = ctk.CTkLabel(self, text="Imagem do item:", font=font_form, width=120)
        l_view.grid(row=7, column=0)
        button_view = ctk.CTkButton(self, width=224, text="Carregar Imagem", command=selecionar_imagem)
        button_view.grid(row=7, column=1, padx=10, pady=(5,10), stick="sew")

    # =========== Window of date pick  ==============
    def create_toplevel_date(self, campo_data):
        
        global date_window, cal

        date_window = ctk.CTkToplevel(self)
        date_window.geometry("325x365")
        date_window.title("Selecionar Data")
        date_window.resizable(width = "false", height= "false")

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
            self.e_data_compra.delete(0, 'end')
            self.e_data_compra.insert(0, new_date)
            self.e_data_compra.configure(state="disabled")     
            
        date_window.destroy()


class FrameButton(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Open image:
        add_img = ctk.CTkImage(Image.open(PATH + "/images/add.png"), size=(30,30))
        update_img = ctk.CTkImage(Image.open(PATH + "/images/refresh.png"), size=(30,30))
        clear_img = ctk.CTkImage(Image.open(PATH + "/images/folder.png"), size=(30,30))
        view_img = ctk.CTkImage(Image.open(PATH + "/images/management.png"), size=(30,30))
       
        # Create 6x1 grid system
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.columnconfigure(0, weight=1)
        
        # Add widgets onto the FrameButton
        button_add = ctk.CTkButton(self, width=175, text="Adicionar", image=add_img, compound="left", command=inserir)        
        button_add.grid(row=0, column=0, padx=5, pady=5)
        
        button_update = ctk.CTkButton(self, width=175, text="Atualizar", image=update_img, compound="left", command=atualizar)
        button_update.grid(row=1, column=0, padx=5, pady=5)

        button_delete = ctk.CTkButton(self, width=175, text="Delete",image=clear_img, compound="left", command=deletar) 
        button_delete.grid(row=2, column=0, padx=5, pady=5)
        
        FrameButton.button_confirm = ctk.CTkButton(self, width=175, text="Confirmar", state="disabled", command=update)
        FrameButton.button_confirm.grid(row=5, column=0, padx=5, pady=5, stick="s")

        button_view = ctk.CTkButton(self, width=175, text="Ver Item", image=view_img, compound="left", command=visualizar_imagem)
        button_view.grid(row=6, column=0, padx=5, pady=5, stick="s")


class FrameText(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)   

        # Font object
        font_label = ctk.CTkFont(size=15, weight="bold")
        font_text_box = ctk.CTkFont(size=20, weight="bold")

        # Add widgets onto the FrameText
        l_value_total = ctk.CTkLabel(self, text="Valor total dos itens", font=font_label)
        l_value_total.grid(row=0, column=0, padx=10, pady=10)

        FrameText.textbox_value = ctk.CTkLabel(self, width=150, height=80, text="", fg_color=("#3B8ED0"), corner_radius=6, font=font_text_box)
        FrameText.textbox_value.grid(row=1, column=0, padx=10, pady=10)

        l_qte_total = ctk.CTkLabel(self, text="Quantidade de itens", font=font_label)
        l_qte_total.grid(row=4, column=0, padx=10, pady=(25,10))
        
        FrameText.textbox_qte_itens = ctk.CTkLabel(self, width=150, height=80, text="", fg_color=("#3B8ED0"), corner_radius=6, font=font_text_box)
        FrameText.textbox_qte_itens.grid(row=5, column=0, padx=10, pady=(10, 10))

class FrameTableInfo(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        global table
       
        # List definitions for table
        table_head = ['#ID', 'Nome', 'Sala / Área', 'Descrição', 'Marca / Modelo', 'Data da Compra', 'Valor da Compra', 'Número de Série']
        width_col = [40, 50, 80, 80, 110, 115, 115, 115] 

        # Index for
        i = 0
        
        # Add Treeview widget onto the frame
        table = ttk.Treeview(self, columns=table_head, show="headings")
        table.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        
        # Table headings and width column connfiguration
        for col in table_head:
            table.heading(col, text=col)
            table.column(col, width=width_col[i])
            i += 1

        lista_itens = ver_form()
        for item in lista_itens:
            table.insert('', 'end', values=item)

        quantidade = []

        for item in lista_itens:
            quantidade.append(item[6])

        FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
        FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")


class FrameImage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Font object:
        font_img_label = ctk.CTkFont(size=14, weight="bold")

        FrameImage.l_image_title = ctk.CTkLabel(self, text="Foto do Item", width=300, font=font_img_label)
        FrameImage.l_image_title.grid(row = 0, column = 0, padx = 15, pady = 2, stick = "new")
       
        FrameImage.l_image = ctk.CTkLabel(self, text="")
        FrameImage.l_image.grid(row = 1, column = 0, padx = 15, pady = (0,15), stick = "nsew")


class App(ctk.CTk):

    # Geometry constants:
    width = 900
    height = 600    
    
    def __init__(self):
        super().__init__()        
        #self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.title("")

        # Create 3x4 grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)  
        
        self.FrameTitleBar = FrameTitleBar(master=self)
        self.FrameTitleBar.grid(row=0, column=0, columnspan=4, stick="new")

        self.FrameForm = FrameForm(master=self)
        self.FrameForm.grid(row=1, column=0, pady=2, padx=1, stick="nsw")

        self.FrameButton = FrameButton(master=self)
        self.FrameButton.grid(row=1, column=1, pady=2, padx=1, stick="nsw")

        self.FrameText = FrameText(master=self)
        self.FrameText.grid(row=1, column=2, pady=2, padx=1, stick="nsw")

        self.FrameImage = FrameImage(master=self)
        self.FrameImage.grid(row=1, column=3, pady=2, padx=2, stick="nsw")

        self.FrameTableInfo = FrameTableInfo(master=self)
        self.FrameTableInfo.grid(row=2, column=0, columnspan=4, pady=2, padx=1, stick="sew")

app = App()
app.mainloop()