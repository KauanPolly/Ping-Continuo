import subprocess
import time
from datetime import datetime
import ctypes

def impedir_suspensao():
    """Impede que o computador entre em suspensão."""
    ES_CONTINUOUS = 0x80000000
    ES_SYSTEM_REQUIRED = 0x00000001
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)

def permitir_suspensao():
    """Permite que o computador entre em suspensão novamente."""
    ES_CONTINUOUS = 0x80000000
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)

def ping_continuo():
    host = input("Digite o Host, Para ser Pingado: ")
    intervalo = input("Digite o intervalo (em segundos): ")
    mtu_entrada = input("Digite o tamanho da MTU: ")

    # Valida o intervalo
    try:
        intervalo = float(intervalo)
        if intervalo <= 0:
            print("Intervalo Inválido. Usando padrão de 1 segundo.")
            intervalo = 1
    except ValueError:
        print("Intervalo Inválido. Usando padrão de 1 segundo.")
        intervalo = 1

    # Valida o MTU
    try:
        mtu = int(mtu_entrada)
        if mtu < 28:
            print("MTU inválido. Usando padrão de 1500 bytes.")
            mtu = 1500
    except ValueError:
        print("MTU inválido. Usando padrão de 1500 bytes.")
        mtu = 1500

    try:
        impedir_suspensao()
        print(f"Iniciando o Ping Contínuo para {host} com MTU={mtu}. Pressione CTRL+C para parar.")
        with open("ping_log.txt", "a") as log_file:
            while True:
                # Comando ping ajustado para Windows
                response = subprocess.run(
                    ["ping", "-n", "1", "-l", str(mtu - 28), host],  # Substitui -s por -l no Windows
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if response.returncode == 0:
                    result = f"[{timestamp}] Host {host} está acessível. Resposta: {response.stdout.splitlines()[2]}"
                    print(result)
                else:
                    result = f"[{timestamp}] Erro ao pingar {host}. Mensagem: {response.stderr.strip()}"
                    print(result)
                
                log_file.write(result + "\n")
                log_file.flush()
                time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nPing Contínuo Interrompido pelo usuário.")
    finally:
        permitir_suspensao()

# Executa o programa
ping_continuo()
