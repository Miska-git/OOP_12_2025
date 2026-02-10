import json

DATA_FILE = "countries.json"

def add_country(data, country, capital):
    key = country
    value = capital

    if key in data:
        return False

    data[key] = value
    return True

def delete_country(data, country):
    key =country
    if key not in data:
        return False
    del data[key]
    return True

def find_capital(data, country):
    key = country
    return data.get(key)


def edit_capital(data, country, new_capital):
    key = country
    if key not in data:
        return False
    data[key] = new_capital
    return True

def list_all(data):
    if not data:
        print("V zozname nie su ziadne krajiny.")
        return
    for country in sorted(data.keys()):
        print(f"{country} -> {data[country]}")


# ---------- JSON serialization (save/load) ----------

def save_to_json(data, filename = DATA_FILE):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_from_json(filename = DATA_FILE):
    try:
        with open(filename, "r") as f:
            loaded = json.load(f)
        return loaded
    except FileNotFoundError:
        return {}

# ----------MENU ----------

def print_menu() -> None:
    print("\n--- Countries & Capitals (JSON) ---")
    print("1) Pridaj krajinu")
    print("2) Zmaz krajinu")
    print("3) Najdi hlavne mesto krajiny")
    print("4) Uprav hlavne mesto krajiny")
    print("5) Vypisat vsetky krajiny a ich hlavne mesta")
    print("6) Ulozit zoznam do suboru")
    print("7) Nacitat zoznam z suboru")
    print("0) Ukonict program")


def main():
    countries = load_from_json()
    print(f"Nacitanych {len(countries)} krajin z {DATA_FILE}.")

    while True:
        print_menu()
        choice = input("Vyberte volbu z menu: ")

        if choice == "1":
            country = input("Krajina pre pridanie do zoznamu: ")
            capital = input("Hlavne mesto: ")
            if add_country(countries, country, capital):
                print("Pridane.")
            else:
                print("Krajina sa uz v zozname nachadza.")

        elif choice == "2":
            country = input("Krajina na vymazanie zo zoznamu: ")
            if delete_country(countries, country):
                print("Vymazene.")
            else:
                print("Krajina sa v zozname nenachadza.")

        elif choice == "3":
            country = input("Krajina: ")
            capital = find_capital(countries, country)
            if capital is None:
                print("Krajina sa v zozname nenachadza.")
            else:
                print(f"Hlavnym mestom {country} je {capital}.")

        elif choice == "4":
            country = input("Krajina: ")
            new_capital = input("Nove hlavne mesto: ")
            if edit_capital(countries, country, new_capital):
                print("Aktualizovane.")
            else:
                print("Krajina sa v zozname nenachadza.")

        elif choice == "5":
            list_all(countries)

        elif choice == "6":
            save_to_json(countries)
            print(f"Ulozene do: {DATA_FILE}.")

        elif choice == "7":
            countries = load_from_json()
            print(f"Naciatanych {len(countries)} krajin z {DATA_FILE}.")

        elif choice == "0":
            print("Program ukonceny.")
            break

        else:
            print("Zadali ste nespravnu volbu.")


if __name__ == "__main__":
    main()
