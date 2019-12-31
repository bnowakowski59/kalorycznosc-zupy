#Program do wyliczenia kaloryczności zupy v0.2 

#############################################################
#v0.1 - napisano funkcjonalność programu                    #
#v0.2 - dodano funkcję warunkową if do gramatury produktów  #     
#############################################################

#Kaloryczność produktów w 100g
KALORIE_MARCHEWKA   = 41.3
KALORIE_ZIEMNIAK    = 75.0
KALORIE_DYNIA       = 26.1
KALORIE_INDYK       = 123
KALORIE_PIETRUSZKA  = 36.1
KALORIE_CUKINNIA    = 16.7
KALORIE_BROKUL      = 33.7
KALORIE_KALAFIOR    = 24.0
KALORIE_SELER       = 14.0
KALORIE_BURAK       = 43
KALORIE_CEBULA      = 40

#Gramatura słoika
GRAMATURA_SLOIKA = 170 #gramatura sloika w gramach

#Gramatura porduktów
dodajMarchewke  = float(input("Podaj ile użyto marchewki: ")) 
dodajZiemniak   = float(input("Podaj ile użyto ziemniaka: "))
dodajDynia      = float(input("Podaj ile użyto dynii: "))  
dodajIndyk      = float(input("Podaj ile użyto indyka: "))
dodajPietruszka = float(input("Podaj ile użyto pietruszki: "))
dodajCukinnia   = float(input("Podaj ile użyto cukinni: "))
dodajBrokul     = float(input("Podaj ile użyto brokuła: "))
dodajKalafior   = float(input("Podaj ile użyto kalafiora: "))
dodajSeler      = float(input("Podaj ile użyto selera: "))
dodajBurak      = float(input("Podaj ile użyto buraka: "))
dodajCebule     = float(input("Podaj ile użyto cebuli: "))

sumaGramaturyProduktow = float(dodajBrokul + dodajBurak + dodajCukinnia + dodajDynia + dodajIndyk + dodajKalafior\
+ dodajMarchewke + dodajPietruszka + dodajSeler + dodajZiemniak + dodajCebule
)

#Całościowa kaloryczność zupy
caloscowaKalorycznoscZupy = float((dodajMarchewke * KALORIE_MARCHEWKA + dodajZiemniak * KALORIE_ZIEMNIAK + dodajDynia * KALORIE_DYNIA\
+ dodajIndyk * KALORIE_INDYK + dodajPietruszka * KALORIE_PIETRUSZKA + dodajCukinnia * KALORIE_CUKINNIA + dodajBrokul * KALORIE_BROKUL\
+ dodajKalafior * KALORIE_KALAFIOR + dodajSeler * KALORIE_SELER + dodajBurak * KALORIE_BURAK + dodajCebule * KALORIE_CEBULA)/100
)

lista = [["Brokul", dodajBrokul, format(dodajBrokul*KALORIE_BROKUL/100,".2f")],
         ["Burak", dodajBurak, format(dodajBurak*KALORIE_BURAK/100,".2f")],
         ["Cukinnia", dodajCukinnia, format(dodajCukinnia*KALORIE_CUKINNIA/100,".2f")],
         ["Dynia", dodajDynia, format(dodajDynia*KALORIE_DYNIA/100,".2f")],
         ["Indyk", dodajIndyk, format(dodajIndyk*KALORIE_INDYK/100,".2f")],
         ["Kalafior", dodajKalafior, format(dodajKalafior*KALORIE_KALAFIOR/100,".2f")],
         ["Marchewka", dodajMarchewke, format(dodajMarchewke*KALORIE_MARCHEWKA/100,".2f")],
         ["Pietruszka", dodajPietruszka, format(dodajPietruszka*KALORIE_PIETRUSZKA/100,".2f")],
         ["Seler", dodajSeler, format(dodajSeler*KALORIE_SELER/100,".2f")],
         ["Ziemniak", dodajZiemniak, format(dodajZiemniak*KALORIE_ZIEMNIAK/100,".2f")],
         ["Cebula", dodajCebule, format(dodajCebule*KALORIE_CEBULA/100,".2f")]
        ]  
print("\n\n")
print("----------------------------------------------------------------")
print("|    Produkt      |     Gramatura     |      Kaloryczność      |")
print("----------------------------------------------------------------")
for item in lista:
    print("|   ",item[0]," "*(11-len(item[0])),"|    ",
              item[1]," "*(12-len(str(item[1]))),"|",
              item[2]," "*(21-len(str(item[2]))),"|" )
print("----------------------------------------------------------------")
print("\n")
print("Ze "+ str(format(sumaGramaturyProduktow,".2f")) + "g produktów uzyskano " + str(format(caloscowaKalorycznoscZupy,".2f")) + " kcal")
if sumaGramaturyProduktow > GRAMATURA_SLOIKA:
    print("W sloiku " + str(format(GRAMATURA_SLOIKA,".2f")) + "g znajduje się " + \
          str(format(caloscowaKalorycznoscZupy * GRAMATURA_SLOIKA / sumaGramaturyProduktow,".2f")) + " kcal"
         )
else:
    print("Użyto zbyt mało produktów dla " + str(format(GRAMATURA_SLOIKA,".2f")) + " g słolika.")
print("\nW 100g zupy znajduje się " + str(format(caloscowaKalorycznoscZupy * 100 / sumaGramaturyProduktow,".2f")) + " kcal")

input("\nNaciśnij dowolny przycisk aby zakończyc.")