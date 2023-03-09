import pytest
from fastapi.testclient import TestClient
from schemas import Game
from game_logic import verify_try_is_correct, check_try
from main import app

client = TestClient(app)

@pytest.mark.parametrize('arg, res', [
    ('1234', True),
    ('9876', True),
    ('0987', False),
    ('', False),
    ('123', False),
    ('12345', False),
    ('9978', False)
]

)
def test_verify_try_is_correct(arg, res):
    assert verify_try_is_correct(arg) == res

@pytest.mark.parametrize('answer, player_try, answer_tuple', [
    ('1234', '1234', ('4', '4')),
    ('1234', '5678', ('0', '0')),
    ('1234', '1243', ('4', '2')),
    ('1234', '2178', ('2', '0')),
('1234', '1327', ('3', '1'))

])
def test_check_try(answer, player_try, answer_tuple):
    assert check_try(answer, player_try) == answer_tuple



