import os
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

from PIL import Image
from tkcalendar import Calendar
import customtkinter as ctk

from crud import * 

# Constants
PATH = os.path.dirname(os.path.realpath(__file__))

# ==================== Functions ======================

def selecionar_imagem():

    global image_path    
    
    image_path = fd.askopenfilename(filetypes=[('JPEG Files', '.jpg .jpeg'), ('PNG Files', '.png')])

    try:
        image = ctk.CTkImage(Image.open(image_path), size=(275,275))
        FrameImage.l_image.configure(image=image)    
    
    except:
        messagebox.showerror('Erro', 'Não foi possível identificar a imagem. Por favor, confira o tipo de arquivo e selecione novamente.') 

def delete_entries():
        
    FrameForm.e_nome.delete(0, 'end')
    FrameForm.e_local.delete(0, 'end')
    FrameForm.e_descricao.delete(0, 'end')
    FrameForm.e_model.delete(0, 'end')
    FrameForm.e_data_compra.configure(state="normal")
    FrameForm.e_data_compra.delete(0, 'end')
    FrameForm.e_data_compra.configure(state="disabled")   
    FrameForm.e_valor.delete(0, 'end')
    FrameForm.e_serial.delete(0, 'end')
    FrameImage.l_image.configure(image=None)

def inserir():
         
    global table, image_path

    # Insert the data list with the form entries
    nome = FrameForm.e_nome.get()
    local = FrameForm.e_local.get()
    descricao = FrameForm.e_descricao.get()
    model = FrameForm.e_model.get()
    data = FrameForm.e_data_compra.get()
    valor = FrameForm.e_valor.get()
    serie = FrameForm.e_serial.get()

    try:
        imagem = image_path

    except NameError:
        messagebox.showerror('Erro', 'Preencha todos os campos e selecione uma imagem.')    
        return
    
    else:    
        lista_inserir = [nome, local, descricao, model, data, valor, serie, imagem]

        for i in lista_inserir:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos e selecione uma imagem.')
                return

        inserir_form(lista_inserir)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    # Delete entries of FrameForm, table and image.
    delete_entries()

    for item in table.get_children():
        table.delete(item)

    # Update info of the table, qtd labels and image
    lista_itens = ver_form()
    for item in lista_itens:
        table.insert('', 'end', values=item)

    quantidade = []
    for item in lista_itens:
        quantidade.append(item[6])

    FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
    FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

def atualizar():
    
    global table_view_list

    try:
        table_view_data = table.focus()
        table_view_dic = table.item(table_view_data)
        table_view_list = table_view_dic['values']
                
        # Delete entries of FrameForm, table and image.
        delete_entries() 

        # Get values and image of item selected
        FrameForm.e_nome.insert(0, table_view_list[1])
        FrameForm.e_local.insert(0, table_view_list[2])
        FrameForm.e_descricao.insert(0, table_view_list[3])
        FrameForm.e_model.insert(0, table_view_list[4])
        FrameForm.e_data_compra.configure(state="normal")
        FrameForm.e_data_compra.insert(0, table_view_list[5])
        FrameForm.e_data_compra.configure(state="disabled") 
        FrameForm.e_valor.insert(0, table_view_list[6])
        FrameForm.e_serial.insert(0, table_view_list[7])           
        image_path = table_view_list[8]
        image = ctk.CTkImage(Image.open(image_path), size=(275,275))
        FrameImage.l_image.configure(image=image)   

        # Update state of buttons 
        FrameButton.button_update.configure(state="normal")
        FrameButton.button_delete.configure(state="normal")        

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

def update():

    global table_view_list, table
    
    # Update the list with the form entries
    nome = FrameForm.e_nome.get()
    local = FrameForm.e_local.get()
    descricao = FrameForm.e_descricao.get()
    model = FrameForm.e_model.get()
    data = FrameForm.e_data_compra.get()
    valor = FrameForm.e_valor.get()
    serie = FrameForm.e_serial.get()           
    imagem = table_view_list[8]
    id = int(table_view_list[0])
     
    lista_atualizar = [nome, local, descricao, model, data, valor, serie, imagem, id]    
    for i in lista_atualizar:
        if i=='':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    atualizar_form(lista_atualizar)
    messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

    # Delete entries of FrameForm, table and image.
    delete_entries()

    for item in table.get_children():
        table.delete(item)

    # Update info of the table, qtd labels and image
    lista_itens = ver_form()
    for item in lista_itens:
        table.insert('', 'end', values=item)

    quantidade = []
    for item in lista_itens:
        quantidade.append(item[6])

    FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
    FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

    # Update state of button_update 
    FrameButton.button_update.configure(state="disabled")
    FrameButton.button_delete.configure(state="disabled")

