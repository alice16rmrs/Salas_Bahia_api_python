from tkinter import Tk, Frame, Label, Entry, Button, Canvas, messagebox, PhotoImage, mainloop
from tkinter import LEFT, END, NW
import json
import requests


class Application:

    def __init__(self, master=None):

        self.fontePadrao = ("Arial", "10")
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["pady"] = 20
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["pady"] = 0
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["pady"] = 20
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["pady"] = 20
        self.container8.pack()

        self.labelTitle = Label(self.container1, text="Salas Bahia Estoque - CRUD")
        self.labelTitle["font"] = ("Arial", "10", "bold")
        self.labelTitle.pack()

        self.labelID = Label(self.container2, text="ID", font=self.fontePadrao, width=10)
        self.labelID.pack(side=LEFT)

        self.entryID = Entry(self.container2)
        self.entryID["width"] = 20
        self.entryID["font"] = self.fontePadrao
        self.entryID.pack(side=LEFT)

        self.labelNome = Label(self.container3, text="Nome", font=self.fontePadrao, width=10)
        self.labelNome.pack(side=LEFT)

        self.entryNome = Entry(self.container3)
        self.entryNome["width"] = 20
        self.entryNome["font"] = self.fontePadrao
        self.entryNome.pack(side=LEFT)

        self.labelQtd = Label(self.container4, text="Quantidade", font=self.fontePadrao, width=10)
        self.labelQtd.pack(side=LEFT)

        self.entryQtd = Entry(self.container4)
        self.entryQtd["width"] = 20
        self.entryQtd["font"] = self.fontePadrao
        self.entryQtd.pack(side=LEFT)

        self.buttonBuscar = Button(self.container8)
        self.buttonBuscar["text"] = "Buscar\npor ID"
        self.buttonBuscar["font"] = ("Calibri", "10")
        self.buttonBuscar["width"] = 12
        self.buttonBuscar["height"] = 3
        self.buttonBuscar["command"] = self.buscarProduto
        self.buttonBuscar.pack(side=LEFT)

        self.buttonInserir = Button(self.container8)
        self.buttonInserir["text"] = "Inserir\nProduto"
        self.buttonInserir["font"] = ("Calibri", "10")
        self.buttonInserir["width"] = 12
        self.buttonInserir["height"] = 3
        self.buttonInserir["command"] = self.inserirProduto
        self.buttonInserir.pack(side=LEFT)

        self.buttonAlterar = Button(self.container8)
        self.buttonAlterar["text"] = "Alterar\nProduto"
        self.buttonAlterar["font"] = ("Calibri", "10")
        self.buttonAlterar["width"] = 12
        self.buttonAlterar["height"] = 3
        self.buttonAlterar["command"] = self.alterarProduto
        self.buttonAlterar.pack(side=LEFT)

        self.buttonExcluir = Button(self.container8)
        self.buttonExcluir["text"] = "Excluir\nProduto"
        self.buttonExcluir["font"] = ("Calibri", "10")
        self.buttonExcluir["width"] = 12
        self.buttonExcluir["height"] = 3
        self.buttonExcluir["command"] = self.excluirProduto
        self.buttonExcluir.pack(side=LEFT)

    # Método para localizar o produto na API a partir do atributo "ID" informado
    def buscarProduto(self):

        self.limparTela()
        produto_id = self.entryID.get()
        req = requests.get('http://localhost:5000/crud/api/produtos/' + produto_id)

        if req.ok:
            resposta = req.json()
            self.entryNome.insert(0, resposta['produto']['nome'])
            self.entryQtd.insert(0, resposta['produto']['qtd'])
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao consultar a API")

    # Método para inserir um produto na API, passando como parâmetros o Nome e o Preço digitados
    # Se for digitada também uma URL de imagem, o programa gera uma miniatura e salva na pasta "GUI"
    def inserirProduto(self):

        # try:
        nome = self.entryNome.get()
        qtd = self.entryQtd.get()

        data = {
            'nome': nome,
            'qtd': int(qtd)
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.post(url='http://localhost:5000/crud/api/produtos', headers=headers, data=json.dumps(data))

        if req.ok:
            self.entryID.delete(0, END)
            self.limparTela()
            messagebox.showinfo("Sucesso", "Produto inserido com sucesso!")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao consultar a API")

    # Método para modificar um produto na API, devendo ser informados o ID, Nome e o Preço
    # Se for digitada também uma URL de imagem, o programa gera uma miniatura e salva na pasta "GUI"
    def alterarProduto(self):
        id = self.entryID.get()
        nome = self.entryNome.get()
        qtd = self.entryQtd.get()

        data = {
            'nome': nome,
            'qtd': int(qtd)
        }

        headers = {
            'Content-Type': 'application/json',
        }

        req = requests.put(url='http://localhost:5000/crud/api/produtos/' + id, headers=headers, data=json.dumps(data))

        if req.ok:
            self.entryID.delete(0, END)
            self.limparTela()
            messagebox.showinfo("Sucesso", "Produto alterado com sucesso!")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao consultar a API")

    # Método para excluir um produto da API a partir do ID fornecido
    def excluirProduto(self):
        id = self.entryID.get()
        req = requests.delete('http://localhost:5000/crud/api/produtos/' + id)

        if req.ok:
            self.entryID.delete(0, END)
            self.limparTela()
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
        else:
            messagebox.showerror("Erro", "Ocorreu um erro ao consultar a API")

    def limparTela(self):
        self.entryQtd.delete(0, END)
        self.entryNome.delete(0, END)


root = Tk()
Application(root)
root.mainloop()
