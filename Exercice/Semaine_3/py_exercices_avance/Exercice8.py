# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 8 : Copies profondes vs superficielles
# Analyse ce code et explique les résultats :
import copy

# Structure complexe
donnees_complexes = [
    [1, 2, 3],
    {"a": 10, "b": [4, 5]},
    (6, 7, [8, 9])
]

# Différentes copies
ref = donnees_complexes
copie_simple = donnees_complexes.copy()
copie_profonde = copy.deepcopy(donnees_complexes)

# Modifications
ref[0][0] = 100
ref[1]["b"][0] = 400
# ref[2][2][0] = 800  # Pourquoi cette ligne génère une erreur ?
# car [2] est un tuple et il sont immuables

print("Original:", donnees_complexes[0][0], donnees_complexes[1]["b"][0])
print("Copie simple:", copie_simple[0][0], copie_simple[1]["b"][0])
print("Copie profonde:", copie_profonde[0][0], copie_profonde[1]["b"][0])