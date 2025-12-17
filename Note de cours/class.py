class  User(): #PascalCase
    #variables globale possible
    ban = False

    def __init__(self, name="john", email="jbloodborne@gmail.com", age=20) -> None: #Constructeur de la classe
    #s'execute a l'instanciation de la classes'
        self.name = name #self est l'equivalent de this en java
        self.email = email
        self.age = age

    #pour voir/acceder au donner de la classe
    def printSelf(self):
        fstr = f"- Nom: {self.name}\n- Email:{self.email}\n- Age:{self.age}"
        print(fstr)

    def _say_hi(self):
        print("Oh hi!")

    def bonjour(self, short:bool=False) -> bool:
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.name}.")
        return short
    
    def say_hi(self):
        print("Oh hi !")

    

    
    #pour retourner une nouvelle instance avec des arguments predifinis 
    @classmethod
    def another_constructor(cls):
        return cls("Unkown", "unkown", 0)

    @staticmethod #utilisable sans avoir a declarer une instance 
    def is_ban(a):
        return a.age <= 16

#instancier class
a = User() # Insrance de la classe
print(a.name)
print(a.email)
print(a.age)

b = User(name="John", email="jbloodborne22@gmail.com", age=22)
print(b.name)
print(b.email)
print(b.age)
b.printSelf()

c = User("Bloodborne")
c.bonjour()

d = User("Bob", "bsouls@gmail.com", 42)
d.bonjour()

e = User.another_constructor()
e.bonjour()

print(User.is_ban(d))

r = User("Bob", "bob@gmail.com", 16)
r.say_hi()
# r.say_hi() = "aahahhhahhhh" #ceci ecrase la methode et la remplace par une chaine de string
r._say_hi() #_ veux dire methode priver, ne doit pas etre appeler vers l'exterieure, elle est pour la classe uniquement
r.bonjour(True)

#pour voir tous les details d'une instance
print(dir(r))