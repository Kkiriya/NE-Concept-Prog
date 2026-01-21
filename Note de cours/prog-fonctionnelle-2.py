une_liste = [1, 5, 7, 84, 52, 43]

def map_by(une_liste, une_fonction):
    new_liste = []
    for item in une_liste:
        new_liste.append(une_fonction(item))
    return new_liste

def multiplier_item(factor):
    def multiplier(item):
        return item * factor
    return multiplier

double = multiplier_item(2)
triple = multiplier_item(3)
quadruple = multiplier_item(4)
quintuple = multiplier_item(5)

# print(map_by(une_liste, double))
# print(map_by(une_liste, triple))
# print(map_by(une_liste, quadruple))
# print(map_by(une_liste, quintuple))

#map 
# print(list(map(double, une_liste)))

#filter
une_liste2 = [1, 5, 7, 84, 52, 43]

def is_pair(item):
    return item % 2 == 0

# print(list(filter(is_pair, une_liste2)))
# print(set(filter(is_pair, une_liste2)))
# print(tuple(filter(is_pair, une_liste2)))

def is_maj(item):
    return item >= 18

# print(list(filter(is_maj, une_liste2)))
# print(set(filter(is_maj, une_liste2)))
# print(tuple(filter(is_maj, une_liste2)))

#zip
une_liste_a = [1, 2, 3]
une_liste_b = ['a', 'b', 'c']
print(list(zip(une_liste_a, une_liste_b))) # strict = True, ne laisse passer que les liste de la meme taille

une_liste_c = ["ID", "Name", "email", "passwd"]
une_liste_d = ["12345", "John Doe", "jd@email.com", "jd12345"]
print(dict(zip(une_liste_c, une_liste_d, strict=True)))