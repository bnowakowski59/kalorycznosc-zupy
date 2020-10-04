
import pickle

class Produkt:

    def __init__(self, nazwaProduktu, kalorycznoscProduktu):
        self.nazwaProduktu = nazwaProduktu
        self.kalorycznoscProduktu = float(kalorycznoscProduktu)
        self.gramaturaSloika = 170
        self.listaProdukty = []

    def __str__(self):
        return f"{self.nazwaProduktu} " f"{self.kalorycznoscProduktu}"


class ProduktyController:

    def __init__(self):
        self.listaZup = []

    def dodajProdukt(self, nazwaProduktu, produktKalorycznosc):
        produkt = Produkt(nazwaProduktu, produktKalorycznosc)

        self.listaProdukty.append(produkt)

        plik = open("produkty.dat", "wb")
        pickle.dump(self.listaProdukty, plik)
        plik.close()

        print(f"Dodano produkt {nazwaProduktu}")

    def usunProdukt(self, nazwa):
        try:
            plik = open("produkty.dat", "rb")
            self.listaProdukty = pickle.load(plik)
            plik.close()
        except:
            print(f"Nie wykryto pliku.")

        for i in self.listaProdukty:

            if(i.nazwaProduktu == nazwa):
                print(i)
                self.listaProdukty.remove(i)
                break

        plik = open("produkty.dat", "wb")
        pickle.dump(self.listaProdukty, plik)
        plik.close()

    def pokazProdukty(self):

        try:
            plik = open("produkty.dat", "rb")
            self.listaProdukty = pickle.load(plik)
            plik.close()
        except:
            print(f"Nie wykryto pliku.")

        for i in self.listaProdukty:
            print(f"{i}")

    def piclkeLoadProdukty(self):
        try:
            plik = open("produkty.dat", "rb")
            self.listaProdukty = pickle.load(plik)
            plik.close()

        except:
            plik = open("produkty.dat", "wb")
            pickle.dump([], plik)
            plik.close()

        finally:
            plik = open("produkty.dat", "rb")
            self.listaProdukty = pickle.load(plik)
            plik.close()

class AplikacjaZupa(ProduktyController):

    def __init__(self, nazwa):
        super().__init__()
        self.nazwa = nazwa
        self.menu()

    def menu(self):

        while(True):
            print(f"Witaj w aplikacji {self.nazwa}")
            menu = input(f"1 - dodaj produkt, 2 - usun produkt, 3 - wyświetl produkty, 4 - sprawdz kalorycznosc zupy, K - Zakończ program.").upper()

            if(menu == "1"):
                self.piclkeLoadProdukty()
                nazwaProduktu = input(f"Wprowadz nazwę produktu: ")
                produktKalorycznosc = float(input(f"Wprowadz kaloryczność {nazwaProduktu} "))
                self.dodajProdukt(nazwaProduktu, produktKalorycznosc)

            elif(menu == "2"):
                nazwaProduktu = input(f"Wprowadz nazwę produktu do usunięcia: ")
                self.usunProdukt(nazwaProduktu)

            elif(menu == "3"):
                self.pokazProdukty()

            elif(menu == "4"):
                while(True):


            elif(menu == "K"):
                break

            else:
                print("Nie rozpoznano opckji.")
aplikacja = AplikacjaZupa("Test")
