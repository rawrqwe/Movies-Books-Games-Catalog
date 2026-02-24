from manager import Manager


def main():
    manager = Manager()
    manager.wczytaj()
    while True:
        print("--MENU--")
        print("1. Dodaj pozycje (Książka/Film/Gra)")
        print("2. Usuń pozycje")
        print("3. Wyszukaj pozycje")
        print("4. Edytuj dane pozycje")
        print("5. Wyjście")
        print("6. Ocen (Książka/Film/Gra")

        try:
            user = int(input("Wybierz opcje: "))
        except ValueError:
            print("Musisz podać liczbę!")
            continue

        if user == 1:
            manager.dodaj_pozycje()
        elif user == 2:
            manager.usun()
        elif user == 3:
            manager.wyszukaj()
        elif user == 4:
            manager.pokaz_wszystkie()
        elif user == 5:
            break
        elif user == 6:
            manager.ocena()


if __name__ == "__main__":
    main()
