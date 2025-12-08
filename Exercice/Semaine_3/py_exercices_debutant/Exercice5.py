# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 5 : Conversions avec input
# Écris un programme qui demande deux nombres à l'utilisateur
#  et effectue différentes conversions :

nombre1 = input("Entrez le premier nombre : ")
nombre2 = input("Entrez le deuxième nombre : ")

# Convertir en entiers et calculer la somme
somme = int(nombre1) + int(nombre2)

# Convertir en floats et calculer la moyenne
moyenne = (float(nombre1) + float(nombre2)) / 2

# Convertir en strings et créer un message
message = "Voici le nombre 1: (" + str(nombre1) + ") et le nombre 2: (" + str(nombre2) + ")"

print(f"somme: {somme}\nmoyenne: {moyenne}\nmessage: {message}")