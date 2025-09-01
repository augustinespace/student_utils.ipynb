# student_utils.ipynb
# CSV WebSocket Server & Client

## Overview
A WebSocket-based system for transferring and analyzing CSV data between client and server using Python, Pandas, and WebSockets.

## Installation
bash
pip install websockets pandas nest_asyncio


## Project Structure

.
├── server.py
├── client.py
├── students.csv
└── README.md


## Usage

### Start Server
python
# server.py
import asyncio
import websockets
import pandas as pd

async def server_handler(websocket):
    try:
        message = await websocket.recv()
        print("Received CSV data!!")
        
        # Convert JSON back to DataFrame
        df = pd.read_json(message)
        print(df.head())  # Show first 5 rows
        
        await websocket.send("CSV file received and processed!")
    except Exception as e:
        print(f"Server error: {e}")

async def start_server():
    server = await websockets.serve(server_handler, "localhost", 8851)
    print("Server running on ws://localhost:8851")
    return server

# Run server
asyncio.get_event_loop().run_until_complete(start_server())
asyncio.get_event_loop().run_forever()
```

### Run Client
```python
# client.py
import asyncio
import websockets
import pandas as pd

async def client():
    url = "ws://localhost:8851"
    df = pd.read_csv("students.csv")
    data = df.to_json()

    async with websockets.connect(url) as websocket:
        await websocket.send(data)
        reply = await websocket.recv()
        print(f"Server says: {reply}")

asyncio.get_event_loop().run_until_complete(client())
```

## Data Format (students.csv)
csv
id,name,age,grade
1,Monish,21,A
2,Ameer,22,B
3,Lokesh,22,A
4,Divya,21,B
5,Floofy,21,A
6,Augustine,22,A
7,Krupa,21,B
8,Meghana,21,C
9,Simran,21,A
10,Yash,22,A

# Search for specific student
print(disp[disp["name"] == "Floofy"])

# Sort by grade
print(disp.sort_values(by="grade"))


## Output Example

Received CSV data!!
   id    name  age grade
0   1  Monish   21     A
1   2   Ameer   22     B
2   3  Lokesh   22     A
3   4   Divya   21     B
4   5  Floofy   21     A

Server says: CSV file received and processed!
