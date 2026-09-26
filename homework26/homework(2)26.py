import websockets, asyncio

client_list = {}

async def broadcast(username,message):
    for client in client_list:
        await client.send(f'{username} : {message}')

async def handler(websocket):
    client_name = input('enter your name')
    client_list[websocket] = client_name
   

    try:
        async for message in websocket:
            print(f"Client: {message}")

            await broadcast(client_list[websocket],message)

    finally:
        client_list.pop(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8500):
        print("Server started...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())