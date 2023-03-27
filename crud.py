import sqlite3 as lite
from datetime import datetime

# Criando conexão
con = lite.connect('dados.db')

# Inserir inventorio
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Inventario (nome, local, descricao, marca, data_compra, valor_compra, serie, imagem) VALUES (?,?,?,?,?,?,?,?)"
        cur.execute(query, i)

# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        query = "SELECT name FROM sqlite_master WHERE type='table' AND name='Inventario'"
        list_table = cur.execute(query).fetchall()
        if list_table == []:
            cur.execute("CREATE TABLE Inventario(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_compra DATE, valor_compra DECIMAL, serie TEXT, imagem TEXT)")        
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Atualizar inventorio
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)

# Deletar inventorio
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query, i)
