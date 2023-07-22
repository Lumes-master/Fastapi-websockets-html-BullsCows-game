from typing import Optional
from pydantic import BaseModel
from random import sample
from fastapi.encoders import jsonable_encoder



class GameNoAnswer(BaseModel):
    player_try_list: list[str] = []
    bulls_list: list[str] = []
    cows_list: list[str] = []
    message: str = ''

class Game(GameNoAnswer):
    answer: str = None

    @classmethod
    def create_answer(cls) -> str:
        number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        answer = ''.join(sample(number_list, 4))
        return answer

    def reset(self):
        self.answer = self.create_answer()
        self.cows_list, self.bulls_list, self.player_try_list = [], [], []
        self.message = ''
