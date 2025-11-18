#!/usr/bin/env python3
# ------------------------------------------------------------
# EXERCÍCIO 1 - Cliente TCP
# Participantes:
#   - Joao Vitor Pinheiro dos Santos
#   - Alvaro Patrocinio Leite
#
# Cliente simples que conecta ao servidor TCP, envia uma
# mensagem digitada pelo usuário e mostra a resposta.
# ------------------------------------------------------------

import socket

HOST = "127.0.0.1"   # Endereço do servidor (localhost por padrão)
PORT = 5000


def main():
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))
        print("[OK] Conectado ao servidor.")

        mensagem = input("Digite uma mensagem: ").strip()

        # Validação de mensagem vazia
        if mensagem == "":
            print("Não é permitido enviar mensagem vazia.")
            cliente.close()
            return

        cliente.sendall(mensagem.encode())

        resposta = cliente.recv(1024).decode()
        print("Resposta do servidor:", resposta)

    except ConnectionRefusedError:
        print("Erro: o servidor não está ativo ou a porta está errada.")
    except Exception as erro:
        print("Erro inesperado:", erro)
    finally:
        cliente.close()
        print("Conexão encerrada.")


if __name__ == "__main__":
    main()
