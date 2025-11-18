import socket
import threading

# Participantes:
# - João Vitor Pinheiro dos Santos
# - Álvaro Patrocínio Leite

# Servidor do chat: recebe mensagens de um cliente e envia para o outro.
# Aceita exatamente 2 clientes.


clients = []   # Lista para armazenar os dois clientes conectados


def handle_client(client_socket, client_address):
    """
    Função que escuta mensagens do cliente e repassa para o outro cliente.
    Roda em uma thread para cada cliente.
    """

    try:
        while True:
            mensagem = client_socket.recv(1024).decode().strip()

            # Cliente desconectou ou digou "sair"
            if not mensagem or mensagem.lower() == "sair":
                print(f"[AVISO] Cliente {client_address} saiu do chat.")
                client_socket.close()
                clients.remove(client_socket)
                break

            print(f"[{client_address}] {mensagem}")

            # Repassa a mensagem para o outro cliente
            for c in clients:
                if c != client_socket:
                    c.send(f"{client_address}: {mensagem}".encode())

    except Exception as e:
        print(f"[ERRO] Problema com {client_address}: {e}")
        if client_socket in clients:
            clients.remove(client_socket)
        client_socket.close()


def main():
    """
    Inicializa o servidor, aceita exatamente dois clientes e cria
    uma thread para cada um.
    """

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 5002))
    servidor.listen(2)

    print("[SERVIDOR] Aguardando 2 clientes para iniciar o chat...")

    while len(clients) < 2:
        client_socket, address = servidor.accept()
        print(f"[CONECTADO] Cliente conectado: {address}")
        clients.append(client_socket)

        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

    print("[SERVIDOR] Chat iniciado. Os dois clientes podem conversar.")


if __name__ == "__main__":
    main()
