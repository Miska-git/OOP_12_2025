# PRODUKT
class Pasta:
    def __init__(self, typ, omacka=None, topping=None, dresing=None):
        self.typ = typ
        self.omacka = omacka
        self.topping = topping
        self.dresing = dresing

    def __str__(self):
        return (
            f"\nTvoja pasta:\n"
            "-------------------\n"
            f"Typ: {self.typ}\n"
            f"Omáčka: {self.omacka if self.omacka else 'Bez omáčky'}\n"
            f"Topping: {self.topping if self.topping else 'Bez toppingu'}\n"
            f"Dresing: {self.dresing if self.dresing else 'Bez dresingu'}\n"
            "-------------------\n"
            "Sám si si vybral :) - Dobrú chuť!"
        )

# BUILDER
class PastaBuilder:
    def __init__(self):
        self.typ = None
        self.omacka = None
        self.topping = None
        self.dresing = None

    def add_typ(self, typ):
        self.typ = typ
        return self

    def add_omacka(self, omacka):
        self.omacka = omacka
        return self

    def add_topping(self, topping):
        self.topping = topping
        return self

    def add_dresing(self, dresing):
        self.dresing = dresing
        return self

    def build(self):
        return Pasta(self.typ, self.omacka, self.topping, self.dresing)


# UZIVATELSKE ROZHRANIE
def main():
    builder = PastaBuilder()
    print("\nVyskladaj si vlastnú pastu:")
    print("----------------------------")

    # ---- Typ cestovín (povinné) ----
    while True:
        print("Vyber typ cestovín:")
        print("1. Spaghetti")
        print("2. Pappardelle")
        print("3. Kolienka")

        volba = input("Číslo: ")
        if volba == "1":
            builder.add_typ("Spaghetti")
            break
        elif volba == "2":
            builder.add_typ("Pappardelle")
            break
        elif volba == "3":
            builder.add_typ("Kolienka")
            break
        else:
            print("Neplatná voľba. Vyber správny typ cestoviny zo zoznamu! Iné typy nemáme.")


    # ---- Omáčka  ----
    print("\nVyber omáčku:")
    print("1 - Bolognese")
    print("2 - Alfredo")
    print("3 - Bryndzová omáčka s hubami")
    print("0 - Bez omáčky")

    volba = input("Číslo: ")
    if volba == "1":
        builder.add_omacka("Bolognese")
    elif volba == "2":
        builder.add_omacka("Alfredo")
    elif volba == "3":
        builder.add_omacka("Bryndzová omáčka s hubami")
    elif volba == "0":
        builder.add_omacka("Bez omáčky")
    else:
        builder.add_omacka(None)
        print ("Zadal si nespravnu volbu. Tvoja cestovina bude bez omáčky.")

    # ---- Topping  ----
    print("\nVyber topping:")
    print("1. Parmezán")
    print("2. Mozzarella")
    print("3. Kuracie kúsky")
    print("0. Bez toppingu")

    volba = input("Číslo: ")
    if volba == "1":
        builder.add_topping("Parmezán")
    elif volba == "2":
        builder.add_topping("Mozzarella")
    elif volba == "3":
        builder.add_topping("Kuracie kúsky")
    elif volba == "0":
        builder.add_omacka("Bez toppingu")
    else:
        builder.add_omacka(None)
        print("Zadal si nespravnu volbu. Tvoja cestovina bude bez toppingu.")

    # ---- Dresing  ----
    print("\nVyber dresing:")
    print("1. Olivový olej")
    print("2. Cesnakový dresing")
    print("3. Kefírový dresing s avokádom")
    print("0. Bez dresingu")

    volba = input("Číslo: ")
    if volba == "1":
        builder.add_dresing("Olivový olej")
    elif volba == "2":
        builder.add_dresing("Cesnakový dresing")
    elif volba == "3":
        builder.add_dresing("Kefírový dresing s avokádom")
    elif volba == "0":
        builder.add_omacka("Bez dresingu")
    else:
        builder.add_omacka(None)
        print("Zadal si nespravnu volbu. Tvoja cestovina bude bez dresingu.")

    pasta = builder.build()
    print(pasta)


# SPUSTENIE
if __name__ == "__main__":
    main()
