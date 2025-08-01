import tkinter as tk
from tkinter import messagebox, scrolledtext, simpledialog
import datetime
import os

# Função para adicionar anotação
def adicionar_anotacao():
    humor = entrada_humor.get()
    gatilho = entrada_gatilho.get()

    if not humor or not gatilho:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return

    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texto = f"{data} - Humor: {humor}, Gatilho: {gatilho}\n"

    with open("humor_diario.txt", "a") as arquivo:
        arquivo.write(texto)

    messagebox.showinfo("Sucesso", "Anotação adicionada com sucesso!")
    entrada_humor.delete(0, tk.END)
    entrada_gatilho.delete(0, tk.END)

# Função para visualizar e excluir anotações
def visualizar_anotacoes():
    try:
        with open("humor_diario.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            messagebox.showinfo("Informação", "Nenhuma anotação encontrada.")
            return

        janela_visualizar = tk.Toplevel(janela)
        janela_visualizar.title("Anotações de Humor")
        janela_visualizar.geometry("550x400")

        listbox = tk.Listbox(janela_visualizar, width=80, height=20)
        listbox.pack(padx=10, pady=10)

        for linha in linhas:
            listbox.insert(tk.END, linha.strip())

        def excluir_anotacao():
            selecionado = listbox.curselection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione uma anotação para excluir.")
                return

            index = selecionado[0]
            confirm = messagebox.askyesno("Confirmar Exclusão", "Deseja realmente excluir esta anotação?")
            if confirm:
                # Remove a linha do arquivo
                del linhas[index]
                with open("humor_diario.txt", "w") as arquivo:
                    arquivo.writelines(linhas)
                listbox.delete(index)
                messagebox.showinfo("Excluído", "Anotação excluída com sucesso.")

        tk.Button(janela_visualizar, text="Excluir anotação selecionada", command=excluir_anotacao).pack(pady=5)

    except FileNotFoundError:
        messagebox.showinfo("Informação", "Nenhuma anotação encontrada.")

# Criar janela principal
janela = tk.Tk()
janela.title("Diário de Humor")
janela.geometry("350x300")

# Campos de entrada
tk.Label(janela, text="Como você se sente hoje?").pack(pady=(10, 0))
entrada_humor = tk.Entry(janela, width=40)
entrada_humor.pack(pady=5)

tk.Label(janela, text="O que causou esse humor?").pack()
entrada_gatilho = tk.Entry(janela, width=40)
entrada_gatilho.pack(pady=5)

# Botões principais
tk.Button(janela, text="Adicionar Anotação", command=adicionar_anotacao).pack(pady=10)
tk.Button(janela, text="Visualizar/Excluir Anotações", command=visualizar_anotacoes).pack(pady=5)

# Iniciar interface
janela.mainloop()



