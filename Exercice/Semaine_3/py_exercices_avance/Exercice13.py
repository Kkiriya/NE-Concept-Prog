# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 13 : Expressions de priorité mixte
# Evalue ces expressions mélangeant différents types d'opérateurs :

# Données de test
x, y, z = 10, 5, 10
a, b = True, False

# Expressions complexes

#devrait donner True
expr1 = x > y and y < z or a and not b
# True and True or True and True
# True or True
# True
print(f"expr1: {expr1}")

#devrait donnner True
expr2 = (x == z) != (y == z) and a or b
# True != False and True
# True and True
# True
print(f"expr2: {expr2}")

#devrait donnner False
expr3 = not (x > y) or (y < z and a) == b
# not True or (True and True) == False
# False or True == False
# True == False 
# False
print(f"expr3: {expr3}")
