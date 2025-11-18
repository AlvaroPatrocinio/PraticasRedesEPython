#!/usr/bin/env python3
# EXERCÍCIO 10 - Cliente CLI WebSocket
# Participantes: Joao Vitor Pinheiro dos Santos, Alvaro Patrocinio Leite

import asyncio
import websockets
import json

HOST = "ws://192.168.3.14:6789"

async def receiver(ws):
    async for msg in ws:
        try:
            data = json.loads(msg)
            if data.get("type") == "message":
                print(f"{data.get('name')}: {data.get('msg')}")
            elif data.get("type") == "error":
                print("[ERRO]", data.get("msg"))
            else:
                print(msg)
        except:
            print(msg)

async def main():
    name = input("Nome: ").strip() or "Anônimo"
    loop = asyncio.get_running_loop() # Pega o loop atual
    
    try:
        async with websockets.connect(HOST) as ws:
            print("Conectado. Digite mensagens (CTRL+C para sair).")
            recv_task = asyncio.create_task(receiver(ws))
            
            # Loop de envio
            while True:
                try:
                    text = await loop.run_in_executor(None, input) 
                    
                except EOFError:
                    break
                
                # ... (Restante da sua lógica de tratamento de texto)
                text = text.strip()
                if not text:
                    print("Mensagem vazia não pode ser enviada.")
                    continue
                
                packet = {"name": name, "msg": text}
                await ws.send(json.dumps(packet))
                
            recv_task.cancel()
    except ConnectionRefusedError:
        print("Servidor indisponível.")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nSaindo.")
