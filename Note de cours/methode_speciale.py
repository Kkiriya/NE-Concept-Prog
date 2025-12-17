class User():
    ban = False

    def __init__(self, nom, email, age, notes) -> None:
        if age <16:
            self.ban = True
        self.nom = nom
        self.email = email
        self.age = age
        self.notes = notes
    
    def _say_hi(self):
        print("Bonjour")

    def bonjour(self,short: bool = False):
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.nom} !")
    
    def __str__(self): #surcharge de la methode par defaut pour afficher celle-ci
        return f"nom: {self.nom}\nemail: {self.email}\nage: {self.age}"
    
    def __eq__(self, value):
        return (self.nom == value.nom) & (self.email == value.email) & (self.age == value.age)
    
    def __call__(self, *args, **kwds):
        print(f"{self.nom} est executer")

    def __getitem__(self, cle):
        print(f"La réponse est  {self.notes[cle]}")

user = User("Bob", "bobds@email.com", 24, [82, 98, 34])
user2 = User("Bob", "bobds@email.com", 24, [82, 98, 34])

# print(dir(user))
# print(user.__dir__())
# print(user.__dict__) # renvoie un dict de l'instance de lobjet

# num = 45
# print(num.__add__(12))

print(user.__str__())
# print(user.__eq__(user2)) # est appeller avec → ==
print(user == user2)

user() #fait appell a une fonction __call__

user[2] #doesnt work :/ ? 