# STATUSY V PROGRAME
STATUS_OK = "OK"
STATUS_NOT_FOUND = "NOT_FOUND"
STATUS_ALREADY_BORROWED = "ALREADY_BORROWED"

# TRIEDA KNIHA

class Kniha:
    def __init__(self, nazov:str, autor:str, ISBN:str, rok_vydania:int, dostupna = True):
        ISBN = ISBN.strip().upper()
        self.nazov= nazov
        self.autor= autor
        self.ISBN= ISBN
        self.dostupna= dostupna
        self.rok_vydania= rok_vydania

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
            return True
        else:
            return False

    def vratit(self):
        self.dostupna = True

    def __str__(self):
        stav = "Dostupna" if self.dostupna else "Vypozicana"
        return f"{self.nazov} od {self.autor}, ISBN: {self.ISBN}, Rok: {self.rok_vydania}, {stav}"

# TRIEDA KNIZNICA

class Kniznica:
    def __init__(self):
        self.kniznica = []

    def pridat_knihu(self, kniha: Kniha):
        for i in self.kniznica:
            if i.ISBN == kniha.ISBN:
                return False
        self.kniznica.append(kniha)
        return True

    def hladat_podla_nazvu(self, hladany_nazov):
        vysledok_hladania = []
        for i in self.kniznica:
            if hladany_nazov.lower() in i.nazov.lower():
                vysledok_hladania.append(i)
        return vysledok_hladania

    def hladat_podla_isbn(self, hladane_ISBN):
        hladane_ISBN = hladane_ISBN.upper().strip()
        for kniha in self.kniznica:
            if kniha.ISBN == hladane_ISBN:
                return kniha
        return None

    def vypozicat_knihu_podla_isbn(self, hladane_ISBN):
        hladane_ISBN = hladane_ISBN.strip().upper()

        kniha = self.hladat_podla_isbn(hladane_ISBN)
        if kniha is None:
            return (STATUS_NOT_FOUND, None)

        uspech = kniha.vypozicat()
        if uspech:
            return (STATUS_OK, kniha)
        else:
            return (STATUS_ALREADY_BORROWED, kniha)

    def vratit_knihu_podla_isbn(self, hladane_ISBN):
        hladane_ISBN = hladane_ISBN.strip().upper()
        kniha = self.hladat_podla_isbn(hladane_ISBN)

        if kniha is None:
            return (STATUS_NOT_FOUND, None)
        else:
            kniha.vratit()
            return (STATUS_OK, kniha)

    def vypisat_dostupne_knihy(self):
        dostupne = []
        for kniha in self.kniznica:
            if kniha.dostupna:
                dostupne.append(kniha)
        return dostupne

    def vypisat_vsetky_knihy(self):
        return self.kniznica

    def vymazat_knihu(self, hladane_ISBN):
        hladane_ISBN = hladane_ISBN.strip().upper()
        for kniha in self.kniznica:
            if kniha.ISBN == hladane_ISBN:
                self.kniznica.remove(kniha)
                return kniha
        return None


# MENU
def vypisat_menu():
    print("**** Vitajte v kniznici. Co chcete urobit? ****")
    print("-------------------------------------------------")
    print("1. Pridat knihu do kniznice")
    print("2. Hladat knihu v kniznici podla nazvu")
    print("3. Hladat knihu v kniznici podla ISBN")
    print("4. Vypozicat knihu")
    print("5. Vratit knihu")
    print("6. Zoznam dostupnych knih")
    print("7. Zoznam vsetkych knih v kniznici")
    print("8. Vymazat knihu")
    print("9. Zobrazit menu")
    print("0. Ukoncit program")


