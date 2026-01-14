import random

a = random.random()
b = random.randint(1,10)
c = random.choice(['a', 'b', 'c', 'd'])
liste = [1, 2, 3, 4, 5]
d = random.shuffle(liste)

print(a, b, c , liste)

#-----------------------------------------
print(10*'-')
#-----------------------------------------
import math 

print(math.pi)
print(math.e)

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.floor(1.23234))
print(math.ceil(1.23234))


#-----------------------------------------
print(10*'-')
#-----------------------------------------
import json

donnes = {"nom": "Alice", "age": 25}
json_str = json.dumps(donnes)
print(json_str)

donnes_recuperees = json.loads(json_str)
print(donnes_recuperees["nom"])

with open("data.json", "w") as f: 
    json.dump(donnes,f)

with open("data.json", "r") as f:
    donnes_lues = json.load(f)
    print(donnes_lues)

#-----------------------------------------
print(10*'-')
#-----------------------------------------
import os 

# chemin de fichiers
result = os.path.exists("data.json")
file_size = os.path.getsize("data.json")
print(result)
print(file_size)

print(os.listdir("."))

if not os.path.exists("test"):
    os.mkdir("test")
else:
    os.rmdir("test")

#-----------------------------------------
print(10*'-')
#-----------------------------------------
import datetime

aujourdhui = datetime.date.today()
print(aujourdhui)

maintenant = datetime.datetime.now()
print(maintenant)

date_specifique = datetime.date(2024, 4, 25)

print(date_specifique)

date_formatee = aujourdhui.strftime("%d/%m/%Y")
