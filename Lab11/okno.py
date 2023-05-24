# -*- coding: utf-8 -*-

from tkinter import BOTH, Tk, W, E, N, S, Canvas, NW, messagebox
from tkinter.ttk import Frame, Style, Label, Entry, Button, Combobox


class Okno(Frame):
    def __int__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.inicjalizuj()

    # def wczytaj_obraz(self):
    #    sciezka = self.o.get()

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
        self.z.grid(row=1, column=1, columnspan=2, rowspan=1, pady=4, padx=5, sticky=E + W + S + N)

        otbtn = Button(self, text="Otwórz")
        otbtn.grid(row=1, column=3)

        self.zbtn = Button(self, text="Zapisz")
        self.zbtn.grid(row=2, column=3)
        self.zbtn.config(state="disable")


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()


if __name__ == "__main__":
    main()
