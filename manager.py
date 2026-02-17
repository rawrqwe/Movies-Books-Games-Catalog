from modele import Ksiazka, Film, Gra

def dodawanie_ksiazek():
    autor = input("Podaj autora: ").lower()
    tytul = input("Podaj tytuł: ").lower()
    gatunek = input("Podaj gatunek: ").lower()
    data_wydania = input("Podaj date wydania(dd/mm/rr): ")
    wydawca = input("Podaj wydawce: ").lower()
    ocena = input("Podaj ocenę(0-10): ")
    opis = input("Napisz krótki opis: ").lower()

    ksiazka = {
        "autor": autor,
        "tytul": tytul,
        "gatunek": gatunek,
        "rok wydania": data_wydania,
        "wydawca": wydawca,
        "ocena": ocena,
        "opis": opis
    }

    print("Dodano nowa ksiażkę!")
    return ksiazka