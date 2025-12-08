# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 4 : Conversions imbriquées
# Exercices sur la Conversion Simple et Cast
# Trouve le résultat final de ces conversions :

# Conversions chainées
valeur1 = int(float("12.75"))
valeur2 = str(int(8.999))
valeur3 = bool(int("0"))
valeur4 = float(str(3 + 4.5))

print(f"valeur1 serat de type int (12): {valeur1}, type: {type(valeur1)}")
print(f"valeur2 serat de type str (8): {valeur2}, type: {type(valeur2)}")
print(f"valeur3 serat de type bool (False): {valeur3}, type: {type(valeur3)}")
print(f"valeur4 serat de type float (7.5): {valeur4}, type: {type(valeur4)}")

# Conversions complexes
texte = "15.5 euros"
prix = float(texte.split()[0])
quantite = 3
total = prix * quantite

print(f"total serat de type float (46.5): {total} type: {type(total)}")

