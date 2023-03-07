from fastapi import FastAPI, WebSocket
from fastapi.encoders import jsonable_encoder

from game_logic import outer_game_function

app = FastAPI()

@app.websocket("/ws")
async def websocket_bullscow(websocket: WebSocket):
    await websocket.accept()
    game1 = outer_game_function()
    while True:
        data = await websocket.receive_text()
        game = game1(data)
        game_json = jsonable_encoder(game)
        print(game_json)
        await websocket.send_json(game_json)
