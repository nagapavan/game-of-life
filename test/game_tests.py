import os
import unittest
from game_of_life.game_board import GameBoard
from test.test_utils import read_seed_data


class MyTestCase(unittest.TestCase):
    def test_board1(self):
        seed_data = read_seed_data(file_path=os.getcwd() + '/../test_data/game_seed1.txt')
        test_board = GameBoard(board_seed=seed_data, turn_count=20)
        test_board.play()

    def test_board2(self):
        seed_data = read_seed_data(file_path=os.getcwd() + '/../test_data/game_seed2.txt')
        test_board = GameBoard(board_seed=seed_data, turn_count=20)
        test_board.play()


if __name__ == '__main__':
    unittest.main()
