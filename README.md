# BullsCows logical game.
Guess given 4-digit number with your tries
Backend - Fastapi, Fastapi websocket.
Frontend - html.

To run app: 
- Run in terminal: uvicorn main:app --reload
- Open frontend.html in browser add print 4-digit number in input field.
- Server will answer with JSON-data, including correct answer, 
player_try list, bulls list, cows list and message.

To give up and reload the game type 'give up' in input field.
If you gave the right answer, the game will reload automaticaly.
Also you can reload the game by reloading the html page.

To implement frontend you should creaete table for lists and 
message (if exists). And parse json response.

![Python](https://img.shields.io/badge/python-v3.10-yellowblue)![FastApi](https://img.shields.io/badge/fastapi-v0.85.1-green)
