# -*- coding: utf-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox

from PIL import Image, ImageTk, ImageFilter

max_h = 500
max_w = 900


class Okno(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.inicjalizuj()

    def wczytaj_ponownie(self):
        self.image = ImageTk.PhotoImage(self.im)
        self.base.create_image(0, 0, image=self.image, anchor=NW)

    def wczytaj_obraz(self):
        sciezka = self.o.get()
        try:
            self.im = Image.open(sciezka)
            self.fbtn.config(state="normal")
            self.pbtn.config(state="normal")
            self.zbtn.config(state="normal")
            self.sbtn.config(state="normal")
            self.obraz_oryg = self.im
            self.wczytaj_ponownie()
        except FileNotFoundError:
            messagebox.showerror("Błąd", "Plik nie istnieje")
        except OSError:
            messagebox.showerror("Bład", "Podaj plik graficzny")

    def przywroc_obraz(self):
        # self.im = self.obraz_oryg
        self.wczytaj_ponownie()

    def inicjalizuj(self):
        self.parent.title("PjaSoft")
        self.style = Style()
        self.style.theme_use("winnative")
        self.pack(fill=BOTH, expand=1)

        lbl = Label(self, text="Ścieżka do pliku: ")
        lbl.grid(sticky=W, pady=4, padx=5)

        self.o = Entry(self)
        self.o.grid(row=1, column=0, columnspan=2, rowspan=1, pady=4, padx=5, sticky=E + W + S + N)

        self.z = Entry(self)
        self.z.grid(row=2, column=0, columnspan=2, rowspan=1, pady=4, padx=5, sticky=E + W + S + N)

        otbtn = Button(self, text="Otwórz", command=self.wczytaj_obraz)
        otbtn.grid(row=1, column=3)

        self.zbtn = Button(self, text="Zapisz")
        self.zbtn.grid(row=2, column=3)
        self.zbtn.config(state="disabled")

        self.scbox = Combobox(self, values=["0.1", "0.2", "0.3", "0.4"])
        self.scbox.grid(row=3, column=0, padx=5, pady=4, sticky=W + N)

        self.fcbox = Combobox(self, values=["BLUR", "CONTOUR", "EMBOSS"])
        self.fcbox.grid(row=4, column=0, padx=5, pady=4, sticky=W + N)

        self.sbtn = Button(self, text="Skaluj")
        self.sbtn.grid(row=3, column=1, padx=5, pady=4, sticky=W + N)
        self.sbtn.config(state="disabled")

        self.fbtn = Button(self, text="Filtruj")
        self.fbtn.grid(row=4, column=1, padx=5, pady=4, sticky=W + N)
        self.fbtn.config(state="disabled")

        self.base = Canvas(self, width=max_w, height=max_h)
        self.base.grid(row=5, column=0, padx=5, pady=4, sticky=E + W + S + N, columnspan=3)

        self.pbtn = Button(self, text="Przywróć")
        self.pbtn.grid(row=5, column=3, padx=5, pady=4, sticky=W + N)
        self.pbtn.config(state="disabled")


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()


if __name__ == "__main__":
    main()
