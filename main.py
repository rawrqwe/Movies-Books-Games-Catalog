from manager import Manager


def main():
    manager = Manager()
    manager.wczytaj()
    try:
        while True:
            print("\n--MENU--")
            print("1. Dodaj pozycje (Książka/Film/Gra)")
            print("2. Usuń pozycje")
            print("3. Wyszukaj pozycje")
            print("4. Edytuj dane")
            print("5. Oceń (Książka/Film/Gra)")
            print("6. Pokaz wszystkie zapisane pozycje")
            print("7. Wyjście")

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
                wynik = manager.wyszukaj()
                if wynik:
                    print(wynik)
                else:
                    print("Nie znaleziono!")
            elif user == 4:
                manager.edycja_danych()
            elif user == 5:
                manager.ocena()
            elif user == 6:
                manager.pokaz_wszystkie()
            elif user == 7:
                break
            else:
                print("Nieprawidłowy wybór!")
    finally:
        manager.zapisz(komunikat=False)
        print(f"Dane zapisane przy zamykaniu programu.")


if __name__ == "__main__":
    main()
