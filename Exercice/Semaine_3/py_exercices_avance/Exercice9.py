# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 9 : Performance des types
# Compare l'efficacité mémoire des différents types :
import sys

# Création de différentes structures
entier = 1000000
chaine = "A" * 1000
liste = ["A"] * 1000
tuple_data = ("A",) * 1000

# Compare la taille mémoire
print(f"Int: {sys.getsizeof(entier)} octets")
print(f"String: {sys.getsizeof(chaine)} octets")
print(f"Liste: {sys.getsizeof(liste)} octets")
print(f"Tuple: {sys.getsizeof(tuple_data)} octets")
