def solo_consonantes(texto):
    vocales = "aeiouAEIOU"
    return ''.join([c for c in texto if c not in vocales])

print(solo_consonantes("algoritmos")) 
print(solo_consonantes("logaritmos"))


def solo_vocales(texto):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return ''.join([c for c in texto if c not in consonantes])

print(solo_vocales("sen consonantes"))


def siguiente_vocal(texto):
    mapa = {
        'a': 'e', 
        'e': 'i',
        'i': 'o', 
        'o': 'u', 
        'u': 'a',
        'A': 'E', 
        'E': 'I', 
        'I': 'O', 
        'O': 'U', 
        'U': 'A'
    }
    return ''.join([mapa.get(c, c) for c in texto])


print(siguiente_vocal("vestiario"))
