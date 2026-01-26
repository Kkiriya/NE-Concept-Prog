from functools import reduce

# reduce permet de reduire une sequence iterable en une valeur unique 
panier = [
    {
        "name": "oignon",
        "price": 5,
        "quantity": 1
    },
    {
        "name": "pomme",
        "price": 1.48,
        "quantity": 10
    },
    {
        "name": "poulet",
        "price": 19,
        "quantity": 2
    },
    {
        "name": "celeri",
        "price": 3,
        "quantity": 2
    }
]
def fn(treduce, item):
    return treduce + item['price'] * item['quantity']

total = reduce(fn, panier, 0)
# print(total)
# en lambda 
total = reduce(lambda treduce, item: treduce + item['price'] * item['quantity'], panier, 0)

# print(total)

def fn(acc, item):
    acc["total_price"] += item["price"] * item["quantity"]
    acc["total_quantity"] += item["quantity"]
    return acc

total = reduce(fn, panier, {"total_price": 0, "total_quantity": 0})
# print(total)total = reduce(lambda treduce, item: treduce + item['price'] * item['quantity'], panier, 0)


# Fonction lambda, soit fonctions ecrise en une seule lignes
# lambda param1, param2, ... : expression

a = [1, 2, 3]
b = list(map(lambda x: x * 2, a))
# print(b)

# exo sortir nbr pair 
la_liste = [1, 25, 45, 74, 8, 102, 56]

nbr_pair = list(filter(lambda x: x%2 == 0, la_liste))

print(nbr_pair)