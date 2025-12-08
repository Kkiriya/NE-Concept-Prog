# Date: 2025-11-05
# Auteur: Émile Valade
# But: remplir les trous
"""
CALCULATRICE SIMPLE
Programme : Effectue des opérations basiques
Auteur : [Ton nom]
Date : [Date]
"""

# Demander deux nombres à l'utilisateur
nombre1 = float(input("Entrez le premier nombre: "))
nombre2 = float(input("Entrez le deuxième nombre: "))

# Afficher les résultats des opérations
print("Addition: ", nombre1 + nombre2)
print("Soustraction: ", nombre1 - nombre2)
print("Multiplication: ", nombre1 * nombre2)
if nombre2 != 0:
    print("Division: ", nombre1 / nombre2)
else:
    print("Division: Impossible de diviser par zéro")