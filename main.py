import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

textoEntradaNome = None
textoEntradaCpf = None
textoEntradaEstado = None

def salvar_dados():
    global textoEntradaNome, textoEntradaCpf, textoEntradaEstado

    if textoEntradaNome.get() and textoEntradaCpf.get() and textoEntradaEstado.get():
        conn = sqlite3.connect('dados.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          nome TEXT NOT NULL,
                          cpf TEXT NOT NULL,
                          estado TEXT NOT NULL)''')

        cursor.execute("INSERT INTO clientes (nome, cpf, estado) VALUES (?, ?, ?)", (textoEntradaNome.get(), textoEntradaCpf.get(), textoEntradaEstado.get()))
        conn.commit()

        conn.close()

        mb.showinfo("Sucesso", "Dados salvos com sucesso!")
    else:
        mb.showerror("Erro", "Por favor, preencha todos os campos.")

def main():
    global textoEntradaNome, textoEntradaCpf, textoEntradaEstado

    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)

    # Abrir a imagem usando Pillow
    imagem = Image.open("background.png")

    # Converter a imagem para um formato que o Tkinter possa usar
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Adicionar a imagem de fundo
    canvas = tkinter.Canvas(root, width=imagem.width, height=imagem.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=imagem_tk, anchor="nw")

    label = tkinter.Label(canvas, text="Nome")
    label.place(x=50, y=50) 

    textoEntradaNome = tkinter.StringVar()
    e1 = tkinter.Entry(canvas, textvariable=textoEntradaNome)
    e1.place(x=150, y=50) 

    label = tkinter.Label(canvas, text="Cpf")
    label.place(x=50, y=80)  

    textoEntradaCpf = tkinter.StringVar()
    e2 = tkinter.Entry(canvas, textvariable=textoEntradaCpf)
    e2.place(x=150, y=80)  

    label = tkinter.Label(canvas, text="Estado")
    label.place(x=50, y=110)  

    textoEntradaEstado = tkinter.StringVar()
    e3 = tkinter.Entry(canvas, textvariable=textoEntradaEstado)
    e3.place(x=150, y=110)  

    # Botão para salvar os dados
    botao_salvar = tkinter.Button(canvas, text="Salvar", command=salvar_dados)
    botao_salvar.place(x=100, y=150)  

    root.mainloop()

main()
