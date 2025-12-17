class Animal():
    def __init__(self, nom, age) -> None:
        self.nom = nom 
        self.age = age

    def manger(self):
        print(f"{self.nom} mange")
    
    def dormir(self):
        print(f"{self.nom} dort")
    
    def __str__(self):
        return f"Animal: {self.nom}, age: {self.age}"

    def __eq__(self, value):
        return (self.nom == value.nom) & (self.age == value.age)

    def get_age(self):
        return self.age
    
    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print("age invalide")
    
class Chien(Animal):
    def __init__(self, nom, age, race) -> None:
        Animal.__init__(self, nom, age)
        self.race = race

    def aboyer(self):
        print(f"{self.nom} abboie: Woof!")
    
    def __str__(self):
        # return f"nom: {self.nom}, age: {self.age}, race: {self.race}"
        parent_str = Animal.__str__(self)
        return f"{parent_str}, race: {self.race}"

class Chat(Animal):
    def __init__(self, nom, age, couleur) -> None:
        Animal.__init__(self, nom, age)
        self.couleur = couleur
    
    def miauler(self):
        print(f"{self.nom} miaule: Miaow!")
    
    def __str__(self):
        parent_str = Animal.__str__(self)
        return f"{parent_str}, couleur: {self.couleur}"
    
class Compagon():
    def __init__(self, proprietaire) -> None:
        self.proprietaire = proprietaire

    def jouer(self):
        print(f"Je joue avec {self.proprietaire}")

class AnimalDomestique(Animal, Compagon):
    def __init__(self, nom, age, prorietaire):
        Animal.__init__(self, nom, age)
        Compagon.__init__(self, prorietaire)
    
    def __str__(self):
        animal_str = Animal.__str__(self)
        return f"{animal_str}, prorpietaire: {self.proprietaire}"
        

un_chien = Chien("Fido", 5, "Golden Retriever")
un_chien.manger()
un_chien.dormir()
un_chien.aboyer()
print(un_chien)

print("*"*40)

un_chat = Chat("Gerard", 2, "Noir et Orange")
un_chat.manger()
un_chat.dormir()
un_chat.miauler()
print(un_chat)

print("*"*40)
un_animal_domestique = AnimalDomestique("Achille", 7, "Mathieu")
un_animal_domestique.manger()
un_animal_domestique.dormir()
un_animal_domestique.jouer()
print(un_animal_domestique)


