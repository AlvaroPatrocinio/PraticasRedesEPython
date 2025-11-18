# ---------------------------------------------------------
# Servidor de Hora com Threads (TCP)
# Participantes:
# - João Vitor Pinheiro dos Santos
# - Alvaro Patrocínio Leite
#
# Este servidor escuta na porta 7000 e retorna a hora atual
# para cada cliente conectado. Cada cliente é atendido em
# uma thread separada.
# ---------------------------------------------------------

import socket
import threading
import datetime


# Função que atende cada cliente individualmente
def atender_cliente(conexao, endereco):
    print(f"[LOG] Cliente conectado: {endereco}")

    try:
        # Aguardando solicitação do cliente
        solicitacao = conexao.recv(1024).decode().strip()

        if solicitacao:
            hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
            conexao.send(hora_atual.encode())

            print(f"[LOG] Hora enviada para {endereco}: {hora_atual}")
        else:
            print(f"[LOG] Solicitação vazia recebida de {endereco}")

    except Exception as erro:
        print(f"[ERRO] Falha ao atender {endereco}: {erro}")

    finally:
        conexao.close()
        print(f"[LOG] Conexão encerrada com {endereco}")


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("0.0.0.0", 7000))
    servidor.listen(5)

    print("[SERVIDOR] Servidor de Hora iniciado na porta 7000")

    while True:
        try:
            conexao, endereco = servidor.accept()

            # Criando uma thread para cada cliente
            thread_cliente = threading.Thread(target=atender_cliente, args=(conexao, endereco))
            thread_cliente.start()

        except KeyboardInterrupt:
            print("\n[SERVIDOR] Encerrando servidor manualmente...")
            break

        except Exception as erro:
            print(f"[ERRO] Problema no servidor: {erro}")

    servidor.close()


if __name__ == "__main__":
    main()
