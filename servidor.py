# servidor.py

import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORTA = 6000         # Porta
BUFFER_SIZE = 1024   # Tamanho do buffer (1024 bytes)

# Cria o socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    # Vincular o socket ao endereço e porta
    s.bind((HOST, PORTA))
    
    print(f"Servidor UDP escutando em {HOST}:{PORTA}...")

    while True:
        try:
            # Espera receber dados 
            # data = bytes recebidos, addr = (ip_cliente, porta_cliente)
            data, addr = s.recvfrom(BUFFER_SIZE)
            
            # 1.c: Imprimir a mensagem recebida
            mensagem_recebida = data.decode('utf-8')
            print(f"Mensagem recebida de {addr}: {mensagem_recebida}")
            
            # 1.b: Enviar a mesma mensagem de volta (eco)
            s.sendto(data, addr)
            
        except Exception as e:
            print(f"Ocorreu um erro: {e}")