class User():
    ban = False

    def __init__(self, nom, email, age) -> None:
        if age <16:
            self.ban = True
        self.nom = nom
        self.email = email
        self.age = age
    
    def _say_hi(self):
        print("Bonjour")

    def bonjour(self,short: bool = False):
        if short:
            self._say_hi()
        else:
            print(f"Bonjour, je suis {self.nom} !")

class Hacker():
    def __init__(self, attack_type: str) -> None:
        self.attack_type = attack_type

    def attack(self, ip: str):
        print(f"{self.attack_type}, rdm bs attack → {ip}")

# ici la class herite des propriete de la class User
class Admin(User, Hacker):
    def __init__(self, nom, email, age, origine, attack_type) -> None:
        # super().__init__(nom, email, age)
        User.__init__(self, nom, email, age)
        Hacker.__init__(self, nom, email, age)
        self.origine = origine


    def delete_user(self, user: User):
        print(f"user: {user.email} a ete supprimer")

    # surcharge == on reecris la meme methode avec un logique differente
    def bonjour(self, short: bool = False):
        # return super().bonjour(short)
        print("Bonjour, je sui l'Admin.")

class Entreprise(User):
    pass

admin = Admin("John", "jbloodb@email.com", 22, "bureau", "ddos")
user = User("Bob", "bobds@email.com", 24)

admin.bonjour()
admin.delete_user(user)

#isinstance et issubclass

print(isinstance(admin, Admin))
print(isinstance(admin, User))
print(isinstance(admin, object)) # classe racine de toute classe dans python

print(issubclass(Admin, User)) # verifie si subclass
print(issubclass(Admin, object))

#Example de multi heritage
admin.attack("127.0.0.1")
#preferer nom de classe plutot que super()