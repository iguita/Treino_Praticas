import tkinter as tk
from tkinter import messagebox
import math

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.resultado = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Tela de entrada
        self.entry1 = tk.Entry(self.master, textvariable=self.valor1, justify='right', font=("Arial", 16))
        self.entry1.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.dropdown = tk.StringVar(value="+")
        self.operadores = tk.OptionMenu(self.master, self.dropdown, "+", "-", "*", "/", "raiz", "potencia", "fatorial", "fibonacci", "porcento", "media")
        self.operadores.grid(row=0, column=3)

        self.entry2 = tk.Entry(self.master, textvariable=self.valor2, justify='right', font=("Arial", 16))
        self.entry2.grid(row=0, column=4)

        # Botões
        self.btn_calcular = tk.Button(self.master, text="Calcular", command=self.calcular, font=("Arial", 12))
        self.btn_calcular.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.btn_limpar = tk.Button(self.master, text="Limpar", command=self.limpar, font=("Arial", 12))
        self.btn_limpar.grid(row=1, column=2, columnspan=2, sticky="nsew")

        # Resultado
        self.label_resultado = tk.Label(self.master, textvariable=self.resultado, font=("Arial", 16))
        self.label_resultado.grid(row=2, column=0, columnspan=5, sticky="nsew")

        # Configurar o grid
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

    def calcular(self):
        try:
            num1 = float(self.valor1.get())
            num2 = float(self.valor2.get()) if self.dropdown.get() not in ["raiz", "fatorial", "fibonacci"] else 0
            operador = self.dropdown.get()

            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro! Divisão por zero."
            elif operador == "raiz":
                resultado = f"√{num1} = {math.sqrt(num1):.2f}"
            elif operador == "potencia":
                resultado = f"{num1}^{num2} = {math.pow(num1, num2):.2f}"
            elif operador == "fatorial":
                resultado = self.fatorial(int(num1))
            elif operador == "fibonacci":
                resultado = self.fibonacci(int(num1))
            elif operador == "porcento":
                resultado = (num1 / 100) * num2
            elif operador == "media":
                resultado = self.media(num1, num2)
            else:
                resultado = "Operação inválida."

            self.resultado.set("Resultado: " + str(resultado))

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

    def fatorial(self, n):
        if n < 0:
            return "Erro! Fatorial de número negativo."
        res = 1
        for i in range(1, n + 1):
            res *= i
        return f"{n}! = {res}"

    def fibonacci(self, n):
        if n < 0:
            return "Erro! Fibonacci de número negativo."
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return ", ".join(map(str, fib[:n + 1]))

    def media(self, n1, n2):
        return f"Média: {(n1 + n2) / 2:.2f}"

    def limpar(self):
        self.valor1.set("")
        self.valor2.set("")
        self.resultado.set("Resultado:")

# Criar a janela principal
if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()

