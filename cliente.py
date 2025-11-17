# cliente.py

import socket

SERVER_HOST = '127.0.0.1' # IP do servidor
SERVER_PORTA = 6000       # Porta do servidor
BUFFER_SIZE = 1024

# Cria o socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    # 3.b: Tratar erros 
    #  timeout de 5 segundos
    s.settimeout(5.0)

    print("Digite 'sair' a qualquer momento para encerrar o cliente.")

    while True:
        # 2.b: envio contínuo
        mensagem = input("Digite a mensagem para enviar ao servidor: ")
        
        if mensagem.lower() == 'sair':
            break
            
        try:
            # Envia a mensagem (codificada em bytes) para o servidor
            s.sendto(mensagem.encode('utf-8'), (SERVER_HOST, SERVER_PORTA))
            
            # resposta
            data_eco, addr = s.recvfrom(BUFFER_SIZE)
            
            # 2.a: Exibir a resposta
            print(f"Eco recebido do servidor: {data_eco.decode('utf-8')}")

        except socket.timeout:
            # 3.b: Tratar tempo limite (se o servidor não responder)
            print("Erro: Tempo limite! O servidor não respondeu em 5 segundos.")
        except Exception as e:
            print(f"Ocorreu um erro na comunicação: {e}")

print("Cliente encerrado.")