#template pentru citirea din fisier (ex.txt):
#------------------------

#stare a    litera din alfabetul automatului    stare b
#stare x    litera din alfabetul automatului    stare s
#    .
#    .
#    .
#    .
# stare y   litera din alfabetul automatului    stare z
# stare x stare z      ( starile finale - pe ultima linie a fisierului)







tranzitie_start = []
litera = []
tranzitie_urm = []
stari_finale = []


with open('ex.txt') as f:
    for x in f:
        y = x.split()
        if len(y) == 3:                     #de modificat
            tranzitie_start.append(y[0])
            litera.append(y[1])
            tranzitie_urm.append(y[2])
        else:
            stari_finale.append(y[0])
            stari_finale.append(y[1])



cuvant = input("Dati Cuvantul :   ")
drum = []
stare_curenta = tranzitie_start[0]
drum.append(stare_curenta)
for cuv in cuvant:
    ok = 0
    for a in range(len(tranzitie_start)):
        if ok == 0:
            if ((stare_curenta == tranzitie_start[a]) & (litera[a] == cuv)):
                stare_curenta = tranzitie_urm[a]
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
