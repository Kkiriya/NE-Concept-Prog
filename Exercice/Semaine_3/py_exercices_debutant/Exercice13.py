# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 13 : Expressions booléennes complexes
# value ces expressions complexes :

x = 10
y = 5
z = 10

# Expression 1
resultat1 = x > y and x == z
# True and True 
# devrait donner True
print(f"(x > y and x == z) = {resultat1}")

# Expression 2
resultat2 = x < y or x == z
# False or True
# devrait donner True
print(f"(x < y or x == z) = {resultat2}")

# Expression 3
resultat3 = not (x == y)
# not False
# devrait donner True
print(f"(not (x == y)) = {resultat3}")

# Expression 4
resultat4 = x > y and x != z or y < z
# True and False or True
# True and True 
# devrait donner True
print(f"(x > y and x != z or y < z) = {resultat4}")

# Expression 5
resultat5 = (x > y and x != z) or y < z
# (True and False) or True
# False or True 
# devrait donner True
print(f"((x > y and x != z) or y < z) = {resultat5}")