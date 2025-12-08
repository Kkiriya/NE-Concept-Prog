# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 2 : Réécriture avec parenthèses
# Réécris ces expressions en ajoutant toutes les parenthèses implicites :

# Expression originale
expr1 = a + b * c - d / e % f
expr1_2 = ((a + (b * c)) - ((d / e) % f))


# Expression originale
expr2 = not x or y and z
expr2_2 = ((not x) or (y and z))

# Expression originale
expr3 = p ** q ** r * s
expr3_2 = ((p ** (q ** r)) * s)