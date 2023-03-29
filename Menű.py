
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