# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 3 : Expressions complexes

a = 5
b = 3
c = 2
print(f"a = {a}\nb = {b}\nc = {c}\n")


print("Expression 1: ")
#devrait donner 17
resultat1 = a + b * c ** 2
print(f"a + b * c ** 2 = {resultat1}")

print("Expression 2: ")
#devrait donner 32
resultat2 = (a + b) * c ** 2
print(f"(a + b) * c ** 2 = {resultat2}")

print("Expression 3: ")
#devrait donner 8
resultat3 = a * b // c + 1
print(f"a * b // c + 1 = {resultat3}")

print("Expresssion 4: ")
#devrait donner 8
resultat4 = a % b + c * 3
print(f"a % b + c * 3 = {resultat4}")