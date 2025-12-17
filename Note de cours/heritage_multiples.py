class A():
    def __init__(self) -> None:
        super().__init__() 
        print("A")

class B():
    def __init__(self) -> None:
        super().__init__()
        print("B")

class D():
    def __init__(self) -> None:
        super().__init__()
        print("D")

# De gauche a droite le init de A va s'executer en premier et son super va referencer le parent suivant
class C(A, B, D):
    def __init__(self):
        super().__init__() 
        print("C")

c = C()

# Method resolution order (de gauche a droite)
print(C.mro())
# lors de l'execution on remonte jusqu'a objet puis on redescent vers la classe en executant chaqune
# C → A → B → D → Objet ... ensuite ... Objet → D → B → A → C 
# c'est dans la deuxieme partie que les classe vont executer le code

