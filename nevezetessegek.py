class Nevezetesseg:
    def __init__(self, nev: str, orszag: str, varos: str, epult: str) -> None:
        self.nev = nev
        self.orszag = orszag
        self.varos = varos
        self.epult = epult

    def __str__(self) -> str:
        return f"{self.nev} {self.orszag} {self.varos} {self.epult}"

csv = open("./nevezetessegek.csv", encoding="UTF-8")

sorok = csv.readlines()

sorok.pop(0)

nevezetessegek = []

for sor in sorok:
    tulajdonsagok = sor.split(";")
    nevezetesseg = Nevezetesseg(tulajdonsagok[0], tulajdonsagok[1], tulajdonsagok[2], tulajdonsagok[3])
    nevezetessegek.append(nevezetesseg)

valasztas = -1

while valasztas != 4:
    print("1. Nevezetességek listája")
    print("2. Ország választás")
    print("3. Város választás")
    print("4. Kilépés")

    valasztott_szam = input("Válassz egy számot 1-4: ")

    if not valasztott_szam.isnumeric():
        continue

    valasztas = int(valasztott_szam)

    if valasztas == 1:
        for nevezetesseg in nevezetessegek:
          print(nevezetesseg)
    
    elif valasztas == 2:
        orszagnev = input("Adj meg egy országot: ")
        for nevezetesseg in nevezetessegek:
            if orszagnev == nevezetesseg.orszag:
                print(nevezetesseg.nev)

    elif valasztas == 3:
        varosnev = input("Adj meg egy várost: ")
        for nevezetesseg in nevezetessegek:
            if varosnev == nevezetesseg.varos:
                print(f"{nevezetesseg.nev} {nevezetesseg.orszag} {nevezetesseg.epult}") 