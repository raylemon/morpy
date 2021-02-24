import morpy
import pytest

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


def test_show_board(capsys):
    morpy.show_board(empty_board)
    rslt = capsys.readouterr().out  # <= flux de sortie
    assert "1 2 3 \n4 5 6 \n7 8 9 \n" == rslt