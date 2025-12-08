# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 9 : Comportement des types immuables
# Observe le comportement des types immuables :

# String (immuable)
texte1 = "hello"
texte2 = texte1
texte2 = texte2 + " world"

print("Texte1 après opération sur texte2:", texte1)
print("Texte2: " + texte2)

# Tuple (immuable)
tuple1 = (1, 2, 3)
tuple2 = tuple1
tuple2[0] = 4  # Cette ligne générera une erreur