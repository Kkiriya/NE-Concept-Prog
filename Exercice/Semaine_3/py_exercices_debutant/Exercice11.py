# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 11 : Opérateurs de comparaison
# Exercices sur les Opérateurs de Comparaison et d'Identité
# Prédit le résultat de ces comparaisons :

# Comparaisons numériques
a = 10
b = 5
c = 10

resultat1 = a > b
resultat2 = a == c
resultat3 = a != b
resultat4 = a <= c
resultat5 = b >= a

#devrait donner True
print(f"a > b = {resultat1}")

#devrait donner True
print(f"a == c = {resultat2}")

#devrait donner True
print(f"a != b = {resultat3}")

#devrait donner True
print(f"a <= c = {resultat4}")

#devrait donner False
print(f"b >= a = {resultat5}")

# Comparaisons de strings
texte1 = "abc"
texte2 = "abd"
texte3 = "abc"

resultat6 = texte1 == texte3
resultat7 = texte1 < texte2
resultat8 = texte1 != texte2

#devrait donner True
print(f"texte1 == texte3 = {resultat6}")

#devrait donner True
print(f"texte1 < texte2 = {resultat7}")

#devrait donner True
print(f"texte1 != texte2 = {resultat8}")