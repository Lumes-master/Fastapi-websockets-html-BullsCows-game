from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from starlette.routing import Mount

from game_logic import outer_game_function
# routs = [Mount("/static", StaticFiles(directory="static"), name="static")]

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.websocket("/ws")
async def websocket_bullscow(websocket: WebSocket):
    await websocket.accept()
    game1 = outer_game_function()
    while True:
        data = await websocket.receive_text()
        game = game1(data)
        game_json = jsonable_encoder(game)
        await websocket.send_json(game_json)

@app.get("/", response_class=HTMLResponse)
async def main(request:Request):
    return templates.TemplateResponse('frontpage.html', {'request':request})