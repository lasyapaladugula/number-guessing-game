# tests/test_game.py
import random
from unittest.mock import patch
from number_guess import play_game

def test_random_number_range():
    for _ in range(100):
        num = random.randint(1, 100)
        assert 1 <= num <= 100
