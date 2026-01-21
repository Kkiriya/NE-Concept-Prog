# Fonction pure: A toujours le meme comportement, Ne change aucun parametre en dehors de son scope

liste = [1, 2, 3]

def doubler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * 2)
    return nouvelle_liste

# print(doubler_liste(liste))
# print(liste)

# Ex 2, elle n'est plus une fonction pure, car elle modifie un element en dehors de son scope
liste = [1, 2, 3]
nouvelle_liste = []

def doubler_liste(une_liste):
    for item in une_liste:
        nouvelle_liste.append(item * 2)
    return nouvelle_liste

# print(doubler_liste(liste))
# print(liste)

# Ex 3, modifie une variables en dehors de son scope donc pas pure
liste = [1, 2, 3]

def doubler_liste(une_liste):
    for index, item in enumerate(une_liste):
        une_liste[index].append(item * 2)
    return une_liste

# print(doubler_liste(liste))
# print(liste)

# 
liste = [1, 2, 3]

def tripler_liste(une_liste):
    nouvelle_liste = []
    for item in une_liste:
        nouvelle_liste.append(item * 3)
    return une_liste

# on retourne une liste avec l'element desirer changer specifiquement
# ici c'est le facteur de multiplication
def multiplier_liste(n):
    def multiplier(une_liste):
        nouvelle_liste = []
        for item in une_liste:
            nouvelle_liste.append(item * n)
        return nouvelle_liste
    
    return multiplier

multiplier_liste_par_2 = multiplier_liste(2)

# print(multiplier_liste_par_2(liste))

# la recursivité
def sum(une_liste):
    total = 0
    for item in une_liste:
        total += item
    return total

# print(sum(liste))

liste = [1, 2, 3]
une_liste2 = [1, 5, 7, 15]

def sum_recursif(une_liste):
    if une_liste:
        return une_liste[0] + sum_recursif(une_liste[1:])
    else:
        return 0
    # return une_liste[0] + sum_recursif(une_liste[1:]) if une_liste else 0
    # return une_liste[0] + sum_recursif(une_liste[1:]) if len(une_liste)>1 else 0
    
print(sum_recursif(une_liste2))
print(sum_recursif(liste))