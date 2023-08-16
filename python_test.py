import re


class proizvod:
    def __init__(self, ime, broj, cena):   
        self.ime = ime  
        self.broj = broj
        self.cena = cena
        


def odstampaj(korpa):
    if len(korpa)==0:
        print("Korpa je prazna!\n")
    else:
        for x in range(len(korpa)):
            print("U korpi su {}, kolicina {} sa cenom po komadu {}".format(korpa[x].ime, korpa[x].broj, korpa[x].cena))    

def dodaj(korpa, ime, kolicina):
       
    if ime in asortiman.keys():
        for x in range(len(korpa)):
            if korpa[x].ime==ime:
                print("Proizvod je vec u korpi, uvecana kolicina!\n")
                kol=int(korpa[x].broj)+int(kolicina)
                korpa[x].broj=kol
                return korpa  
        cena=asortiman[ime]
        korpa.append(proizvod(ime, kolicina, cena))
        return korpa
    else:
        print("Molimo unesite proizvod iz ponude!\n")    


def ucitaj_datoteku(ulazna):
    with open(ulazna, encoding="UTF-8") as ulaz:
        asortiman = dict()
        for linija in ulaz:
            ime, cena = linija.split(",")
            asortiman[ime] = int(cena)
        return asortiman

def suma(korpa):
    if len(korpa)==0:
        print("Korpa je prazna!\n")
    else:
        odstampaj(korpa)
        kolicina=0
        for x in range(len(korpa)):
            kolicina+=int(korpa[x].broj)*int(korpa[x].cena)
        print("Ukupno za platiti je: {} dinara" .format(kolicina))    

def obrisi(korpa, ime):
    if len(korpa)==0:
        print("Korpa je vec prazna!\n")
    else:
        for x in range(len(korpa)):
            if korpa[x].ime==ime:
                del korpa[x]
                print("Proizvod je uklonjen iz korpe!\n")
                return
        print("Proizvod nije u korpi!\n")   

asortiman = ucitaj_datoteku("cene.txt")


with open("cene.txt") as file:
    text = file.read()
pattern = re.compile(r"\d{1,5}")
cena = pattern.findall(text)

print (text)

print (cena)

print(asortiman)

print(asortiman["banane"]+asortiman["hleb"])
korpa = []

while True:
    print("Dobrodosli u prodavnicu!\nAko zelite da pogledate ponudu unesite 1\nAko zelite da dodate proizvod u korpu unesite 2\nAko zelite da obrisete proizvod iz korpe unesite 3\nAko zelite da pregledate korpu pritisne 4\nAko zelite da platite pritisnite 5\nAko zelite da izadjete iz programa pritisnite 6\n")
    
    ulaz = input("Odaberite opciju: ")

    if ulaz=="1":
        print("U ponudi su: \n {}" .format(list(asortiman.keys())))
        print("\n")
    elif ulaz=="2":
        ime_proizvoda = input("Unesite ime proizvoda koji bi da dodate u korpu: ")
        kolicina_proizvoda = input("Unesite kolicinski broj proizvoda koji bi da dodate u korpu: \n")   
        dodaj(korpa, ime_proizvoda, kolicina_proizvoda)     
    elif ulaz=="3":
        ime_proizvoda = input("Unesite ime proizvoda koji bi da uklonite iz korpe: ")
        obrisi(korpa, ime_proizvoda)
    elif ulaz=="4":
        odstampaj(korpa)
    elif ulaz=="5": 
        suma(korpa)
    elif ulaz=="6":
        print("Nadamo se da ste zadovoljni koriscenjem prodavnice\nPrijatan dan!")
        break
    else:
        print("Molimo da odaberete jednu od opcija!")

"""

    korpa = []



    ime_proizvoda = input("Unesite ime proizvoda koji bi da dodate u korpu: ")
    kolicina_proizvoda = input("Unesite kolicinski broj proizvoda koji bi da dodate u korpu: ")



    for i in range(len(korpa)):
            if str(korpa[i].ime)==ime_proizvoda
                korpa[i].kolicina+=kolicina_proizvoda
                print ("Proizvod je vec bio u korpi, uvecana kolicina!")
            else:
                dodaj(korpa, ime_proizvoda, kolicina_proizvoda)
                
            """