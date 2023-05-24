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


def main():
    gui = Tk()
    gui.geometry("1000x700")
    app = Okno(gui)
    gui.mainloop()


if __name__ == "__main__":
    main()
