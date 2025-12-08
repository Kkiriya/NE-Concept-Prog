# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 6 : Gestion des erreurs de conversion
# Écris un programme qui gère les erreurs de conversion :

valeurs = ["123", "45.67", "abc", "789", "12.34.56"]

for valeur in valeurs:
    try:
        # Essayer de convertir en float
        resultat = float(valeur)
        print(f"Conversion réussie: {valeur} -> {resultat}")
    except ValueError:
        print(f"Erreur: impossible de convertir '{valeur}' en nombre")