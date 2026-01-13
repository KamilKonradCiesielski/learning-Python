# W pełnej talii jest 52 karty, Wartości kart:

#2–10 – wartość równa liczbie na karcie

#Walet (J) – 2 pkt

#Dama (Q) – 3 pkt

#Król (K) – 4 pkt

#As (A) – 11 pk

import random

def talia_pik():
    pik = []
    for r in rangi:
        pik.append(f"{r} pik")
    return pik

def talia_karo():
    karo = []
    for r in rangi:
        karo.append(f"{r} karo")
    return karo

def talia_trefl():
    trefl = []
    for r in rangi:
        trefl.append(f"{r} trefl")
    return trefl

def talia_kier():
    kier = []
    for r in rangi:
        kier.append(f"{r} kier")
    return kier

def talia_pełna():
    talia = talia_pik() + talia_karo() + talia_trefl() + talia_kier()
    return talia

def punktacja_kart(karty_gracza):

    suma = 0

    for karta in karty_gracza:

        punkty_karty = karta.split() #tutaj mamy stringi

        wartosc_karty = punkty_karty[0] #tutaj dostajemy tez stringi

        wartosc_karty = punkty.get(wartosc_karty,0)

        suma = suma + wartosc_karty

    return (suma)

licznik = 0
rangi = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
punkty = {
"2":2,
"3":3,
"4":4,
"5":5,
"6":6,
"7":7,
"8":8,
"9":9,
"10":10,
"J": 2,
"Q": 3,
"K": 4,
"A": 11,
}
karty_gracza = []
karty_krupiera = []
talia = talia_pełna() # nie widziałem że można zrobić zmienną dla całej funkcji
random.shuffle(talia)
karta = random.choice(talia)
#print(karta)

liczba_rozdan = int(input("Ile chcesz grac rozdan, podaj liczbe z zakresu 1-10:"))

while licznik < liczba_rozdan:
    karty_gracza =[]
    karty_krupiera = []
    print(f"Rozpoczynamy rozdanie numer {licznik + 1}.")
    karty_gracza.append(talia.pop())
    karty_krupiera.append(talia.pop())
    suma_punktow_gracza = punktacja_kart(karty_gracza)
    suma_punktow_krupiera = punktacja_kart(karty_krupiera)
    czy_gracz_dobiera = True
    czy_krupier_dobiera = True
    print(f"Twoje karty to: {karty_gracza} a suma punktów: {suma_punktow_gracza}")
    while suma_punktow_gracza <= 21 and czy_gracz_dobiera:

        decyzja_gracza = input("Bierzesz czy stoisz? Jeśli bierzesz wpisz 'b', jeśli stoisz wpisz 's'.")

        if suma_punktow_gracza > 21:
            czy_gracz_dobiera = False
            print("Gracz Bust!")
            break

        if decyzja_gracza == 'b':
            # Krok 3: Dodaj kartę, zaktualizuj sumę punktów
            czy_gracz_dobiera = True
            karty_gracza.append(talia.pop())
            suma_punktow_gracza = punktacja_kart(karty_gracza)
            print(f"Twoje karty to: {karty_gracza} a suma punktów: {suma_punktow_gracza}")

        elif decyzja_gracza == 's':
            czy_gracz_dobiera = False
            break

        else:
            print("Niepoprawny wybór.")


    while suma_punktow_krupiera < 17:
        karty_krupiera.append(talia.pop())
        suma_punktow_krupiera = punktacja_kart(karty_krupiera)
        print(f"Krupier dobiera. Karty krupiera: {karty_krupiera} | Suma: {suma_punktow_krupiera}")

    if suma_punktow_krupiera > 21:
        print("Krupier spuchł (Bust)!")

# match summary - results

    print("\n *** PODSUMOWANIE ***");
    if suma_punktow_gracza > 21:
        print(f"PRZEGRAŁEŚ! Masz {suma_punktow_gracza} pkt. (Przekroczyłeś 21)")
    elif suma_punktow_krupiera > 21:
        print(f"WYGRAŁEŚ! Krupier ma {suma_punktow_krupiera} pkt. (Krupier przekroczył 21)")
    elif suma_punktow_gracza > suma_punktow_krupiera:
        print(f"WYGRAŁEŚ! Twój wynik: {suma_punktow_gracza}, Krupier: {suma_punktow_krupiera}")
    elif suma_punktow_gracza < suma_punktow_krupiera:
        print(f"PRZEGRAŁEŚ! Twój wynik: {suma_punktow_gracza}, Krupier: {suma_punktow_krupiera}")
    else:
        print(f"REMIS! Obaj macie po {suma_punktow_gracza} pkt.")

    licznik += 1
