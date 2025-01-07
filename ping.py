import os
import subprocess
import time
from datetime import datetime
import ctypes
import tkinter as tk
from tkinter import messagebox, filedialog
import threading

def impedir_suspensao():
    """Impede que o computador entre em suspensão."""
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

def permitir_suspensao():
    """Permite que o computador entre em suspensão novamente."""
    ES_CONTINUOUS = 0x80000000
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

stop_ping = False  # Variável global para parar o ping

def iniciar_ping(host, intervalo, mtu, log_area, log_path):
    global stop_ping
    try:
        impedir_suspensao()
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_area.insert(tk.END, f"Log será salvo em: {log_file.name}\n")
            while not stop_ping:
                # Comando ping ajustado para Windows
                response = subprocess.run(
                    ["ping", "-n", "1", "-l", str(mtu - 28), host],  # Substitui -s por -l no Windows
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if response.returncode == 0:
                    lines = response.stdout.splitlines()
                    result = f"[{timestamp}] Host {host} está acessível. Resposta: {lines[2] if len(lines) > 2 else 'Sem resposta detalhada.'}"
                else:
                    result = f"[{timestamp}] Erro ao pingar {host}. Mensagem: {response.stderr.strip()}"

                log_area.insert(tk.END, result + "\n")
                log_area.see(tk.END)  # Rola automaticamente para o fim
                log_file.write(result + "\n")
                log_file.flush()
                time.sleep(intervalo)
    except KeyboardInterrupt:
        log_area.insert(tk.END, "\nPing Contínuo Interrompido pelo usuário.\n")
    finally:
        permitir_suspensao()
        log_area.insert(tk.END, f"\nPing interrompido. Arquivo salvo em: {log_path}\n")

def iniciar_interface():
    def executar():
        global stop_ping
        stop_ping = False  # Reseta a variável ao iniciar

        host = host_entry.get()
        intervalo = intervalo_entry.get()
        mtu = mtu_entry.get()

        # Valida o intervalo
        try:
            intervalo = float(intervalo)
            if intervalo <= 0:
                messagebox.showerror("Erro", "Intervalo inválido. Usando padrão de 1 segundo.")
                intervalo = 1
        except ValueError:
            messagebox.showerror("Erro", "Intervalo inválido. Usando padrão de 1 segundo.")
            intervalo = 1

        # Valida o MTU
        try:
            mtu = int(mtu)
            if mtu < 28:
                messagebox.showerror("Erro", "MTU inválido. Usando padrão de 1500 bytes.")
                mtu = 1500
        except ValueError:
            messagebox.showerror("Erro", "MTU inválido. Usando padrão de 1500 bytes.")
            mtu = 1500

        # Abre o gerenciador de arquivos para selecionar o local do log
        log_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
        if not log_path:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado para salvar o log.")
            return

        # Inicia o ping contínuo em uma thread separada
        threading.Thread(target=iniciar_ping, args=(host, intervalo, mtu, log_area, log_path), daemon=True).start()

    def parar():
        global stop_ping
        stop_ping = True
        log_area.insert(tk.END, "\nParando o ping...\n")

    # Janela principal
    janela = tk.Tk()
    janela.title("Ping Contínuo")
    janela.geometry("1100x550")  # Aumenta largura da janela
    janela.resizable(False, False)  # Impede redimensionamento

    # Configuração do layout com grid
    janela.grid_columnconfigure(1, weight=1)  # Permite expansão horizontal
    janela.grid_rowconfigure(3, weight=1)  # Permite expansão vertical

    tk.Label(janela, text="Host:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    host_entry = tk.Entry(janela, width=120)  # Aumenta largura do campo
    host_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(janela, text="Intervalo (em segundos):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    intervalo_entry = tk.Entry(janela, width=120)  # Aumenta largura do campo
    intervalo_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    tk.Label(janela, text="MTU:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    mtu_entry = tk.Entry(janela, width=120)  # Aumenta largura do campo
    mtu_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

    # Área de log
    tk.Label(janela, text="Log:").grid(row=3, column=0, padx=10, pady=5, sticky="nw")
    log_area = tk.Text(janela, height=20, width=120, wrap="none")  # Aumenta largura da área de log
    log_area.grid(row=3, column=1, padx=10, pady=5, sticky="nsew")

    # Botões
    iniciar_btn = tk.Button(janela, text="Iniciar Ping", command=executar)
    iniciar_btn.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    parar_btn = tk.Button(janela, text="Parar", command=parar)
    parar_btn.grid(row=4, column=1, padx=10, pady=10, sticky="w")

    # Executa a interface
    janela.mainloop()

# Inicia a interface gráfica
iniciar_interface()
