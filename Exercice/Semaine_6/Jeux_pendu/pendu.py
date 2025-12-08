# Date: 2025-12-01
# Auteur: Émile Valade
# But: Programmer le jeux du pendu
import random

LETTRES = "abcdefghijklmnopqrstuvwxyz"
MOTS = ["pointu", "raser", "ruisseau", "pastorale", "chiens", "cadre", "meteorite", "effacer", "naissance", "facteur"]
MOTS_A_DEVINER = list(random.choice(MOTS))
VIE = 5

nbr_vie = VIE
mot = list("_" * len(MOTS_A_DEVINER))

print(f"Debut du jeux, veuillez deviner un mot au hasard - ({''.join(MOTS_A_DEVINER)})\n")
while(nbr_vie > 0):
    essai = input(f"{''.join(mot)} | vie: {nbr_vie}/{VIE} | (a-z): ").strip()

    if essai in LETTRES:
        if essai in MOTS_A_DEVINER:
           for idx, m in enumerate(MOTS_A_DEVINER):
               if m == essai:
                   mot[idx] = essai
        else:
            if essai == '':
                print("EMPTY INPUT")
                continue
            else:
                nbr_vie -= 1
                continue
    else:
        print("INVALID INPUT")
        continue

    if mot == MOTS_A_DEVINER:
        print(f"{''.join(mot)} | vie: {nbr_vie}/{VIE} | (a-z): {essai}")
        print("Bravo vous avez deviner le mot secret!")
        break

if nbr_vie == 0: 
    print("vous avez perdu!")

