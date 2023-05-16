import random
def afisare(dictionar):
    for linie in dictionar:
        print(linie,dictionar[linie])
    print()

def afisarePartitie(partitii):
    for partitie in partitii:
        print(partitii.index(partitie))
        for stare in partitie:
            print(stare,partitie[stare])
    print()

def stariAproapeEgale(st1,st2):
    ok = 1
    for litera in alfabet:
        if st1[litera][1] != st2[litera][1]:
            ok = 0
    return ok

def partitionare(listaPartitii):
    partitieNoua = []
    for partitie in listaPartitii:
        for stare in partitie:
            if len(partitieNoua) == 0 or len(partitie) == 1: #daca partitia e goala sau are o sg stare
                partitieNoua.append({stare:partitie[stare]})
            else:
                for x in partitieNoua:
                    if stariAproapeEgale(partitie[stare] , x[random.choice(list(x.keys()))]): #verifica daca st curenta si una random sunt aproape egale
                        x[stare] = partitie[stare]
                        break
                else:
                    partitieNoua.append({stare: partitie[stare]}) # daca nu s a gasit partitie, adaugam dict cu cheia stare si valoarea corespunzatoare
    return partitieNoua

def reconstruct(partiii):
    for partitie in partitii:
        for stare in partitie:
            for litera in partitie[stare]:
                for partitie2 in partitii:
                    if partitie[stare][litera][0] in partitie2:
                        partitie[stare][litera][1] = partitii.index(partitie2)

with open("minimalDFA.in")as f:
    alfabet = f.readline().strip().split()
    finale = f.readline().strip().split()
    tranzitii = f.readline().strip().split()
    dictionar_tranzitii = {}
    for stare in tranzitii:
        dictionar_tranzitii[stare] = {}
    for linie in f:
        tranz = linie.strip().split()
        dictionar_tranzitii[tranz[0]][tranz[1]] = [tranz[2],None]

partitii = []
A = {}
B = {}
for stare in dictionar_tranzitii:
    if stare in finale:
        B[stare] = dictionar_tranzitii[stare]
    else:
        A[stare] = dictionar_tranzitii[stare]
partitii.append(A)
partitii.append(B)
reconstruct(partitii)

partitieaux = partitionare(partitii)
reconstruct(partitieaux)


while partitieaux != partitii:
    partitii = partitionare(partitii)
    reconstruct(partitii)

    parAux = partitionare(partitieaux)
    reconstruct(partitieaux)
print("Partitii finale dupa minimizare:")
afisarePartitie(partitii)