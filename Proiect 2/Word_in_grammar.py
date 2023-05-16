def valideaza(gramatica, start_symbol, cuvant):
    if not cuvant and 'l' in gramatica[start_symbol]:
        print("Cuvant Valid")
        return True

    for regula in gramatica[start_symbol]:
        if regula[0].islower() and cuvant and cuvant[0] == regula[0]:
            if valideaza(gramatica, regula[1], cuvant[1:]):
                return True
        elif regula[0].isupper():
            if valideaza(gramatica, regula[0], regula[1] + cuvant):
                return True

    return False


gramatica = {
    'S': [('a', 'A'), ('d', 'E')],
    'A': [('a', 'B'), ('a', 'S')],
    'B': [('b', 'C')],
    'C': [('b', 'D'), ('b', 'B')],
    'D': [('c', 'D'), 'l'],
    'E': ['l']
            }

start_symbol = 'S'
cuvant = "aabbdcc"

if not valideaza(gramatica, start_symbol, cuvant):
    print(f"Cuvant '{cuvant}' invalid")
