# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 1 : Décomposition d'expressions complexes
# Exercices sur les Opérateurs, Précédence et Associativité
# Écris les étapes intermédiaires de calcul pour ces expressions :

# Expression 1
resultat1 = 3 + 4 * 2 ** 3 // 2 - 1
print("3 + 4 * 8 // 2 - 1")
print("3 + 32 // 2 - 1")
print("3  + 16 - 1")
print("18")
print(f"resultat1 = {resultat1}")

# Expression 2
a, b, c = 5, 3, 2
resultat2 = a % b + c * (a // b) ** c
print("5 % 3 + 2 * (5 // 3) ** 2")
print("2 + 2 * 1 ** 2")
print("2 + 2 * 1")
print("2 + 2")
print("4")
print(f"resultat2 = {resultat2}")


# Expression 3
x, y, z = 8, 3, 2
resultat3 = (x > y and y < z) or (x == y * z)
print("(8 > 3 and 3 < 2) or (8 == 3 * 2)")
print("(True and False) or (8 == 6)")
print("False or False")
print("False")
print(f"resultat3 = {resultat3}")