class Queue:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.elements = ['A', 'B', 'C', 'D']
    def is_empty(self):
        return len(self.elements) == 0

    def is_full(self):
        return len(self.elements) >= self.max_capacity

    # pridavame na koniec
    def enqueue(self, element):
        if self.is_full():
            return False
        self.elements.append(element)
        return True

    # odoberame zo zaciatku
    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)

    def content(self):
        return list(self.elements)  # vráti kópiu

    def size(self):
        return len(self.elements)


# MENU
def vypisat_menu():
    print("\n*********** MENU ************")
    print("1 - Je queue prazdny?")
    print("2 - Je queue plny?")
    print("3 - Pridat objekt do queue.")
    print("4 - Vymazat objekt z queue.")
    print("5 - Ukazat cely queue.")
    print("6 - Pocet objektov v queue.")
    print("7 - Zobrazit menu.")
    print("0 - Ukoncit program.")

def spusti_menu():
    queue = Queue(5)
    vypisat_menu()

    while True:
        volba = input("\nZadajte cislo volby z menu: ").strip()

        if volba == "1":
            print("Queue je prazdny" if queue.is_empty() else "Queue nie je prazdny")

        elif volba == "2":
            print("Queue je plny" if queue.is_full() else "Queue nie je plny")

        elif volba == "3":
            data = input("Zadaj hodnotu, ktoru chces pridat: ")
            uspech = queue.enqueue(data)
            if uspech:
                print(f"Prvok '{data}' bol pridany.")
            else:
                print("\nQueue je plny. Neda sa pridat!")

        elif volba == "4":
            vymazany_element = queue.dequeue()
            if vymazany_element is None:
                print("Queue je prazdny. Neda sa mazat.")
            else:
                print(f"Odstraneny prvok: {vymazany_element}")


        elif volba == "5":
            obsah = queue.content()
            if obsah:
                print(", ".join(obsah))
            else:
                print("Queue je prazdny.")

        elif volba == "6":
            print("Pocet prvkov v queue:", queue.size())

        elif volba == "7":
            vypisat_menu()

        elif volba == "0":
            print("\n--- Program ukonceny. ---")
            break

        else:
            print("\nZadaj spravnu hodnotu z menu.")


if __name__ == "__main__":
    spusti_menu()
