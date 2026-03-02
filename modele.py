class Media:
    def __init__(self, tytul, rok_wydania, gatunek, oceny=None):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        if oceny is None:
            self.oceny = []
        else:
            self.oceny = oceny

    def __str__(self):
        return f"{self.tytul} | {self.gatunek} | {self.rok_wydania} | {self.oceny}"

    def srednia_ocen(self):
        if not self.oceny:
            return "Brak ocen"

        return round(sum(self.oceny) / len(self.oceny), 2)


class Ksiazka(Media):
    def __init__(self, autor, wydawnictwo, miejsce_wydania, tytul, rok_wydania, gatunek, oceny=None):
        super().__init__(tytul, rok_wydania, gatunek, oceny)
        self.autor = autor
        self.wydawnictwo = wydawnictwo
        self.miejsce_wydania = miejsce_wydania

    def __str__(self):
        return (
            f"Typ: Książka\n"
            f"Tytuł: {self.tytul}\n"
            f"Autor: {self.autor}\n"
            f"Rok wydania: {self.rok_wydania}\n"
            f"Gatunek: {self.gatunek}\n"
            f"Wydawnictwo: {self.wydawnictwo}\n"
            f"Miejsce wydania: {self.miejsce_wydania}\n"
            f"Średnia ocen: {self.srednia_ocen()}"
        )


class Film(Media):
    def __init__(self, rezyser, scenarzysta, producent, studio_filmowe, tytul, rok_wydania, gatunek, oceny=None):
        super().__init__(tytul, rok_wydania, gatunek, oceny)
        self.rezyser = rezyser
        self.scenarzysta = scenarzysta
        self.producent = producent
        self.studio_filmowe = studio_filmowe

    def __str__(self):
        return (
            f"Typ: Film\n"
            f"Tytuł: {self.tytul}\n"
            f"Reżyser: {self.rezyser}\n"
            f"Scenarzysta: {self.scenarzysta}\n"
            f"Producent: {self.producent}\n"
            f"Studio filmowe: {self.studio_filmowe}\n"
            f"Gatunek: {self.gatunek}\n"
            f"Rok produkcji: {self.rok_wydania}\n"
            f"Średnia ocen: {self.srednia_ocen()}"
        )


class Gra(Media):
    def __init__(self, platforma, studio, wydawca, tryb_gry, tytul, rok_wydania, gatunek, oceny=None):
        super().__init__(tytul, rok_wydania, gatunek, oceny)
        self.platforma = platforma
        self.studio = studio
        self.wydawca = wydawca
        self.tryb_gry = tryb_gry

    def __str__(self):
        return (
            f"Typ: Gra\n"
            f"Tytuł: {self.tytul}\n"
            f"Studio: {self.studio}\n"
            f"Wydawca: {self.wydawca}\n"
            f"Rok produkcji: {self.rok_wydania}\n"
            f"Platforma: {self.platforma}\n"
            f"Gatunek: {self.gatunek}\n"
            f"Tryb gry: {self.tryb_gry}\n"
            f"Średnia ocen: {self.srednia_ocen()}"
        )
