# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 10 : Tables de vérité complexes
# Exercices sur les Opérateurs de Comparaison et d'Identité
# Complète la table de vérité pour ces expressions :

# Pour a = True, b = False, c = True
a = True
b = False
c = True

expression1 = not a or b and c
# not a = False 
# b and c = False
# (not a) or (b and c) = False
print(f"Table de vérité de l'expression: not a or b and c:\n\n")
print(f"a = {a}\nb = {b}\nc = {c}\nnot a = {not a}\nb and c = {b and c}\n(not a) or (b and c) = {(not a) or (b and c)}")
print(f"evaluation de l'expression: {expression1}\n\n")

expression2 = (not a) or (b and c)
# not a = False
# b and c = False
# (not a) or (b and c) = False
print(f"Tabe de vérité de l'expression: (not a) or (b and c):\n\n")
print(f"not a = {not a}\nb and c = {b and c}\n(not a) or (b and c) = {(not a) or (b and c)}")
print(f"evalutaion de l'expression: {expression2}\n\n")


expression3 = not (a or b) and c
# a or b = True
# not (a or b) = False
# not (a or b) and c = False
print(f"evaluation de l'expression 3: {expression3}")

expression4 = a != b == c
#apparament python ici fait ceci: 
# (a != b) and (b == c)
# (a != b) = True
# (b == c) = False 
# (a != b) and (b == c) = False
print(f"evalutaion de l'expression 4: {expression4}")
