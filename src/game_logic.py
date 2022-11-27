"""Functions for game logic """
from random import sample
from schemas import Game

def create_answer() -> str:
    """create 4number answer with different digits. Used in
    "outer_game" function """
    number_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
    answer = ''.join(sample(number_list, 4))
    return answer

def verify_try(player_try: str) -> bool:
    """Validating player try-number Used in "game logic" function """
    if len(player_try) == 4 and len(set(player_try)) == 4:
        for i in player_try:
            if i not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return False
        return True
    return False


def check_try(answer: str, player_try: str) -> tuple:
    """compares players_try and answer, returns 2 digits -
    number of good guessed digits and number of them on
    the proper place. Used in 'game_logic' function """
    bulls = 0
    cows = 0
    for i in range(len(player_try)):
        if player_try[i] == answer[i]:
            cows += 1
            bulls += 1
        elif player_try[i] in answer:
            cows += 1
    return str(cows), str(bulls)


def update_game_fields(game: Game, player_try: str) -> Game:
    """Updates instance fields, when player_try is valid"""
    tuple_cowsbulls = check_try(game.answer, player_try)
    game.player_try_list.append(player_try)
    game.bulls_list.append(tuple_cowsbulls[0])
    game.cows_list.append(tuple_cowsbulls[1])
    game.message = ''
    return game



def give_up(game: Game) -> Game:
    game.message = f'Загаданное число - {game.answer}'
    return game

def outer_game_function():
    '''Outer function, that create game instance to be hold
    in inner function'''
    game = Game(answer=create_answer())
    def game_logic (request_value: str) -> Game:
        try:
            if game.cows_list[-1] == '4' or game.message.startswith('Загаданное'):
                game.reset()
        except IndexError:
            pass
        player_try = request_value
        if player_try == 'give up':
            return give_up(game)

        elif not verify_try(player_try):
            game.message = "Число должно содержать 4 неповторяющиеся цифры в диапазоне 1-9"
            return game

        update_game_fields(game, player_try)
        if game.cows_list[-1] == '4':
            game.message = f"Вы вычислили загаданное число - {game.answer}. Поздравляем"
        return game

    return game_logic

# def game_logic(game: Game, request_value: str) -> Game:
#     player_try = request_value
#     if not verify_try(player_try):
#         game.message = "Число должно содержать 4 неповторяющиеся цифры в диапазоне 1-9"
#         return game
#     elif player_try == 'give up':
#         return give_up(game)
#     update_game_fields(game, player_try)
#     if game.cows_list[-1] == '4':
#         game.message = f"Вы вычислили загаданное число - {game.answer}. Поздравляем"
#     return game