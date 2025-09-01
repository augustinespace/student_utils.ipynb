#server
import asyncio
import websockets
import pandas as pd
import json

async def server_handler(websocket):
    try:
        message = await websocket.recv()
        print("Received CSV data !!")

        # Convert JSON string back into DataFrame
        df = pd.read_json(message)
        print(df.head())   # show first 5 rows

        await websocket.send("CSV file received and processed!")
    except Exception as e:
        print("Server error:", e)

async def start_server():
    server = await websockets.serve(server_handler, "localhost", 8851)  # changed port
    print("Server running on ws://localhost:8851")
    return server

server = await start_server()