def deletar():

    global table_view_list, table

    id = table_view_list[0]
    deletar_form([id])
    messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

    # Delete entries of FrameForm, table and image
    delete_entries()

    for item in table.get_children():
        table.delete(item)

    # Update info of the table, qtd labels and image
    lista_itens = ver_form()
    for item in lista_itens:
        table.insert('', 'end', values=item)

    quantidade = []
    for item in lista_itens:
        quantidade.append(item[6])

    FrameText.textbox_value.configure(text="R$ {:,.2f}".format(sum(quantidade)))
    FrameText.textbox_qte_itens.configure(text=f"{len(quantidade)}")

    # Update state of buttons 
    FrameButton.button_delete.configure(state="disabled")
    FrameButton.button_update.configure(state="disabled")


# ==================== Frames =========================

class FrameTitleBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
     
        # Create 1x3 grid system -- column configure
        self.columnconfigure(2, weight=1)
        
        # Font object
        font_title = ctk.CTkFont(family="Verdana", size=24, weight="bold")
        font_option_btn = ctk.CTkFont(size=13, weight="bold")  

        # Open image
        app_img = ctk.CTkImage(Image.open(PATH + "/images/cadastre-se.png"), size=(50,50))
        option_img = ctk.CTkImage(Image.open(PATH + "/images/settings.png"), size=(25,25))

        # Add widgets onto the FrameTitleBar
        label_img = ctk.CTkLabel(self, text="", image=app_img)
        label_img.grid(row=0, column=0, padx=(10,5), pady=5, stick="ne")

        label_title = ctk.CTkLabel(self, text="Inventário Doméstico", font=font_title)
        label_title.grid(row=0, column=1, padx=(5,0), pady=0, stick="nse")

        button_option = ctk.CTkButton(self, text="Opções", image=option_img, font=font_option_btn, state="disabled")
        button_option.grid(row=0, column=2, padx=10, pady=10, stick="nse")


