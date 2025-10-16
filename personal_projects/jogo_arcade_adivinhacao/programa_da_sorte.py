# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import random
import pygame
import time
import threading
import os

# ====== CONFIGURAÇÃO DE SONS ======
pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SONS_DIR = os.path.join(BASE_DIR, "sons")

def tocar_som(nome_arquivo):
    caminho = os.path.join(SONS_DIR, nome_arquivo)
    if os.path.exists(caminho):
        threading.Thread(target=lambda: pygame.mixer.Sound(caminho).play(), daemon=True).start()
    else:
        print(f"[⚠️] Som não encontrado: {caminho}")

# ====== VARIÁVEIS GLOBAIS ======
numero_secreto = None
contador_tentativas = 0
max_tentativas = 0
game_started = False
historico = []
pontuacao = 0
inicio_tempo = 0
modo_atual = ""
jogador_atual = ""
ranking = []
limite_inferior = 0
limite_superior = 0

# ====== FUNÇÕES AUXILIARES ======
def piscar_label(cor, vezes=3, intervalo=0.1):
    original = label_resultado.cget("fg")
    for _ in range(vezes):
        label_resultado.config(fg=cor)
        janela.update()
        time.sleep(intervalo)
        label_resultado.config(fg=original)
        janela.update()
        time.sleep(intervalo)

def calcular_pontuacao(tentativas):
    if tentativas <= 5:
        return 10
    elif tentativas <= 10:
        return 5
    elif tentativas <= 15:
        return 3
    elif tentativas <= 20:
        return 1
    else:
        return 0

def atualizar_ranking(nome, pontos):
    global ranking
    ranking.append((nome, pontos))
    ranking.sort(key=lambda x: x[1], reverse=True)
    ranking = ranking[:10]

def exibir_ranking():
    texto = "\n".join([f"{i+1}. {nome} — {pontos} pts" for i, (nome, pontos) in enumerate(ranking)]) or "Nenhum jogador ainda."
    messagebox.showinfo("Ranking de Jogadores", texto)

# ====== FUNÇÕES PRINCIPAIS ======
def iniciar_jogo():
    global numero_secreto, contador_tentativas, max_tentativas, limite_inferior, limite_superior
    global game_started, historico, pontuacao, inicio_tempo, modo_atual, jogador_atual

    dificuldade = dificuldade_var.get()
    modo_atual = dificuldade

    modos = {
        "Fácil": (1, 100, 20),
        "Médio": (1, 5000, 20),
        "Difícil": (-10000, 10000, 15),
        "Insano": (-1000000, 1000000, 10),
        "Caos": (-10000000, 10000000, 8),
        "Tempo": (-100000000, 100000000, 25),
        "Roubo": (-1000000, 1000000, 20),
        "Puzzle": (-5000, 5000, 15)
    }

    if dificuldade not in modos:
        messagebox.showwarning("Erro", "Selecione uma dificuldade válida.")
        return

    limite_inferior, limite_superior, max_tentativas = modos[dificuldade]
    jogador_atual = simpledialog.askstring("Jogador", "Digite seu nome:")
    if not jogador_atual:
        messagebox.showinfo("Aviso", "É necessário informar um nome para jogar.")
        return

    numero_secreto = random.randint(limite_inferior, limite_superior)
    contador_tentativas = 0
    historico.clear()
    pontuacao = 0
    game_started = True
    inicio_tempo = time.time()
    barra['value'] = 0
    lista.delete(0, tk.END)
    entrada.delete(0, tk.END)
    entrada.focus()
    label_evento.config(text="")
    label_resultado.config(
        text=f"{jogador_atual}, adivinhe entre {limite_inferior} e {limite_superior}.",
        fg="#00FFAA"
    )
    atualizar_infos()
    tocar_som("start.mp3")

    if modo_atual == "Tempo":
        iniciar_contagem_tempo(60)

def iniciar_contagem_tempo(segundos):
    def contar():
        nonlocal segundos
        while segundos > 0 and game_started:
            label_evento.config(text=f"Tempo restante: {segundos}s")
            janela.update()
            time.sleep(1)
            segundos -= 1
        if segundos == 0 and game_started:
            encerrar_jogo(False, "Tempo esgotado!")

    threading.Thread(target=contar, daemon=True).start()

