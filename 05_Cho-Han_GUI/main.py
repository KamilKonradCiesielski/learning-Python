import tkinter as tk
import random

class Menu:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg = "black")
        self.frame.pack(expand=True,fill="both")
        naglowek = tk.Label(self.frame, text = "Cho - Han", font=("Courier", 14, "bold"), fg="black", bg="white", bd = 1)
        naglowek.pack(expand=True, fill="both")
        start_gre = tk.Button(self.frame, text="Start", command = self.zacznij_gre, fg="white", bg="black", bd = 1, font=("Courier", 12, "bold"))
        start_gre.pack(expand=True, fill="both")
        koniec_gry = tk.Button(self.frame, text="Quit", command = self.root.destroy, fg="black", bg="white", bd = 1, font=("Courier", 12, "bold"))
        koniec_gry.pack(expand=True, fill="both")

    def zacznij_gre(self):
        self.frame.destroy()
        GryWidok(self.root)

class GryWidok:

    def sprawdz_wynik(self, wybor_gracza):

        kostka_pierwsza = random.randint(1, 6)
        kostka_druga = random.randint(1, 6)
        suma_kostek = kostka_pierwsza + kostka_druga

        print(f"Kostka pierwsza: {kostka_pierwsza}")
        print(f"Kostka druga: {kostka_druga}")
        print(f"Suma kostek: {suma_kostek}")

        if (suma_kostek % 2 == 0) and (wybor_gracza == "p") or (suma_kostek % 2 !=0) and (wybor_gracza == "n"):
            self.komunikat.config(text="Wygrałeś!")
            self.kostka_pierwsza.config(text = f"Kostka pierwsza: {kostka_pierwsza}")
            self.kostka_druga.config(text = f"Kostka druga: {kostka_druga}")
            self.suma_kostek.config(text = f"Suma kostek: {suma_kostek}")
        elif (suma_kostek % 2 == 0) and (wybor_gracza== "n") or (suma_kostek % 2 !=0) and (wybor_gracza == "p"):
            self.komunikat.config(text = "Przegrałeś!")
            self.kostka_pierwsza.config(text = f"Kostka pierwsza: {kostka_pierwsza}")
            self.kostka_druga.config(text = f"Kostka druga: {kostka_druga}")
            self.suma_kostek.config(text = f"Suma kostek: {suma_kostek}")
        self.root.after(4000, self.spauzuj)

    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg = "black")
        self.frame.pack(expand=True,fill="both")
        self.komunikat = tk.Label(self.frame, text = "Co obstawiasz, liczby parzyste czy nieparzyste?",  fg="black", bg="white", bd = 0, font=("Courier", 12, "bold"))
        self.komunikat.pack(expand=True, fill="both")
        self.kostka_pierwsza = tk.Label(self.frame, text = "Kostka pierwsza:", fg="white", bg="black", bd = 1, font=("Courier", 12, "bold"))
        self.kostka_pierwsza.pack(expand=True)
        self.kostka_druga = tk.Label(self.frame, text = "Kostka druga:", fg="white", bg="black", bd = 1, font=("Courier", 12, "bold"))
        self.kostka_druga.pack(expand=True)
        self.suma_kostek = tk.Label(self.frame, text = "Suma kostek:", fg="white", bg="black", bd = 1, font=("Courier", 12, "bold"))
        self.suma_kostek.pack(expand=True)
        #przyciski
        self.przycisk_p = tk.Button(self.frame, text="Parzyste", command=lambda: self.sprawdz_wynik("p"), fg="black", bg="white", bd = 1, font=("Courier", 12, "bold"))
        self.przycisk_n = tk.Button(self.frame, text="Nieparzyste", command=lambda: self.sprawdz_wynik("n"), fg="black", bg="white", bd = 1, font=("Courier", 12, "bold"))
        self.przycisk_p.pack(expand=True, fill="both")
        self.przycisk_n.pack(expand=True, fill="both")

    def spauzuj(self):
        self.frame.destroy()
        PauzaEkran(self.root)

class PauzaEkran:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root, bg = "black")
        self.frame.pack(expand=True,fill="both")

        naglowek = tk.Label(self.frame, text = "Cho - Han", font=("Courier", 14, "bold"), fg="white", bg="black", bd = 1)
        naglowek.pack(expand=True, fill ="both")

        graj_ponownie = tk.Button(self.frame, text="Graj jeszcze raz", command = self.zacznij_gre, fg="black", bg="white", bd = 1, font=("Courier", 12, "bold"))
        graj_ponownie.pack(expand=True, fill ="both")
        koniec_gry = tk.Button(self.frame, text="Quit", command = self.root.destroy, fg="white", bg="black", bd = 1, font=("Courier", 12, "bold"))
        koniec_gry.pack(expand=True, fill ="both")

    def zacznij_gre(self):
        self.frame.destroy()
        GryWidok(self.root)

root = tk.Tk()            # Tworzysz bazę (fundament)
root.geometry("1000x600")
app = Menu(root)          # Przekazujesz bazę do klasy (ekipa wchodzi do środka)
root.mainloop()           # Uruchamiasz prąd w budynku (pętla gry)