class FrameForm(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create 8x2 grid system
        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)
        self.columnconfigure((0, 1), weight=1)

        # Font object:
        font_form = ctk.CTkFont(size=14, weight="normal")        

        # Add widgets onto the FrameForm
        # Name
        l_nome = ctk.CTkLabel(self, text="Nome:",font=font_form, anchor=ctk.W)
        l_nome.grid(row=0, column=0, padx=10, pady=(10,5), stick="w")
        FrameForm.e_nome = ctk.CTkEntry(self, width=225)
        FrameForm.e_nome.grid(row=0, column=1, padx=10, pady=(10,5), stick="ne")

        # Area
        l_local = ctk.CTkLabel(self, text="Área:", font=font_form, anchor=ctk.W)
        l_local.grid(row=1, column=0, padx=10, stick="w")
        FrameForm.e_local = ctk.CTkEntry(self, width=225)
        FrameForm.e_local.grid(row=1, column=1, padx=10, pady=5, stick="ne")

        # Description
        l_descricao = ctk.CTkLabel(self, text="Descrição:",font=font_form, anchor=ctk.W)
        l_descricao.grid(row=2, column=0, padx=10, stick="w")
        FrameForm.e_descricao = ctk.CTkEntry(self, width=225)
        FrameForm.e_descricao.grid(row=2, column=1, padx=10, pady=5, stick="ne")

        # Model
        l_model = ctk.CTkLabel(self, text="Marca ou modelo:", font=font_form, anchor=ctk.W)
        l_model.grid(row=3, column=0, padx=10, stick="w")
        FrameForm.e_model = ctk.CTkEntry(self, width=225)
        FrameForm.e_model.grid(row=3, column=1, padx=10, pady=5, stick="ne") 

        # Price
        l_valor = ctk.CTkLabel(self, text="Valor da compra:", font=font_form, anchor=ctk.W)
        l_valor.grid(row=4, column=0, padx=10, stick="w")
        FrameForm.e_valor = ctk.CTkEntry(self, width=225)
        FrameForm.e_valor.grid(row=4, column=1, padx=10, pady=5, stick="ne")

        # Serial number
        l_serial = ctk.CTkLabel(self, text="Número de série:", font=font_form, anchor=ctk.W)
        l_serial.grid(row=5, column=0, padx=10, stick="w")
        FrameForm.e_serial = ctk.CTkEntry(self, width=225)
        FrameForm.e_serial.grid(row=5, column=1, padx=10, pady=5, stick="se")

        # Date
        l_cal = ctk.CTkLabel(self, text="Data da compra:", font=font_form, anchor=ctk.W)
        l_cal.grid(row=6, column=0, padx=(10,0), stick="we")
        FrameForm.e_data_compra = ctk.CTkEntry(self, width=85)
        FrameForm.e_data_compra.grid(row=6, column=1, padx=10, stick="w")        
        button_date = ctk.CTkButton(self, width=120, text="Selecionar Data", font=font_form, command=lambda: self.create_toplevel_date("compra"))
        button_date.grid(row=6, column=1, padx=10, pady=5, stick="e")

        # Image
        l_view = ctk.CTkLabel(self, text="Imagem do item:", font=font_form, width=120, anchor=ctk.W)
        l_view.grid(row=7, column=0, padx=10, stick="w")
        button_view = ctk.CTkButton(self, width=224, text="Selecionar Imagem", font=font_form, command=selecionar_imagem)
        button_view.grid(row=7, column=1, padx=10, pady=(5,10), stick="se")

    # =========== Window of date pick  ==============
    def create_toplevel_date(self, campo_data):
        
        global date_window, cal

        # CTkToplevel window configuration
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

        # Open image
        add_img = ctk.CTkImage(Image.open(PATH + "/images/portfolio.png"), size=(40,40))
        update_img = ctk.CTkImage(Image.open(PATH + "/images/refresh.png"), size=(40,40))
        confirm_img = ctk.CTkImage(Image.open(PATH + "/images/configuration.png"), size=(40,40))
        clear_img = ctk.CTkImage(Image.open(PATH + "/images/trash.png"), size=(40,40))
               
        # Create 4x1 grid system -- row configuration
        self.rowconfigure((0, 1, 2, 3), weight=1)
                
        # Font object
        font_button = ctk.CTkFont(size=13, weight="bold")

        # Add widgets onto the FrameButton
        FrameButton.button_add = ctk.CTkButton(self, width=175, text="Adicionar", image=add_img, compound="left", font=font_button, command=inserir)        
        FrameButton.button_add.grid(row=0, column=0, padx=5, pady=5)
        
        FrameButton.button_view = ctk.CTkButton(self, width=175, text="Visualizar", image=update_img, compound="left", font=font_button, command=atualizar)
        FrameButton.button_view.grid(row=1, column=0, padx=5, pady=5)
        
        FrameButton.button_update = ctk.CTkButton(self, width=175, text="Atualizar", image=confirm_img, state="disabled", font=font_button, command=update)
        FrameButton.button_update.grid(row=2, column=0, padx=5, pady=5)

        FrameButton.button_delete = ctk.CTkButton(self, width=175, text="Excluir",image=clear_img, compound="left", state="disabled", font=font_button, command=deletar) 
        FrameButton.button_delete.grid(row=3, column=0, padx=5, pady=5)


