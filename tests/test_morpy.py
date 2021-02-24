import morpy
import pytest
from io import StringIO

# pip install -U pytest

empty_board = [["_" for _ in range(3)] for _ in range(3)]

win_board_o_hor = [["O", "O", "O"],
                   ["_", "_", "_"],
                   ["_", "_", "_"]]

win_board_o_ver = [["O", "_", "_"],
                   ["O", "_", "_"],
                   ["O", "_", "_"]]

win_board_o_slash = [["_", "_", "O"],
                     ["_", "O", "_"],
                     ["O", "_", "_"]]

win_board_o_backslash = [["O", "_", "_"],
                         ["_", "O", "_"],
                         ["_", "_", "O"]]

win_board_x_hor = [["X", "X", "X"],
                   ["_", "_", "_"],
                   ["_", "_", "_"]]

win_board_x_ver = [["X", "_", "_"],
                   ["X", "_", "_"],
                   ["X", "_", "_"]]

win_board_x_slash = [["_", "_", "X"],
                     ["_", "X", "_"],
                     ["X", "_", "_"]]

win_board_x_backslash = [["X", "_", "_"],
                         ["_", "X", "_"],
                         ["_", "_", "X"]]

win_full_board_x = [["X", "O", "O"],
                    ["O", "X", "O"],
                    ["O", "O", "X"]]

win_full_board_o = [["O", "X", "X"],
                    ["X", "O", "X"],
                    ["X", "X", "O"]]

board_draw = [["X", "O", "X"],
              ["X", "O", "O"],
              ["O", "X", "X"]]

predic_computer_win = [["X", "X", "_"],
                       ["_", "_", "_"],
                       ["_", "_", "_"]]

predic_human_win = [["O", "O", "_"],
                    ["_", "_", "_"],
                    ["_", "_", "_"]]

predic_random = [["X", "O", "_"],
                 ["X", "O", "_"],
                 ["O", "X", "_"]]


@pytest.mark.parametrize("board,result", [
    (empty_board, "1 2 3 \n4 5 6 \n7 8 9 \n"),
    (win_board_o_hor, "O O O \n4 5 6 \n7 8 9 \n"),
    (win_board_x_hor, "X X X \n4 5 6 \n7 8 9 \n"),
    (board_draw, "X O X \nX O O \nO X X \n"),
])
# param 1 : tous les paramètres utilisés
# param 2 : les entrées et  les résultats attendus
def test_show_board(capsys, board, result):
    morpy.show_board(board)
    rslt = capsys.readouterr().out  # <= flux de sortie
    assert result == rslt


@pytest.mark.parametrize("attempt",range(50))
def test_play_computer(attempt):
    rslt = morpy.play(empty_board, is_player=False, symbol="X")
    assert 1 <= rslt <= 9


@pytest.mark.parametrize("attempt",range(50))
def test_play_computer_non_empty(attempt):
    rslt = morpy.play(predic_random, is_player=False, symbol="X")
    assert rslt in [3,6,9]


@pytest.mark.parametrize("attempt",range(50))
def test_play_computer_non_empty_2(attempt):
    rslt = morpy.play(win_board_o_slash, is_player=False, symbol="X")
    assert rslt not in [3,5,7]


def test_play_human(monkeypatch):
    # l’humain tape forcément la touche "6"
    s_in = StringIO("6\n") # <- simulation d’appui de la touche "6"
    monkeypatch.setattr("sys.stdin",s_in)
    rslt = morpy.play(empty_board,is_player=True,symbol="X")

    assert rslt == 6

def test_play_human(monkeypatch):
    # l’humain tape forcément la touche "6"
    s_in = StringIO("4\n") # <- simulation d’appui de la touche "6"
    monkeypatch.setattr("sys.stdin",s_in)
    rslt = morpy.play(predic_random,is_player=True,symbol="X")

    assert rslt == -1
