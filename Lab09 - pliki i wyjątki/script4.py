"""
Lab09 - polecenia systemowe
"""
import os

print(os.listdir("C:/Users/Public/Documents"))

path = os.path.join(os.path.expanduser("~"), "Test")
print(path)

# os.mkdir(path, 0o7777)
print(os.listdir(os.path.expanduser("~")))

path2 = os.path.join(os.path.expanduser("~"), "test_1")
# os.rename(path, path2)
print(os.listdir(os.path.expanduser("~")))

(katalog, plik) = os.path.split("C:/Users/Public/Documents/desktop.ini")
print(katalog)
print(plik)

(nazwa, rozszerzenie) = os.path.splitext(plik)
print(nazwa)
print(rozszerzenie)

os.rmdir(path2)
print(os.listdir(os.path.expanduser("~")))
