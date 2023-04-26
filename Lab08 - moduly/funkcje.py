"""
Lab08 - własny modułu
"""

import math
import sys


def oblicz_pole_kola(r):
    return math.pi * r ** 2


def oblicz_obwod_kola(r):
    return 2 * math.pi * r


def main():
    print(sys.argv)
    print(oblicz_pole_kola(int(sys.argv[1])))


if __name__ == "__main__":
    main()