class FrameText(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)   

        # Font object
        font_label = ctk.CTkFont(size=15, weight="bold")
        font_textbox_small = ctk.CTkFont(size=20, weight="bold")
        font_textbox_large = ctk.CTkFont(size=46, weight="bold")

        # Add widgets onto the FrameText
        l_value_total = ctk.CTkLabel(self, text="Valor total dos itens", font=font_label)
        l_value_total.grid(row=0, column=0, padx=10, pady=10)

        FrameText.textbox_value = ctk.CTkLabel(self, width=150, height=80, text="", fg_color=("#3B8ED0"), corner_radius=6, font=font_textbox_small)
        FrameText.textbox_value.grid(row=1, column=0, padx=10, pady=10)

        l_qte_total = ctk.CTkLabel(self, text="Quantidade de itens", font=font_label)
        l_qte_total.grid(row=4, column=0, padx=10, pady=(25,10))
        
        FrameText.textbox_qte_itens = ctk.CTkLabel(self, width=150, height=80, text="", fg_color=("#3B8ED0"), corner_radius=6, font=font_textbox_large)
        FrameText.textbox_qte_itens.grid(row=5, column=0, padx=10, pady=(10, 10))

class FrameTableInfo(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        global table

        # Create 2x3 grid system
        self.columnconfigure((0, 2), weight=1)
        self.columnconfigure(1, weight=30)
        
        # Font object
        font_label = ctk.CTkFont(size=13, weight="bold")

        # Open image
        search_img = ctk.CTkImage(Image.open(PATH + "/images/magnifying-glass.png"), size=(25,25))
        
        # Add widgets onto the FrameText
        l_value_search = ctk.CTkLabel(self, text="Pesquisar", image=search_img, compound="left", padx=8, font=font_label)
        l_value_search.grid(row=0, column=0, padx=(10,0)  , stick="w")

        e_value_search = ctk.CTkEntry(self, state="disabled")
        e_value_search.grid(row=0, column=1, padx=0, pady=5, stick="we")

        button_search = ctk.CTkButton(self, text="Pesquisar", state="disabled", font=font_label)
        button_search.grid(row=0, column=2, padx=10, stick="e")
       
        # List definitions for table
        table_head = ['#ID', 'Nome', 'Sala / Área', 'Descrição', 'Marca / Modelo', 'Data da Compra', 'Valor da Compra', 'Número de Série']
        width_col = [40, 125, 125, 210, 165, 118, 118, 140]         
        i = 0 # Index for
        
        # Add Treeview widget onto the frame
        table = ttk.Treeview(self, columns=table_head, selectmode="browse", show="headings")
        table.grid(row=1, column=0, padx=10, pady=(5,10), columnspan=3, sticky='nsew')
        
        # Table headings and width column connfiguration
        for col in table_head:
            table.heading(col, text=col)
            table.column(col, width=width_col[i])
            i += 1

        # Update info of the table, qtd labels and image
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

        # Font object
        font_img_label = ctk.CTkFont(size=14, weight="bold")
        
        # Add widgets onto the FrameImage
        FrameImage.l_image_title = ctk.CTkLabel(self, text="Foto do Item", width=300, font=font_img_label)
        FrameImage.l_image_title.grid(row = 0, column = 0, padx = 15, pady = 2, stick = "new")
       
        FrameImage.l_image = ctk.CTkLabel(self, text="")
        FrameImage.l_image.grid(row = 1, column = 0, padx = 15, pady = (0,15), stick = "nsew")


class App(ctk.CTk): 
    def __init__(self):
        super().__init__()  

        # Configure window   
        self.resizable(False, False)
        self.title("")

        # Create 3x4 grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)  

        # Add frames to App        
        self.FrameTitleBar = FrameTitleBar(master=self)
        self.FrameTitleBar.grid(row=0, column=0, pady=(3, 1), padx=3, columnspan=4, stick="new")

        self.FrameForm = FrameForm(master=self)
        self.FrameForm.grid(row=1, column=0, pady=2, padx=(3, 1), stick="nsw")

        self.FrameButton = FrameButton(master=self)
        self.FrameButton.grid(row=1, column=1, pady=2, padx=1, stick="nsw")

        self.FrameText = FrameText(master=self)
        self.FrameText.grid(row=1, column=2, pady=2, padx=1, stick="nsw")

        self.FrameImage = FrameImage(master=self)
        self.FrameImage.grid(row=1, column=3, pady=2, padx=(2, 3), stick="nsw")

        self.FrameTableInfo = FrameTableInfo(master=self)
        self.FrameTableInfo.grid(row=2, column=0, columnspan=4, pady=(2, 5), padx=3, stick="sew")

app = App()
app.mainloop()