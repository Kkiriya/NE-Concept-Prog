# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercices sur la Conversion Simple et Cast
# Exercice 4 : Conversions de base
# Complète le code suivant avec les conversions appropriées :

print("Conversion de string vers entier: ")

texte_nombre = "123"
nombre_entier = int(texte_nombre)
print(f"typeOf texte_nombre ({texte_nombre}) = {type(texte_nombre)}")
print(f"typeOf nombre_entier ({nombre_entier}) = {type(nombre_entier)}\n")

print("Conversion de string vers float: ")
texte_decimal = "45.67"
nombre_decimal = float(texte_decimal)
print(f"typeOf texte_decimal ({texte_decimal}) = {type(texte_decimal)}")
print(f"typeOf nombre_decimal ({nombre_decimal}) = {type(nombre_decimal)}\n")

print("Conversion de float vers entier: ")
prix = 99.99
prix_entier = int(prix)
print(f"typeOf prix ({prix}) = {type(prix)}")
print(f"typeOf prix_entier ({prix_entier}) = {type(prix_entier)}\n")

print("Conversion de booléen vers entier: ")
vrai = True
faux = False
vrai_entier = int(vrai)
faux_entier = int(faux)
print(f"typeOf vrai ({vrai}) = {type(vrai)}")
print(f"typeOf vrai_entier ({vrai_entier}) = {type(vrai_entier)}\n")
print(f"typeOf faux ({faux}) = {type(faux)}")
print(f"typeOf faux_entier ({faux_entier}) = {type(faux_entier)}\n")