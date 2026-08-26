# Zodiac by Jessica Emberly
# Quick-Start Guide
# a = 1
# b = 2
# c = 3
# d = 4
# f = 5
# f = 6
# g = 7
# h = 8
# i = 9
# j = 10
# k = 11
# l = 12
# m = 13
# n = 14
# o = 15
# p = 16
# q = 17
# r = 18
# s = 19
# t = 20
# u = 21
# v = 22
# w = 23
# x = 24
# y = 25
# z = 26

import os
def encode():
  os.system("clear")
  encode = input("What should I encode?: ")
  dictionary = {"a": "alphabet", "b": "abs", "c": "cocaine", "d": "abide", "e": "abase", "f": "payoff", "g": "buzzing", "h": "jackfish", "i": "paparazzi", "j": "mosbolletjie", "k": "cyberattacker", "l": "ahistorically", "m": "antimodernism", "n": "acknowledgement", "o": "15", "p": "16", "q": "17", "r": "18", "s": "19", "t": "20", "u": "21", "v": "22", "w": "23", "x": "24", "y": "25", "z": "26"}
  table = str.maketrans(dictionary)
  ev = encode.translate(table)
  os.system("clear")
  print(ev)