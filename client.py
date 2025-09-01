#client
import asyncio
import websockets
import pandas as pd

async def client():
    uri = "ws://localhost:8851"

    df = pd.read_csv("students.csv")
    data = df.to_json()

    async with websockets.connect(uri) as websocket:
        await websocket.send(data)
        reply = await websocket.recv()
        print(f"Server says: {reply}")

await client()
