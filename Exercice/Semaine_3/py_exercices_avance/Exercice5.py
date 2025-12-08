# Date: 2025-11-12
# Auteur: Émile V
# But: Exercice 5 : Programme de conversion universelle
# Crée un programme qui détecte automatiquement le type d'entrée et le convertit :

def detecter_et_convertir(valeur):
    # À compléter : doit détecter si c'est un int, float, bool ou string
    # et retourner la valeur convertie dans tous les types possibles
    
    #commence avec int
    try: 
        tmp = int(valeur)

        if(tmp == 0 or tmp == 1):
            return([tmp, float(tmp), bool(tmp), valeur])
        else:
            return([tmp, float(tmp), valeur])
        
    except ValueError:
        pass

    #ensuite float
    try:
        tmp = float(valeur.replace(',', '.'))
        
        return([int(tmp), tmp, valeur])

    except ValueError:
        pass

    #ensuite bool
    if valeur.lower() in ('true', 'false'):
        tmp = valeur.lower()
        if(tmp == 'true'):
            return([1, 1.0, True, 'True'])
        else:
            return([0, 0.0, False, 'False'])

    #enfing str
    return [valeur]


# Tests
test_values = ["123", "45.67", "True", "hello", "0"]

for valeur in test_values:
    print(detecter_et_convertir(valeur))