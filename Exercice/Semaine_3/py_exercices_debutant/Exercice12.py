# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 12 : Opérateurs d'identité
# Comprends la différence entre == et is :

# Cas 1 : Même valeur, même objet
a = 100
b = 100
resultat1 = a == b
resultat2 = a is b

print(f"a == b = {resultat1}")
print(f"a is b = {resultat2}")

# Cas 2 : Même valeur, objets différents
c = [1, 2, 3]
d = [1, 2, 3]
resultat3 = c == d
resultat4 = c is d

print(f"c == d = {resultat3}")
print(f"c is d = {resultat4}")

# Cas 3 : Petits entiers (interning)
e = 5
f = 5
resultat5 = e is f

print(f"e is f = {resultat5}")

# Cas 4 : Gros entiers
g = 1000
h = 1000
resultat6 = g is h

print(f"g is h = {resultat6}")