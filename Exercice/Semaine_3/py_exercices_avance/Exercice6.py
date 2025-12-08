# Date: 2025-11-12
# Auteur: Émile Valade
# But: Exercice 6 : Gestion des arrondis et troncatures
# Écris un programme qui montre les différences entre différentes 
# méthodes de conversion :
import math

# Valeurs à convertir
valeurs = [12.3, 12.7, -12.3, -12.7, "12.3", "12.7"]

for valeur in valeurs:
    # Conversions avec int(), round(), et math.floor()
    print(f"debut de conversion de la valeur: {valeur}, de type: {type(valeur)}\n\n")

    try:
        tmp = int(valeur)
        print(f"conversion: int()\nvaleur: {tmp}\ntype: {type(tmp)}\n")
    except Exception as e:
        print(f"conversion impossible: valeur: {valeur}, type: {type(valeur)}")

    try:
        tmp = round(valeur)
        print(f"conversion: round()\nvaleur: {tmp}\ntype: {type(tmp)}\n")
    except Exception as e:
        print(f"conversion impossible: valeur: {valeur}, type: {type(valeur)}")

    try: 
        tmp = math.floor(valeur)
        print(f"conversion: math.floor()\nvaleur: {tmp}\ntype: {type(tmp)}\n")
    except Exception as e:
        print(f"conversion impossible: valeur: {valeur}, type: {type(valeur)}")
    
    print(f"fin de la conversion de la valeur: {valeur}")
    print(f"-------------------------------------------\n\n\n")