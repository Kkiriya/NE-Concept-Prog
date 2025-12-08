# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 14 : Programme de validation
# Écris un programme qui valide des conditions complexes :

# Données d'un utilisateur
age = 25
salaire = 45000
experience = 3
diplome = True

# Conditions pour un prêt
condition1 = age >= 18 and salaire >= 40000
condition2 = experience >= 2 or diplome
condition3 = salaire >= 50000 or (diplome and experience >= 1)

# Validation finale
pret_approuve = condition1 and condition2 and condition3

print("Prêt approuvé:", pret_approuve)