def spusti_menu(kn):
    vypisat_menu()

    while True:
        volba = input("\nZadajte cislo volby (0-9): ").strip()

        # Pridat knihu do kniznice
        if volba == "1":
            nazov_knihy = input("Nazov knihy: ").strip()
            autor_knihy = input("Autor knihy: ").strip()
            isbn_knihy = input("ISBN: ").strip().upper()
            try:
                rok_vydania = int(input("Rok vydania: "))
            except ValueError:
                print("\nRok musi byt cislo. Napr.2021")
                continue

            k = Kniha(nazov_knihy, autor_knihy, isbn_knihy, rok_vydania)

            uspech = kn.pridat_knihu(k)
            if uspech:
                print("\n----Kniha pridana----")
            else:
                print("\nKniha nebola pridana. ISBN sa uz v kniznici nachadza")

        # Hladat knihu v kniznici podla nazvu
        elif volba == "2":
            hladany_nazov = input("Zadajte nazov knihy alebo jeho cast: ").strip()
            if not hladany_nazov:
                print("\nNezadali ste nazov.")
                continue
            vysledky = kn.hladat_podla_nazvu(hladany_nazov)
            if not vysledky:
                print("\nKniha sa v kniznici nenachadza.")
            else:
                print("\n--- Nájdené knihy ---")
                for i in vysledky:
                    print(i)
                print()

        # Hladat knihu v kniznici podla ISBN
        elif volba == "3":
            hladane_isbn = input("\nZadajte ISBN: ").strip().upper()
            if not hladane_isbn:
                print("\nNezadali ste ISBN.")
                continue
            najdena_kniha = kn.hladat_podla_isbn(hladane_isbn)
            if not najdena_kniha:
                print("\nKnihu sa nepodarilo najst.")
            else:
                print (najdena_kniha)

        # Vypozicat knihu
        elif volba == "4":
            hladane_isbn = input("Zadajte ISBN: ").strip().upper()

            if not hladane_isbn:
                print("\nNezadali ste ISBN.")
                continue

            status, kniha = kn.vypozicat_knihu_podla_isbn(hladane_isbn)

            if status == STATUS_ALREADY_BORROWED:
                print(f"\nKnihu {kniha.nazov}, ISBN: {kniha.ISBN} sa nepodarilo vypozicat, lebo je prave vypozicana.")
            elif status == STATUS_NOT_FOUND:
                print(f"\nKniha s ISBN: {hladane_isbn} sa nenachadza v zozname kniznice.")
            elif status == STATUS_OK:
                print(f"\nVypozicali ste si knihu {kniha.nazov}, ISBN: {kniha.ISBN}. Vratte je do 30 dni.")

        # Vratit knihu
        elif volba == "5":
            hladane_isbn = input("Zadajte ISBN: ").strip().upper()

            status, kniha = kn.vratit_knihu_podla_isbn(hladane_isbn)

            if status == STATUS_NOT_FOUND:
                print(f"\nKnihu s ISBN {hladane_isbn} sa nepodarilo vratit.")
            else:
                print(f"\nDakujeme za vratenie knihy {kniha.nazov}, ISBN: {kniha.ISBN}.")

        # Zoznam dostupnych knih
        elif volba == "6":
            zoznam = kn.vypisat_dostupne_knihy()
            print("\n--- Dostupne knihy ---")

            if not zoznam:
                print("Ziadne dostupne knihy.")
            else:
                for kniha in zoznam:
                    print(kniha)

        # Zoznam vsetkych knih v kniznici
        elif volba == "7":
            zoznam = kn.vypisat_vsetky_knihy()
            print("\n--- Vsetky knihy v kniznici---")
            if not zoznam:
                print("Kniznica je prazdna.")
            else:
                for kniha in zoznam:
                    print(kniha)

        # Vymazat knihu
        elif volba == "8":
            hladane_isbn = input("Zadajte ISBN: ").strip().upper()
            vystup = kn.vymazat_knihu(hladane_isbn)

            if vystup is None:
                print(f"\nISBN {hladane_isbn} sa v kniznici nenachadza. Kniha nebola vymazana.")
            else:
                print(f"\n---Kniha {vystup.nazov} , ISBN: {vystup.ISBN} bola vymazana.---")

        # Zobrazit menu
        elif volba == "9":
            vypisat_menu()

        # Ukoncit program
        elif volba == "0":
            print("\n--- Program ukonceny ---")
            break

        else:
            print("\nZadaj spravnu hodnotu z menu.")

if __name__ == "__main__":
    kn = Kniznica()
    spusti_menu(kn)