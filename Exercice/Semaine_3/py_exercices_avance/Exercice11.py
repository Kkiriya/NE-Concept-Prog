# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 11 : Comparaisons chainées
# Évalue ces comparaisons chainées :

# Comparaisons multiples
a, b, c, d = 5, 10, 5, 20

# devrait donner False
resultat1 = a < b < c < d
# ici python fait encore un foit:
# (a < b) and (b < c) and (c < d)
# True and False and True
# False 

#devrait donner True
resultat2 = a == c != b < d
# (a == c) and (c != b) and (b < d)
# True and True and True
# True

# devrait donner True
resultat3 = a <= c == 5 != b
# (a <= c) and (c == 5) and (5 != b)
# True and True and True
# True

print(f"resultat1: {resultat1}\nresulta2: {resultat2}\nresultat3: {resultat3}")