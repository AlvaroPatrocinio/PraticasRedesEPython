# ---------------------------------------------------------
# Cliente de Solicitação de Hora (TCP)
# Participantes:
# - João Vitor Pinheiro dos Santos
# - Alvaro Patrocínio Leite
#
# Este cliente conecta ao servidor na porta 7000, solicita
# a hora atual e exibe a resposta no console.
# ---------------------------------------------------------

import socket


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(("127.0.0.1", 7000))  # Ajuste o IP se o servidor estiver em outra máquina
        cliente.send("HORA".encode())

        resposta = cliente.recv(1024).decode()
        print(f"Hora recebida do servidor: {resposta}")

    except Exception as erro:
        print(f"[ERRO] Não foi possível conectar ao servidor: {erro}")

    finally:
        cliente.close()


if __name__ == "__main__":
    main()
