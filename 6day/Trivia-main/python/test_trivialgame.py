import io
import random
import sys
import unittest
from unittest import TestCase
from trivia import IGame, GameBetter, Game, Player


class TestGameBetter(TestCase):
    def play_game(self, game: IGame, seed):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            game.add("Chet")
            game.add("Pat")
            game.add("Sue")

            random.seed(seed)
            while True:
                game.rolling(random.randrange(6) + 1)

                if random.randrange(9) == 7:
                    winner = game.wrong_answer()
                else:
                    winner = game.was_correctly_answered()

                if winner:
                    break
        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        return captured_output

    def play_game1(self, game: IGame, seed):
        output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        try:
            game.add(Player("Chet"))
            game.add(Player("Pat"))
            game.add(Player("Sue"))

            random.seed(seed)
            while True:
                game.rolling(random.randrange(6) + 1)

                if random.randrange(9) == 7:
                    game.wrong_answer()
                else:
                    game.was_correctly_answered()

                winner = game.did_player_win()
                if winner:
                    break
                game.change_next_player()

        finally:
            sys.stdout = original_stdout

        captured_output = output.getvalue()
        return captured_output

    def test_characterized(self):
        seed = [1, 100, 1000, 10000, 100000]
        for s in seed:
            with self.subTest(f"{s} seed test"):
                self.assertEqual(
                    self.play_game(Game(), s),
                    self.play_game1(GameBetter(), s),
                )


if __name__ == "__main__":
    unittest.main()
