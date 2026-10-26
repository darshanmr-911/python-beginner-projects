from contextlib import redirect_stdout
from io import StringIO
import unittest
from unittest.mock import patch

from main import parse_guess, play_game


class ParseGuessTests(unittest.TestCase):
    def test_accepts_space_separated_colors_case_insensitively(self):
        self.assertEqual(parse_guess("Red BLUE"), ["red", "blue"])

    def test_accepts_comma_separated_colors(self):
        self.assertEqual(parse_guess("green, yellow"), ["green", "yellow"])

    def test_returns_none_when_player_quits(self):
        self.assertIsNone(parse_guess("Q"))

    def test_rejects_empty_or_unknown_colors(self):
        for answer in ("", "purple", "red purple"):
            with self.subTest(answer=answer):
                with self.assertRaises(ValueError):
                    parse_guess(answer)


class PlayGameTests(unittest.TestCase):
    def test_score_increases_for_each_correct_sequence(self):
        with (
            patch("main.random.choice", side_effect=["red", "blue", "green"]),
            patch(
                "builtins.input",
                side_effect=["red", "red blue", "red blue red"],
            ),
            redirect_stdout(StringIO()),
        ):
            self.assertEqual(play_game(), 2)

    def test_wrong_sequence_ends_the_game(self):
        with (
            patch("main.random.choice", return_value="red"),
            patch("builtins.input", return_value="blue"),
            redirect_stdout(StringIO()),
        ):
            self.assertEqual(play_game(), 0)


if __name__ == "__main__":
    unittest.main()
