import tkinter
from tkinter import messagebox as mb
from tkinter import ttk
import sqlite3

def chamarBotao():
    # Função de exemplo para o botão 'Salvar'
    print("Salvo com sucesso")


def main():
    root = tkinter.Tk()
    root.title("Trabalho RAD")
    root.resizable(False, False)
    
    label = tkinter.Label(root, text="Nome")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = chamarBotao

    
    label = tkinter.Label(root, text="Cpf")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = chamarBotao

    
    label = tkinter.Label(root, text="Estado")
    label.pack()

    textoEntrada = tkinter.StringVar()
    e1 = tkinter.Entry(root)
    e1.bind('<Key>', lambda x:textoEntrada.set(e1.get()+x.char))
    e1.pack()
    
    test2 = tkinter.Button(root, text="Salvar")
    test2['command'] = chamarBotao

    test2.pack()

    root.iconify() 
    root.update()
    root.deiconify() 
    root.mainloop()

main()