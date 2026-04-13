class Diak:
    def __init__(self, nev, osztaly, atlag):
        self.nev = nev
        self.osztaly = osztaly
        self.atlag = float(atlag)


diakok = []

with open("diak.txt", encoding="utf-8") as f:
    for sor in f:
        sor = sor.strip()
        if sor != "":
            adatok = sor.split(";")
            nev = adatok[0]
            osztaly = adatok[1]
            atlag = adatok[2]

            uj_diak = Diak(nev, osztaly, atlag)
            diakok.append(uj_diak)

print("letszam:", len(diakok))

osszeg = 0
for d in diakok:
    osszeg += d.atlag

atlag = osszeg / len(diakok)
print("csoportatlag:", round(atlag, 2))

if diakok:
    legjobb = diakok[0]
    for d in diakok:
        if d.atlag > legjobb.atlag:
            legjobb = d

    print("legjobb tanulo:", legjobb.nev, legjobb.atlag)

evfolyamok = []

for d in diakok:
    ev = int(d.osztaly[:2])
    if ev not in evfolyamok:
        evfolyamok.append(ev)

hianyzo = []

for ev in range(9, 13):
    if ev not in evfolyamok:
        hianyzo.append(ev)

if len(hianyzo) == 0:
    print("van minden evfolyam")
else:
    print("hianyzo evfolyam:", hianyzo)