from numere import numere
import random
from art import logo


numar_random = random.choice(numere)
print(numar_random)


def comparare_numere():
  print(logo)
  flag = True
  vieti = 0
  alegere_dificultate = input("Alege dificultatea ta! usor/greu\n>")
  if alegere_dificultate == 'usor':
    vieti = 10
  elif alegere_dificultate == 'greu':
    vieti = 5
  while flag:
    numar = int(input("Alege un numar intre 1 si 100\n>"))
    if numar > 100 or numar < 1:
      print("Alege un numar din interval!!")
    if numar_random > numar:
      print("Prea mic!")
      vieti -=1
      print(f"Ai mai ramas cu {vieti} vieti!")
    elif numar_random < numar:
      print("Prea mare!")
      vieti -=1
      print(f"Ai mai ramas cu {vieti} vieti!")
    else:
      print(f"Ai castigat numarul era {numar_random}!")
      print(f"Ai mai ramas cu {vieti} vieti!")
      flag = False
    if vieti == 0:
      print(f"Ai ramas fara vieti, numarul corect era {numar_random}")
      flag = False