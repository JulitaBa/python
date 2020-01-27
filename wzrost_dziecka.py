# Napisz program, który obliczy potencjalny wzrost dziecka w dorosłości.
# h = (wzrost matki + wzrost ojca)/2
# h - 6.5, dla dziewczynki
# h + 6.5, dla chłopca
# Zabezpiecz program przed błędami użytkownika.

class ZaWysoki(Exception):
    def __init__(self):
        info = "Rekord Guinessa. Najwyższy człowiek w historii miał 272 cm wzrostu."
        super().__init__(info)

class ZaNiski(Exception):
    pass

def wzrost_dziecka():
    while True:
        gender = str(input("Podaj płeć dziecka (K/M):\n")).upper()
        if gender != "M" and gender != "K":
            raise Exception("Tylko: K lub M!")
        try:
            wzrost_matki = float(input("Podaj wzrost matki:\n"))
            if wzrost_matki > 272:
                raise ZaWysoki()
            if wzrost_matki < 54.6:
                raise ZaNiski("Rekord Guinessa. Najnmniejszy odnotowany wzrost w historii to 54,6 cm.")
            wzrost_ojca = float(input("Podaj wzrost ojca:\n"))
            if wzrost_ojca > 272:
                raise ZaWysoki()
            if wzrost_ojca < 54.6:
                raise ZaNiski("Rekord Guinessa. Najnmniejszy odnotowany wzrost w historii to 54,6 cm.")
            h = (wzrost_matki + wzrost_ojca) / 2
            if gender == "K":
                 return f"Twoja córka będzie miała {h - 6.5} (+/- 5) cm wzrostu."
            if gender == "M":
                 return f"Twój syn będzie miał {h + 6.5} (+/- 5) cm wzrostu."
        except ValueError:
            print("Tylko liczby!\n")
        wzrost_dziecka()


print(wzrost_dziecka())