def gerar_dica_puzzle():
    dicas = []
    if numero_secreto % 2 == 0: dicas.append("O número é PAR.")
    if numero_secreto % 3 == 0: dicas.append("Divisível por 3.")
    if numero_secreto > 0: dicas.append("É POSITIVO!")
    if numero_secreto < 0: dicas.append("É NEGATIVO!")
    if not dicas: dicas.append("Zero absoluto?")
    return random.choice(dicas)

def verificar_palpite(event=None):
    global contador_tentativas, limite_inferior, limite_superior, game_started, pontuacao, numero_secreto

    if not game_started:
        messagebox.showinfo("Aviso", "Clique em 'Iniciar Jogo' primeiro.")
        return

    try:
        palpite = int(entrada.get())
    except ValueError:
        label_resultado.config(text="Entrada inválida!", fg="#FF5555")
        tocar_som("error.mp3")
        return

    contador_tentativas += 1
    entrada.delete(0, tk.END)

    if contador_tentativas > max_tentativas:
        encerrar_jogo(False, "GAME OVER! Tentativas esgotadas!")
        return

    if modo_atual == "Roubo" and contador_tentativas % 3 == 0:
        numero_secreto = random.randint(limite_inferior, limite_superior)
        limite_inferior -= random.randint(10, 50)
        limite_superior += random.randint(10, 50)
        label_evento.config(text="O sistema alterou os limites!")
        tocar_som("error.mp3")

    if palpite < numero_secreto:
        limite_inferior = palpite
        label_resultado.config(text=f"O número é MAIOR que {palpite}", fg="#00FFFF")
        tocar_som("error.mp3")
    elif palpite > numero_secreto:
        limite_superior = palpite
        label_resultado.config(text=f"O número é MENOR que {palpite}", fg="#00FFFF")
        tocar_som("error.mp3")
    else:
        encerrar_jogo(True, f"Parabéns {jogador_atual}! Acertou!")
        return

    if modo_atual == "Puzzle" and contador_tentativas % 3 == 0:
        label_evento.config(text=gerar_dica_puzzle())

    historico.append(palpite)
    lista.insert(tk.END, f"Tentativa {contador_tentativas}: {palpite}")
    lista.yview_moveto(1)
    barra['value'] = (contador_tentativas / max_tentativas) * 100
    atualizar_infos()

def encerrar_jogo(venceu, mensagem):
    global game_started, pontuacao
    game_started = False

    if venceu:
        pontuacao = calcular_pontuacao(contador_tentativas)
        atualizar_ranking(jogador_atual, pontuacao)
        tocar_som("victory.mp3")
        label_resultado.config(text=f"{mensagem}\nPontuação: {pontuacao} pts", fg="#00FF00")
        piscar_label("#00FF00", 6, 0.07)
    else:
        tocar_som("gameover.mp3")
        label_resultado.config(text=mensagem, fg="#FF0000")
        piscar_label("#FF0000", 4, 0.1)
    atualizar_infos()

# ====== INTERFACE ======
janela = tk.Tk()
janela.title("Adivinhe o Número - Ultimate Edition")
janela.geometry("1000x700")
janela.configure(bg="#000000")
janela.minsize(600, 500)

for i in range(6):
    janela.rowconfigure(i, weight=1 if i == 4 else 0)
janela.columnconfigure(0, weight=1)

titulo = tk.Label(janela, text="ADIVINHE O NÚMERO", font=("Courier New", 22, "bold"), bg="#000", fg="#00FFAA")
titulo.grid(row=0, column=0, pady=(10, 5))

# --- CONTROLES ---
frame_ctrl = tk.Frame(janela, bg="#000")
frame_ctrl.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
frame_ctrl.columnconfigure(1, weight=1)

tk.Label(frame_ctrl, text="Modo:", font=("Courier New", 10, "bold"), bg="#000", fg="#FFD700").grid(row=0, column=0, padx=5)
dificuldade_var = tk.StringVar(value="Fácil")
menu = ttk.Combobox(frame_ctrl, textvariable=dificuldade_var, values=["Fácil", "Médio", "Difícil", "Insano", "Caos", "Tempo", "Roubo", "Puzzle"], width=16, state="readonly")
menu.grid(row=0, column=1, padx=5, sticky="w")

