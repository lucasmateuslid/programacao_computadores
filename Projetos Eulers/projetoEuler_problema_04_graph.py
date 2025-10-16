import tkinter as tk
from tkinter import ttk

def calcular_palindromo():
    # Limpa o texto anterior
    resultado_var.set("Calculando...")

    valor_produto01 = 100
    maiorPalindromo = 0
    fator_a = 0
    fator_b = 0

    while valor_produto01 <= 999:
        valor_produto02 = valor_produto01  # evita repetições (ex: 101x102 e 102x101)
        while valor_produto02 <= 999:
            multiplica_produtos = valor_produto01 * valor_produto02
            check = str(multiplica_produtos)
            if check == check[::-1] and multiplica_produtos > maiorPalindromo:
                maiorPalindromo = multiplica_produtos
                fator_a = valor_produto01
                fator_b = valor_produto02
            valor_produto02 += 1
        valor_produto01 += 1

    # Atualiza a interface com o resultado final
    resultado_var.set(f"Maior Palíndromo: {maiorPalindromo}\nFatores: {fator_a} x {fator_b}")

# ===== INTERFACE GRÁFICA =====

janela = tk.Tk()
janela.title("Maior Palíndromo de 3 Dígitos")
janela.geometry("400x250")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="🔢 Palíndromo 3 Dígitos",
    font=("Arial", 16, "bold"),
    fg="#333"
)
titulo.pack(pady=15)

# Botão para iniciar cálculo
botao_calcular = ttk.Button(
    janela,
    text="Calcular Palíndromo",
    command=calcular_palindromo
)
botao_calcular.pack(pady=10)

# Resultado
resultado_var = tk.StringVar(value="Clique no botão para começar...")
resultado_label = tk.Label(
    janela,
    textvariable=resultado_var,
    font=("Arial", 12),
    justify="center",
    wraplength=350
)
resultado_label.pack(pady=20)

# Rodapé
rodape = tk.Label(
    janela,
    text="Desenvolvido por Lucas Mateus",
    font=("Arial", 9),
    fg="#666"
)
rodape.pack(side="bottom", pady=5)

# Inicia o loop da janela
janela.mainloop()
