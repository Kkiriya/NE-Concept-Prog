# Date: 2025-11-27
# Auteur: Émile Valade
# But: Programmer le jeux Tic Tac Toe


#on cherche a avoir cet affichage 
# . . .
# . . .
# . . . 
# facon simple de le faire mais laisse plasse 
# au faute de frappe 
# map = [
#     [' . ', ' . ', ' . '],
#     [' . ', ' . ', ' . '],
#     [' . ', ' . ', ' . ']
# ]
# a la place on fait

val_nulle = ' . '
val_1 = ' O '
val_2 = ' x '

map = [
    [val_nulle, val_nulle, val_nulle],
    [val_nulle, val_nulle, val_nulle],
    [val_nulle, val_nulle, val_nulle]
]

joueur_en_cours = "Joueur 1"

#on utilise une methode pour afficher la matrice sans avoir 
# a reicrire le code a chauque fois 
def draw():
    for i in range(3):
        for j in range(3):
            print(map[i][j], end="")
        print("")

#fct pour verifier la condition gagante ou egaliter
def check_win():
    #verifie les lignes 
    for i in range(3):
        if map[i][0] == map[i][1] == map[i][2] != val_nulle:
            return True
    
    #verifie les colonnes 
    for j in range(3):
        if map[0][j] == map[1][j] == map[2][j] != val_nulle:
            return True
    
    #verifie les diagonales 
    if map[0][0] == map[1][1] == map[2][2] != val_nulle:
        return True
    if map[0][2] == map [1][1] == map[2][0] != val_nulle:
        return True
    
    return False

# fct pour verifie egalite   
def check_egalite():
    for i in range(3):
        for j in range(3):
            if map[i][j] == val_nulle:
                return False
                
    return True

while True:
    #premier dessin de la map
    draw()
    #demnander au joueur son choix
    # verifier la matrice
    # si un joueur gagne la partie ou egalite --> break
    try:
        entree = int(input(f"{joueur_en_cours} [1-9] ? > "))
    except ValueError:
        print("Veuillez entrez un nombre entre 1 et 9 seulement!!")
        continue

    if entree > 9 or entree < 1:
       print("Veuillez entrez un nombre entre 1 et 9 seulement!!")
       continue 
    # 1 - 9
    # 1 --> 0,0    4 --> 1,0   7 --> 2,0
    # 2 --> 0,1    5 --> 1,1   8 --> 2,1
    # 3 --> 0,2    6 --> 1,2   9 --> 2,2

    # 7//3 = 2 ---- 7-1 mod 3 = 0 ---> 2,0

    ligne = (entree -1 ) // 3 #2
    colonne = (entree - 1) % 3 # 0

    if map[ligne][colonne] != val_nulle:
        print("Erreur: case deja remplie!")
        continue

    if (map[ligne][colonne] == val_nulle):
        map[ligne][colonne] = val_1 if joueur_en_cours == "Joueur 1" else val_2

    #verification de win
    if check_win():
        draw()
        print(f"{joueur_en_cours} à gagné ! ")
        break

    #verification de legalite
    if check_egalite():
        draw()
        print(f"Dommange égalité ! ")
        break


    # a la fin pour changer de joueur juste avant la prochaine iteration
    joueur_en_cours = "Joueur 1" if joueur_en_cours == "Joueur 2" else "Joueur 2"
    