# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 12 : Programme de validation d'identité
# Crée un système qui vérifie l'identité des objets :

def verifier_identite(obj1, obj2, nom1, nom2):
    # Doit retourner un rapport complet
    egalite = obj1 == obj2
    identite = obj1 is obj2
    type_identique = type(obj1) == type(obj2)

    return {
        "égalité": egalite,
        "identité": identite,
        "même_type": type_identique
    }

# Tests avec différents cas
cas_test = [
    (100, 100, "a", "b"),
    (1000, 1000, "c", "d"),
    ([1,2], [1,2], "liste1", "liste2"),
    ("hello", "hello", "str1", "str2")
]

for obj1, obj2, nom1, nom2 in cas_test:
    id_verifier = verifier_identite(obj1, obj2, nom1, nom2)
    
    print(f"verification de l'egalite entre {nom1}:({obj1}) et {nom2}:({obj2})")
    print(f"égalité: {id_verifier["égalité"]}\n\n")

    print(f"verification de l'identite entre {nom1}:({obj1}) et {nom2}:({obj2})")
    print(f"identité: {id_verifier["identité"]}\n\n")

    print(f"verification du type entre {nom1}:({obj1}) et {nom2}:({obj2})")
    print(f"même_type: {id_verifier["même_type"]}\n\n")