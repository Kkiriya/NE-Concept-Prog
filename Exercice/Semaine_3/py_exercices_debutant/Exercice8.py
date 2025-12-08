# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 8 : Manipulation des types mutables
# Observe le comportement des types mutables :

# Liste (mutable)
liste1 = [1, 2, 3]
liste2 = liste1
liste2.append(4)

print("Liste1 après modification de liste2:", liste1)

# Dictionnaire (mutable)
dict1 = {"a": 1, "b": 2}
dict2 = dict1
dict2["c"] = 3

print("Dict1 après modification de dict2:", dict1)