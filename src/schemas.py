from typing import Optional
from pydantic import BaseModel
from random import sample
from fastapi.encoders import jsonable_encoder


def create_game_answer() -> str:
    """create 4number answer with different digits. Used in
    "creating_new_game" function """
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    answer = ''.join(sample(number_list, 4))
    return answer


class Game(BaseModel):
    answer: str | None = None
    player_try_list: list[str] = []
    bulls_list: list[str] = []
    cows_list: list[str] = []
    message: str = 'Hello'

    def reset(self):
        self.answer = create_game_answer()
        self.cows_list, self.bulls_list, self.player_try_list = [], [], []
