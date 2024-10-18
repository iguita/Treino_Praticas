import tkinter as tk
from tkinter import messagebox

class GerenciadorTarefas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Tarefas")
        
        self.tarefas = []

        # Label de Título
        self.label_titulo = tk.Label(self.master, text="Gerenciador de Tarefas", font=("Arial", 16))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Campo de Entrada para Nova Tarefa
        self.entry_tarefa = tk.Entry(self.master, width=40, font=("Arial", 12))
        self.entry_tarefa.grid(row=1, column=0, padx=10, pady=10)

        # Botão de Adicionar Tarefa
        self.btn_adicionar = tk.Button(self.master, text="Adicionar Tarefa", command=self.adicionar_tarefa, font=("Arial", 12))
        self.btn_adicionar.grid(row=1, column=1, padx=10, pady=10)

        # Lista de Tarefas
        self.listbox_tarefas = tk.Listbox(self.master, width=40, height=10, font=("Arial", 12))
        self.listbox_tarefas.grid(row=2, column=0, padx=10, pady=10)

        # Botão de Remover Tarefa
        self.btn_remover = tk.Button(self.master, text="Remover Tarefa", command=self.remover_tarefa, font=("Arial", 12))
        self.btn_remover.grid(row=2, column=1, padx=10, pady=10)

    def adicionar_tarefa(self):
        tarefa = self.entry_tarefa.get()
        if tarefa:  # Se a tarefa não for vazia
            self.tarefas.append(tarefa)
            self.atualizar_lista_tarefas()
            self.entry_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "A tarefa não pode estar vazia.")

    def remover_tarefa(self):
        try:
            indice = self.listbox_tarefas.curselection()[0]
            self.tarefas.pop(indice)
            self.atualizar_lista_tarefas()
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

    def atualizar_lista_tarefas(self):
        self.listbox_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.listbox_tarefas.insert(tk.END, tarefa)

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    gerenciador = GerenciadorTarefas(root)
    root.mainloop()
