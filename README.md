# Ping-Continuo


# Ping Contínuo com Log

Este projeto contém dois scripts em Python que permitem realizar pings contínuos a um host, registrando os resultados em um arquivo de log. Uma das versões utiliza uma interface gráfica, enquanto a outra é baseada em linha de comando.

## Funcionalidades

### Versão com Interface Gráfica
- **Ping Contínuo:** Realize pings para um host com intervalo configurável.
- **Configuração de MTU:** Ajuste o tamanho do pacote ICMP.
- **Logs em Tempo Real:** Exibição dos resultados diretamente na interface e registro em arquivo de texto.
- **Evitar Suspensão do Sistema:** O sistema não entra em suspensão enquanto o programa estiver em execução.
- **Interface Gráfica:** Fácil de usar, construída com `tkinter`.
- **Execução em Thread:** Mantém a interface responsiva mesmo durante o ping contínuo.

### Versão sem Interface Gráfica
- **Ping Contínuo:** Realize pings para um host com intervalo configurável.
- **Configuração de MTU:** Ajuste o tamanho do pacote ICMP.
- **Logs Salvos em Arquivo:** Resultados são gravados no arquivo `ping_log.txt`.
- **Evitar Suspensão do Sistema:** O sistema não entra em suspensão enquanto o programa estiver em execução.
- **Baseada em Linha de Comando:** Simples e funcional, sem necessidade de interface gráfica.

## Requisitos

- **Sistema Operacional:** Windows
- **Python:** 3.6 ou superior
- **Bibliotecas Necessárias:**
  - `subprocess` (incluso no Python)
  - `ctypes` (incluso no Python)
  - `time` (incluso no Python)
  - `datetime` (incluso no Python)
  - Para a versão gráfica: `tkinter` (incluso no Python)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/KauanPolly/Ping-Continuo.git



# Continuous Ping with Logging

This project includes two Python scripts that allow you to perform continuous pings to a host, logging the results into a file. One version uses a graphical interface, while the other is command-line-based.

## Features

### Version with Graphical Interface
- **Continuous Ping:** Perform continuous pings to a host with configurable intervals.
- **MTU Configuration:** Adjust the ICMP packet size.
- **Real-Time Logs:** Display results directly in the interface and save them to a text file.
- **Prevent System Suspension:** Keeps the system from entering suspension while the program is running.
- **Graphical Interface:** User-friendly, built with `tkinter`.
- **Threaded Execution:** Keeps the interface responsive during the continuous ping process.

### Version without Graphical Interface
- **Continuous Ping:** Perform continuous pings to a host with configurable intervals.
- **MTU Configuration:** Adjust the ICMP packet size.
- **Logs Saved to File:** Results are logged into the `ping_log.txt` file.
- **Prevent System Suspension:** Keeps the system from entering suspension while the program is running.
- **Command-Line Based:** Simple and functional, no graphical interface required.

## Requirements

- **Operating System:** Windows
- **Python:** 3.6 or higher
- **Required Libraries:**
  - `subprocess` (built-in Python library)
  - `ctypes` (built-in Python library)
  - `time` (built-in Python library)
  - `datetime` (built-in Python library)
  - For the graphical version: `tkinter` (built-in Python library)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KauanPolly/Ping-Continuo.git