# --- Estilo dos botões ---
style = ttk.Style()
style.theme_use("clam")
style.configure("Arc.TButton",
                font=("Courier New", 10, "bold"),
                background="#00FFAA",
                foreground="#000",
                padding=6,
                relief="raised")
style.map("Arc.TButton",
          background=[("active", "#00FFFF")],
          foreground=[("active", "#000000")])

ttk.Button(frame_ctrl, text="INICIAR", style="Arc.TButton", command=iniciar_jogo).grid(row=0, column=2, padx=8)
ttk.Button(frame_ctrl, text="RANKING", style="Arc.TButton", command=exibir_ranking).grid(row=0, column=3, padx=8)

# --- ENTRADA ---
entrada = tk.Entry(janela, font=("Courier New", 14, "bold"), justify="center", bg="#111", fg="#00FFAA", insertbackground="#00FFAA")
entrada.grid(row=2, column=0, sticky="ew", padx=300, pady=8)
entrada.bind("<Return>", verificar_palpite)
ttk.Button(janela, text="CONFIRMAR PALPITE", style="Arc.TButton", command=verificar_palpite).grid(row=3, column=0, pady=6)

label_resultado = tk.Label(janela, text="Clique em 'Iniciar' para começar.", font=("Courier New", 11), bg="#000", fg="#888")
label_resultado.grid(row=4, column=0, sticky="n", pady=(10, 2))
label_evento = tk.Label(janela, text="", font=("Courier New", 10, "bold"), bg="#000", fg="#FFD700")
label_evento.grid(row=5, column=0, sticky="n")

main_frame = tk.Frame(janela, bg="#000")
main_frame.grid(row=6, column=0, sticky="nsew", padx=10, pady=10)
main_frame.columnconfigure(0, weight=3)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)

barra = ttk.Progressbar(main_frame, orient="horizontal", mode="determinate")
barra.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)

tk.Label(main_frame, text="Histórico de Tentativas:", font=("Courier New", 10, "bold"), bg="#000", fg="#FFDD00").grid(row=1, column=0, sticky="nw")
frame_lista = tk.Frame(main_frame, bg="#000")
frame_lista.grid(row=1, column=0, sticky="nsew")
scroll = tk.Scrollbar(frame_lista)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
lista = tk.Listbox(frame_lista, font=("Courier New", 10), bg="#111", fg="#00FFAA", yscrollcommand=scroll.set, borderwidth=2, relief="sunken")
lista.pack(fill=tk.BOTH, expand=True)
scroll.config(command=lista.yview)

# Painel lateral
side = tk.Frame(main_frame, bg="#000")
side.grid(row=1, column=1, sticky="nsew", padx=(10,0))
lbl_info = tk.Label(side, text="Informações", font=("Courier New", 11, "bold"), bg="#000", fg="#FFD700")
lbl_info.pack(pady=(0,6))
lbl_player = tk.Label(side, text="Jogador: -", font=("Courier New", 10), bg="#000", fg="#AAA", anchor="w")
lbl_player.pack(fill="x")
lbl_mode = tk.Label(side, text="Modo: -", font=("Courier New", 10), bg="#000", fg="#AAA", anchor="w")
lbl_mode.pack(fill="x")
lbl_score = tk.Label(side, text="Pontuação: 0", font=("Courier New", 10), bg="#000", fg="#AAA", anchor="w")
lbl_score.pack(fill="x")
lbl_limits = tk.Label(side, text="Limites: -", font=("Courier New", 10), bg="#000", fg="#00FFAA", anchor="w")
lbl_limits.pack(fill="x", pady=(5,0))

# Rodapé
tk.Label(janela, text="© Lucas Mateus - Ultimate Edition", font=("Courier New", 8), bg="#000", fg="#555").grid(row=8, column=0, pady=10)

# Atualização dinâmica
def atualizar_infos():
    lbl_player.config(text=f"Jogador: {jogador_atual if jogador_atual else '-'}")
    lbl_mode.config(text=f"Modo: {modo_atual if modo_atual else '-'}")
    lbl_score.config(text=f"Pontuação: {pontuacao}")
    lbl_limits.config(text=f"Limites: {limite_inferior} até {limite_superior}")

janela.bind("<Configure>", lambda e: atualizar_infos())
janela.mainloop()
