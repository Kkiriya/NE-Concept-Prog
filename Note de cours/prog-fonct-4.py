liste = [x for x in range(10)]
# print(liste)

li = [5, 8, 7, 96]
# les item de li multp 3
li3 = [x * 3 for x in li]
# print(li, li3)

resultat = ['.' * 3 for i in range(3)]
# print(resultat)

resultat2 = [['.' * 3 for i in range(3)] for j in range(3)]
# print(resultat2)

la_liste = [1,25, 45, 74, 8, 102, 56]
nbr_pair = [x for x in la_liste if x%2 == 0]
# print(nbr_pair)

# Exo 
exo = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

resultat4 = [[i+j*3 for i in range(3)] for j in range(3)]
# print(resultat4)

# Comprehension de dict 
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {cle: value*2 for (cle,value) in dict1.items()}
# print(dict2)

dict3 = {value:cle for (cle,value) in dict1.items()}
print(dict3)

