#!/usr/bin/env python3
# ------------------------------------------------------------
# EXERCÍCIO 1 - Servidor TCP
# Participantes:
#   - Joao Vitor Pinheiro dos Santos
#   - Alvaro Patrocinio Leite
#
# Servidor simples utilizando TCP que aceita múltiplos clientes.
# Cada cliente que enviar uma mensagem recebe uma confirmação.
# ------------------------------------------------------------

import socket
import threading

HOST = "0.0.0.0"   # Aceita conexões de qualquer lugar da rede
PORT = 5000        # Porta definida para o exercício


def atender_cliente(conexao, endereco):
    """
    Função que lida com um cliente por vez.
    Roda em uma thread separada para permitir múltiplas conexões.
    """
    print(f"[+] Conexão estabelecida com {endereco}")

    try:
        while True:
            dados = conexao.recv(1024)

            # Se não receber nada, o cliente encerrou a conexão
            if not dados:
                print(f"[-] Cliente {endereco} desconectou")
                break

            mensagem = dados.decode().strip()

            # Validação simples de mensagem vazia
            if mensagem == "":
                conexao.sendall("Mensagem vazia não é permitida.\n".encode())
                continue

            print(f"[{endereco}] Enviou: {mensagem}")

            # Resposta padrão solicitada no enunciado
            conexao.sendall("Mensagem recebida\n".encode())

    except Exception as erro:
        print(f"[ERRO] Problema com o cliente {endereco}: {erro}")

    finally:
        conexao.close()


def main():
    """
    Cria o socket, inicia o servidor e fica aguardando conexões.
    """
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Permite reiniciar o servidor sem esperar a porta "liberar"
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    servidor.bind((HOST, PORT))
    servidor.listen()

    print(f"Servidor ativo na porta {PORT}. Aguardando conexões...")

    try:
        while True:
            conexao, endereco = servidor.accept()

            # Cada cliente é atendido em uma thread
            t = threading.Thread(target=atender_cliente, args=(conexao, endereco))
            t.start()

    except KeyboardInterrupt:
        print("\nServidor encerrado manualmente.")

    finally:
        servidor.close()


if __name__ == "__main__":
    main()
