from modele import Ksiazka, Film, Gra
import json

class Manager:
    def __init__(self):
        self.media_list = []

    def dodaj_pozycje(self):
        typ = input("Podaj typ (ksiazka/film/gra): ").lower()
        tytul = input("Podaj tytuł: ").title()
        rok_wydania = int(input("Podaj rok: "))
        gatunek = input("Podaj gatunek: ").title()

        if typ == "ksiazka":
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
        tytul = input("Podaj tytuł do wyszukania: ").title()
        for item in self.media_list:
            if item.tytul.lower() == tytul.lower():
                print("Znaleziono:", item.tytul, item.rok, item.gatunek)
                return item
        print("Nie znaleziono.")
        return None

    def usun(self):
        tytul = input("Podaj tytuł do usunięcia: ").title()
        self.media_list = [
            m for m in self.media_list if m.tytul == tytul
        ]
        self.zapisz()
        print("Jeśli istniało — zostało usunięte.")

    def pokaz_wszystkie(self):
        if not self.media_list:
            print("Brak pozycji.")
            return

        for item in self.media_list:
            print(
                item.tytul,
                "|",
                item.rok,
                "|",
                item.gatunek,
                "| Średnia ocen:",
                item.srednia_ocen(),
            )

    def zapisz(self):
        dane = []
        for item in self.media_list:
            rekord = vars(item).copy()  # vars zwraca słownik wszystkich atrybutów instancji
            rekord["typ"] = item.__class__.__name__  # Bo JSON sam nie wie, jaką klasą był obiekt
            dane.append(rekord)

        with open("dane.json", "w", encoding="utf-8") as f:  # w - nadpisuje plik/ towrzy jak nie ma
            json.dump(dane, f, indent=4)  # co_zapisać, gdzie_zapisać, opcje
        # f- otwarty plik | indent=4 - ładne formatowanie
        print("Zapisano do pliku.")

    def wczytaj(self):
        try:
            with open("dane.json", "r", encoding="utf-8") as f:  # r - tylko odczyt
                dane = json.load(f)

            self.media_list = []

            for rekord in dane:
                typ = rekord.pop("typ")  # usuwa typ ze słownika

                if typ == "ksiazka":
                    obiekt = Ksiazka(**rekord)  # rozpakuj słownik jako argumenty nazwane
                elif typ == "film":
                    obiekt = Film(**rekord)
                elif typ == "gra":
                    obiekt = Gra(**rekord)
                else:
                    continue

                self.media_list.append(obiekt)

            print("Wczytano dane z pliku.")

        except FileNotFoundError:
            print("Brak pliku do wczytania — start z pustą bazą danych.")

    def ocena(self):
        tytul = input("Podaj tytuł do ocenienia: ").lower()
        for item in self.media_list:
            if item.tytul == tytul:
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
