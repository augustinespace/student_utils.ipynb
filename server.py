import asyncio
import websockets

async def handler(ws, path):
    msg = await ws.recv()
    print("Received in server:", msg)
    await ws.send("ok got it")

start = websockets.serve(handler, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start)
asyncio.get_event_loop().run_forever()
