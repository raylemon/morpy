# IMPORTS

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

def is_finished(a_board: list)-> bool:
    """
    Détecte si la partie est terminée
    :param a_board: le tableau de jeu
    :return: True si la partie est terminée, False sinon
    """


# PROGRAMME PRINCIPAL
if __name__ == '__main__':
    board = [["_" for _ in range(LINES)] for _ in range(LINES)]
    show_board(board)
