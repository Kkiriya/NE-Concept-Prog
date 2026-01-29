def aplatir(liste, liste_aplati=[], msg="from original loop"):
    for i in liste:
        print(f"whoami: {msg}\nliste: {liste}\nliste_aplati: {liste_aplati}\nn: {i}\n")
        
        if isinstance(i, list):
            (aplatir(i, liste_aplati, "from inside loop"))
        else:
            liste_aplati.append(i)
            print(f"liste_aplati: {liste_aplati}\nn: {i}\n")
    return liste_aplati

# Test
print(aplatir([1, [2, [3, 4], 5], 6]))
# [1, 2, 3, 4, 5, 6]