# IMPORTS

# création d’un tableau 3*3
# Jeu à deux joueurs, à tour de rôle
# Joueur 1 utilise "X", Joueur 2 utilise "O"
# AI - Anticiper les coups (plus tard !)
# Interface Graphique (plus tard)
# tableaux plus grands (plus tard)
# gagner avec des lignes plus grandes (plus tard)
# détecter QUAND la partie se termine -> QUI à gagné (X,O) ou égalité

# VARIABLES "GLOBALES"
LINES = 3

# DÉFINITIONS DE FONCTIONS

def show_board(a_board:list):
    """Affiche un tableau de jeu à l’écran""" # [[_,_,_], [_,_,_],[_,_,_]]
    """ _ _ _
        _ X _
        _ _ O
    """
    i = 1
    for line in a_board:
        for cell in line:
            print(i,end="")
            i+=1
        print("") # passage à la ligne par ici


# PROGRAMME PRINCIPAL
if __name__ == '__main__':
    board = [["_" for _ in range(LINES)] for _ in range(LINES)]
    show_board(board)