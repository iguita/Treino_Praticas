import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Adivinhação")
        
        # Número secreto e tentativas
        self.numero_secreto = random.randint(1, 20)
        self.tentativas = 0
        
        # Layout gráfico
        self.label_titulo = tk.Label(self.master, text="Tente adivinhar o número entre 1 e 20!", font=("Arial", 14))
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=10)
        
        self.label_palpite = tk.Label(self.master, text="Digite seu palpite:", font=("Arial", 12))
        self.label_palpite.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_palpite = tk.Entry(self.master, font=("Arial", 12))
        self.entry_palpite.grid(row=1, column=1, padx=10, pady=10)
        
        self.btn_confirmar = tk.Button(self.master, text="Confirmar", command=self.verificar_palpite, font=("Arial", 12))
        self.btn_confirmar.grid(row=2, column=0, columnspan=2, pady=10)
        
        self.label_feedback = tk.Label(self.master, text="", font=("Arial", 12))
        self.label_feedback.grid(row=3, column=0, columnspan=2, pady=10)

    def verificar_palpite(self):
        try:
            palpite = int(self.entry_palpite.get())
            self.tentativas += 1

            if palpite > self.numero_secreto:
                self.label_feedback.config(text="Muito alto! Tente um número menor.")
            elif palpite < self.numero_secreto:
                self.label_feedback.config(text="Muito baixo! Tente um número maior.")
            else:
                messagebox.showinfo("Parabéns!", f"Você acertou o número {self.numero_secreto} em {self.tentativas} tentativas!")
                self.reiniciar_jogo()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(1, 20)
        self.tentativas = 0
        self.entry_palpite.delete(0, tk.END)
        self.label_feedback.config(text="")

# Criar a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()
