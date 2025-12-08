# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 10 : Copie de types mutables
# Écris un programme qui montre la différence 
# entre copie superficielle et référence :

# Liste originale
originale = [1, 2, [3, 4]]

# Référence
reference = originale

# Copie superficielle
copie_superficielle = originale.copy()

# Modification
copie_superficielle[0] = 100
copie_superficielle[2][0] = 300

print("Originale après modifications:", originale)
print("Référence après modifications:", reference)
print("Copie superficielle après modifications:", copie_superficielle)