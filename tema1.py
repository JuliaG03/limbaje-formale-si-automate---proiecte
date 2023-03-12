tranzitii_initiale = []
ramura = []
urmatoare = []
stari_finale = []


with open('det.txt') as f:
    for x in f:
        y = x.split()
        if len(y) == 3:
            tranzitii_initiale.append(y[0])
            ramura.append(y[1])
            urmatoare.append(y[2])
        elif len(y) == 2:
            stari_finale.append(y[0])
            stari_finale.append(y[1])



cuvant = input("Dati Cuvantul :   ")
drum = []
stare_curenta = tranzitii_initiale[0]
drum.append(stare_curenta)
for cuv in cuvant:
    ok = 0
    for si in range(len(tranzitii_initiale)):
        if ok == 0:
            if ((stare_curenta == tranzitii_initiale[si]) & (ramura[si] == cuv)):
                stare_curenta = urmatoare[si]
                drum.append(stare_curenta)
                ok = 1
            else:
                pass



if drum[len(drum)-1] not in stari_finale:
    print("Cuvant neacceptat")
    print(drum)
else:
    for i in range(len(drum)-1):
        print("Cuvant acceptat.")
        print("Drumul final este :")
        print(drum[i] + "->" + drum[i+1])
