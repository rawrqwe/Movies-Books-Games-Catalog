from modele import Ksiazka, Film, Gra
import json


class Manager:
    def __init__(self):
        self.media_list = []

    def dodaj_pozycje(self):
        typ = input("Podaj typ (Książka/Film/Gra): ").lower()
        tytul = input("Podaj tytuł: ").title()
        rok_wydania = int(input("Podaj rok: "))
        gatunek = input("Podaj gatunek: ").title()

        if typ == "książka":
            autor = input("Podaj autor: ").title()
            wydawnictwo = input("Podaj wydawnictwo: ").title()
            miejsce_wydania = input("Podaj miejsce wydania: ").title()

            obiekt = Ksiazka(autor, wydawnictwo, miejsce_wydania, tytul, rok_wydania, gatunek)
        elif typ == "film":
            rezyser = input("Reżyser: ").title()
            scenarzysta = input("Scenarzysta: ").title()
            producent = input("Producent: ").title()
            studio_filmowe = input("Studio filmowe: ").title()

            obiekt = Film(rezyser, scenarzysta, producent, studio_filmowe, tytul, rok_wydania, gatunek)
        elif typ == "gra":
            platforma = input("Platforma: ").title()
            studio = input("Studio: ").title()
            wydawca = input("Wydawca: ").title()
            tryb_gry = input("Tryb gry: ").title()

            obiekt = Gra(platforma, studio, wydawca, tryb_gry, tytul, rok_wydania, gatunek)
        else:
            print("Niepoprawny typ!")
            return

        self.media_list.append(obiekt)
        self.zapisz()
        print("Dodano pomyślnie!")

    def wyszukaj(self):
        tytul = input("Podaj tytuł do wyszukania: ").strip().lower()

        for item in self.media_list:
            if item.tytul.strip().lower() == tytul:
                print("\nZnaleziono!")
                return item

        return None

    def usun(self):
        tytul = input("Podaj tytuł do usunięcia: ").strip().lower()

        for item in self.media_list:
            if item.tytul.strip().lower() == tytul:
                self.media_list.remove(item)
                self.zapisz()
                print("\nZnaleziono!")
                print(f"Pozycja '{tytul.title()}' została usunięta")
                return

        print("Nie znaleziono!")

    def pokaz_wszystkie(self):
        if not self.media_list:
            print("Brak pozycji.")
            return

        for item in self.media_list:
            print(f"Typ: {item.typ} | Tytuł: {item.tytul} | Rok wydania: {item.rok_wydania} | Średnia ocen: {item.srednia_ocen()}")

    def zapisz(self, komunikat=True):
        dane = []
        for item in self.media_list:
            rekord = vars(item).copy()  # vars zwraca słownik wszystkich atrybutów instancji
            rekord["typ"] = item.typ  # Bo JSON sam nie wie, jaką klasą był obiekt
            dane.append(rekord)

        with open("dane.json", "w", encoding="utf-8") as f:  # w - nadpisuje plik/ tworzy jak nie ma
            json.dump(dane, f, indent=4)  # co_zapisać, gdzie_zapisać, opcje
        # f- otwarty plik | indent=4 - ładne formatowanie

        if komunikat:
            print("Zapisano!")

    def wczytaj(self):
        try:
            with open("dane.json", "r", encoding="utf-8") as f:  # r - tylko odczyt
                dane = json.load(f)

            self.media_list = []

            for rekord in dane:
                typ = rekord.pop("typ")  # usuwa typ ze słownika

                if typ == "Ksiażka":
                    obiekt = Ksiazka(**rekord)  # rozpakuj słownik jako argumenty nazwane
                elif typ == "Film":
                    obiekt = Film(**rekord)
                elif typ == "Gra":
                    obiekt = Gra(**rekord)
                else:
                    continue

                self.media_list.append(obiekt)

            print("Wczytano dane z pliku.")

        except FileNotFoundError:
            print("Brak pliku do wczytania — start z pustą bazą danych.")

    def ocena(self):
        tytul = input("Podaj tytuł do ocenienia: ").strip().lower()
        for item in self.media_list:
            if item.tytul.strip().lower() == tytul:
                while True:
                    try:
                        ocena = float(input("Podaj ocenę (0-10): "))
                        if 0 <= ocena <= 10:
                            item.oceny.append(ocena)
                            self.zapisz()
                            print("Dodano ocenę!")
                            return
                        else:
                            print("Ocena musi być w zakresie 0-10!")
                    except ValueError:
                        print("Podaj liczbę!")

        print("Nie znaleziono pozycji.")

    def edycja_danych(self):
        typ = input("Podaj typ (Ksiazka/Film/Gra): ").lower()
        tytul = input("Podaj tytuł do edycji: ").strip().lower()

        for item in self.media_list:
            if item.tytul.strip().lower() == tytul:

                if typ == "ksiazka":
                    self.edytuj_ksiazke(item)
                elif typ == "film":
                    self.edytuj_film(item)
                elif typ == "gra":
                    self.edytuj_gre(item)

                return

        print("Nie znaleziono pozycji.")

    def edytuj_ksiazke(self, item):

        while True:

            print("\nCo chcesz edytować?")
            print("1. Tytuł")
            print("2. Autor")
            print("3. Rok wydania")
            print("4. Gatunek")
            print("5. Wydawnictwo")
            print("6. Miejsce wydania")
            print("7. Wyjście")

            try:
                wybor = int(input("Podaj wybór: "))

                if wybor == 1:
                    item.tytul = input("Nowy tytuł: ")
                elif wybor == 2:
                    item.autor = input("Nowy autor: ")
                elif wybor == 3:
                    try:
                        item.rok_wydania = int(input("Nowy rok: "))
                    except ValueError:
                        print("Podaj poprawny rok!")
                elif wybor == 4:
                    item.gatunek = input("Nowy gatunek: ")
                elif wybor == 5:
                    item.wydawnictwo = input("Nowe wydawnictwo: ")
                elif wybor == 6:
                    item.miejsce_wydania = input("Nowe miejsce wydania: ")
                elif wybor == 7:
                    self.zapisz()
                    return

                else:
                    print("Nieprawidłowy wybór!")

            except ValueError:
                print("Podaj poprawną liczbę!")

    def edytuj_film(self, item):

        while True:

            print("\nCo chcesz edytować?")
            print("1. Tytuł")
            print("2. Reżyser")
            print("3. Scenarzysta")
            print("4. Producent")
            print("5. Studio filmowe")
            print("6. Gatunek")
            print("7. Rok produkcji")
            print("8. Wyjście")

            try:
                wybor = int(input("Podaj wybór: "))

                if wybor == 1:
                    item.tytul = input("Nowy tytuł: ")
                elif wybor == 2:
                    item.rezyser = input("Nowy reżyser: ")
                elif wybor == 3:
                    item.scenarzysta = input("Nowy scenarzysta: ")
                elif wybor == 4:
                    item.producent = input("Nowy producent: ")
                elif wybor == 5:
                    item.studio_filmowe = input("Nowe studio filmowe: ")
                elif wybor == 6:
                    item.gatunek = input("Nowy gatunek: ")
                elif wybor == 7:
                    try:
                        item.rok_wydania = int(input("Nowy rok: "))
                    except ValueError:
                        print("Podaj poprawny rok!")
                elif wybor == 8:
                    self.zapisz()
                    return
                else:
                    print("Nieprawidłowy wybór!")


            except ValueError:
                print("Podaj poprawną liczbę!")

    def edytuj_gre(self, item):

        while True:

            print("\nCo chcesz edytować?")
            print("1. Tytuł")
            print("2. Studio")
            print("3. Wydawca")
            print("4. Rok produkcji")
            print("5. Platforma")
            print("6. Gatunek")
            print("7. Tryb gry")
            print("8. Wyjście")

            try:
                wybor = int(input("Podaj wybór: "))

                if wybor == 1:
                    item.tytul = input("Nowy tytuł: ")
                elif wybor == 2:
                    item.studio = input("Nowe studio: ")
                elif wybor == 3:
                    item.wydawca = input("Nowy wydawca: ")
                elif wybor == 4:
                    try:
                        item.rok_wydania = int(input("Nowy rok: "))
                    except ValueError:
                        print("Podaj poprawny rok!")
                elif wybor == 5:
                    item.platforma = input("Nowa platforma: ")
                elif wybor == 6:
                    item.gatunek = input("Nowy gatunek: ")
                elif wybor == 7:
                    item.tryb_gry = input("Nowy tryb gry: ")
                elif wybor == 8:
                    self.zapisz()
                    return
                else:
                    print("Nieprawidłowy wybór!")

            except ValueError:
                print("Podaj poprawną liczbę!")