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

# Deletar inventorio
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Inventario WHERE id=?"
        cur.execute(query, i)

# Atualizar inventorio
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Inventario SET nome=?, local=?, descricao=?, marca=?, data_compra=?, valor_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)

# Ver Inventario
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver Item no inventorio
def ver_item(id):
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE id=?",(id))
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens