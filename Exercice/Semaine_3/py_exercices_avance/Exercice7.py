# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 7 : Effets de bord complexes
# Exercices sur les Types Mutables et Immuables
# Prédit le résultat de ce code :

def modifier_data(data1, data2):
    data1[0] = 100
    data2 = "modifié"
    return data2

# Données initiales
liste_originale = [1, 2, 3]
texte_original = "original"

# Appel de fonction
resultat = modifier_data(liste_originale, texte_original)

print("Liste après appel:", liste_originale)
print("Texte après appel:", texte_original)
print("Résultat fonction:", resultat)