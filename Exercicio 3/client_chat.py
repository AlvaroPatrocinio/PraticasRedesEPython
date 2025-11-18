import socket
import threading

# Participantes:
# - João Vitor Pinheiro dos Santos
# - Álvaro Patrocínio Leite

# Cliente do chat: envia e recebe mensagens ao mesmo tempo usando threads.


def receber_mensagens(sock):
    """
    Thread para continuamente receber mensagens do servidor.
    """
    while True:
        try:
            mensagem = sock.recv(1024).decode()
            if not mensagem:
                print("[AVISO] Conexão com o servidor encerrada.")
                break

            print(f"\n{mensagem}")

        except:
            print("[ERRO] Não foi possível receber mensagens.")
            break


def enviar_mensagens(sock):
    """
    Thread para enviar mensagens enquanto o programa está rodando.
    """
    while True:
        msg = input()

        if msg.lower() == "sair":
            sock.send(msg.encode())
            print("Você saiu do chat.")
            sock.close()
            break

        sock.send(msg.encode())


def main():
    """
    Conecta no servidor e inicia duas threads: uma para envio e outra
    para recebimento de mensagens.
    """
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 5002))

    print("Conectado ao chat! Digite mensagens. Para sair, use: sair")

    # Thread para receber mensagens
    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    # Thread para enviar mensagens
    enviar_mensagens(cliente)


if __name__ == "__main__":
    main()
