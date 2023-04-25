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

f = open("ex.txt", "r")
y =[[x for x in linie.split()] for linie in f.read().split('\n')]
f.close()
stari_finale = y[len(y)-1]
y.remove(y[len(y)-1])



for i in range(len(y)):
    tranzitie_start.append(y[i][0])
    litera.append(y[i][1])
    tranzitie_urm.append(y[i][2])

print(tranzitie_start)
print(litera)
print(tranzitie_urm)


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
    print("Cuvant acceptat.")
    print("Drumul final este :")
    for i in range(len(drum)-1):
        print(drum[i] + "->" + drum[i+1])
