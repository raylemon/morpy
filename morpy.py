# IMPORTS
import random

# Jeu à deux joueurs, à tour de rôle
# Joueur 1 utilise "X", Joueur 2 utilise "O"
# AI - Anticiper les coups (plus tard !)
# détecter QUAND la partie se termine -> QUI à gagné (X,O) ou égalité

# VARIABLES "GLOBALES"


LINES = 3


# DÉFINITIONS DE FONCTIONS

def show_board(a_board: list):
    """Affiche un tableau de jeu à l’écran"""  # [[_,_,_], [_,_,_],[_,_,_]]
    """ _ _ _
        _ X _
        _ _ O
    """
    i = 1
    for line in a_board:
        for cell in line:
            if cell == "X" or cell == "O":
                print(cell, end=" ")
            else:
                print(i, end=" ")
            i += 1
        print("")  # passage à la ligne par ici


def is_finished(a_board: list) -> bool:
    """
    Détecte si la partie est terminée
    :param a_board: le tableau de jeu
    :return: True si la partie est terminée, False sinon
    """
    for line in board:
        if "_" in line:
            return False
    return True


def is_horizontal(tbl: list, symbol: str) -> bool:
    pass


def is_vertical(tbl: list, symbol: str) -> bool:
    pass


def is_slash(a_board, symbol: str) -> bool:
    for i in range(len(a_board)):
        if not a_board[i][len(a_board) - i - 1] == symbol:
            return False
    return True
    # return a_board[0][2] == symbol and a_board[1][1] ==symbol and a_board[2][0] == symbol


def is_backslash(a_board, symbol: str) -> bool:
    for i in range(len(a_board)):
        if not a_board[i][i] == symbol:
            return False
    return True

    # return a_board[0][0] == symbol and a_board[1][1] == symbol and a_board[2][2] == symbol


def is_won() -> bool:
    """
    Définit si le jeu est gagné ou non
    :return: True si le jeu est gagné, False sinon
    """
    return is_horizontal() or is_vertical() or is_slash() or is_backslash()


def play(a_board:list, is_player:bool, symbol):
    empties = []
    i = 1
    for line in a_board:
        for cell in line:
            if cell == "_":
                empties.append(i)
            i += 1

    if is_player:
        rep = input(f"Entrez un nombre entre {empties}: ")
        if not rep.isdigit():
            return -1
        else:
            if int(rep) not in empties:
                return - 1
            else:
                return int(rep)

    else: # c’est l’ordinateur
        return random.choice(empties)


# PROGRAMME PRINCIPAL
if __name__ == '__main__':
    board = [["_" for _ in range(LINES)] for _ in range(LINES)]
    show_board(board)
    print(play(board,False,"X"))