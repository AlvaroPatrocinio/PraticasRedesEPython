#!/usr/bin/env python3
# EXERCÍCIO 10 - Chat WebSocket (servidor)
# Participantes: Joao Vitor Pinheiro dos Santos, Alvaro Patrocinio Leite

import asyncio
import websockets
import json

HOST = "0.0.0.0"
PORT = 6789

connected = set()

async def broadcast(message):
    tasks = []
    for ws in connected:
        tasks.append(ws.send(message))
    await asyncio.gather(*tasks, return_exceptions=True)

async def handler(ws):
    connected.add(ws)
    addr = ws.remote_address
    print(f"[+] Cliente conectado: {addr}")

    try:
        async for raw in ws:
            raw = raw.strip()
            if not raw:
                await ws.send(json.dumps({"type": "error", "msg": "Mensagem vazia não permitida"}))
                continue

            # tenta json
            try:
                data = json.loads(raw)
                text = data.get("msg", "").strip()
                name = data.get("name", "Anônimo")
            except:
                text = raw
                name = "Anônimo"

            if not text:
                await ws.send(json.dumps({"type": "error", "msg": "Mensagem vazia não permitida"}))
                continue

            packet = json.dumps({"type": "message", "name": name, "msg": text})
            print(f"[MSG] {addr} -> {name}: {text}")

            await broadcast(packet)

    except websockets.ConnectionClosed:
        print(f"[-] Cliente desconectado: {addr}")
    finally:
        connected.discard(ws)

async def main():
    print(f"Servidor WebSocket rodando em ws://{HOST}:{PORT}")
    async with websockets.serve(handler, HOST, PORT):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())