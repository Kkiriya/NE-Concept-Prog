# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 1 : Calculs avec précédence
# Exercices sur les Opérateurs, Précédence et Associativité

print("Expression 1: ")
#devrait donner 16
resultat1 = 10 + 3 * 2 
print(f"10 + 3 * 2 = {resultat1}")

print("Expression 2: ")
#devrait donner 26
resultat2 = (10 + 3) * 2
print(f"(10 + 3) * 2 = {resultat2}")

print("Expression 3: ")
#devrait donner  13
resultat3 = 15 - 4 / 2
print(f"15 - 4 / 2 = {resultat3}")

print("Expression 4: ")
#devrait donner 5.5
resultat4 = (15 - 4) / 2
print(f"(15 - 4) / 2 = {resultat4}")

print("Expression 5: ")
#devrait donner 16
resultat5 = 2 ** 3 * 2
print(f"2 ** 3 * 2 = {resultat5}")

print("Expression 6: ")
#devrait donner 64
resultat6 = 2 ** (3 * 2)
print(f"2 ** (3*2) = {resultat6}")
