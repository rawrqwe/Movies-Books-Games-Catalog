class Media:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek


class Ksiazka(Media):
    def __init__(self, autor, wydawnictwo, miejsce_wydania, tytul, rok_wydania, gatunek):
        super().__init__(tytul, rok_wydania, gatunek)
        self.autor = autor
        self.wydawnictwo = wydawnictwo
        self.miejsce_wydania = miejsce_wydania

    def __str__(self):
        return (f"Książka: {self.tytul}\n"
                f"Autor: {self.autor}\n"
                f"Rok wydania: {self.rok_wydania}\n"
                f"Gatunek: {self.gatunek}\n"
                f"Wydawnictwo: {self.wydawnictwo}\n"
                f"Miejsce wydania: {self.miejsce_wydania}")


class Film(Media):
    def __init__(self, rezyser, scenarzysta, producent, studio_filmowe, tytul, rok_wydania, gatunek):
        super().__init__(tytul, rok_wydania, gatunek)
        self.rezyser = rezyser
        self.scenarzysta = scenarzysta
        self.producent = producent
        self.studio_filmowe = studio_filmowe
        self.gatunek = gatunek

    def __str__(self):
        return (f"Film: {self.tytul}\n"
                f"Reżyser: {self.rezyser}\n"
                f"Scenarzysta: {self.scenarzysta}\n"
                f"Producent: {self.producent}\n"
                f"Studio filmowe: {self.studio_filmowe}\n"
                f"Gatunek: {self.gatunek}\n"
                f"Rok produkcji: {self.rok_wydania}")


class Gra(Media):
    def __init__(self, platforma, studio, wydawca, tryb_gry, tytul, rok_wydania, gatunek):
        super().__init__(tytul, rok_wydania, gatunek)
        self.platforma = platforma
        self.studio = studio
        self.wydawca = wydawca
        self.tryb_gry = tryb_gry
        self.gatunek = gatunek

    def __str__(self):
        return (f"Gra: {self.tytul}\n"
                f"Studio: {self.studio}\n"
                f"Wydawca: {self.wydawca}\n"
                f"Rok produkcji: {self.rok_wydania}\n"
                f"Platforma: {self.platforma}\n"
                f"Gatunek: {self.gatunek}\n"
                f"Tryb gry: {self.tryb_gry}")


ksiazka = Ksiazka("rafal", "Romans", "Agora", 1993, "Balanda", "dramat")
print(f"{ksiazka}")
print("*" * 30)
film = Film("rafal", "rafal", "rafal", "Rafal studio", "Ogniem i mieczem", 1933, "dramat")
print(f"{film}")
