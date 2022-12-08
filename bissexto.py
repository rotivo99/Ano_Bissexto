#!/usr/bin/env python3

import sys

ano = int(sys.argv[1])

if (ano % 4 != 0):
    print(ano, "não é um ano bissexto.")
elif(ano % 100 != 0):
    print(ano, "é um ano bissexto.")
elif(ano % 400 != 0):
    print(ano, "não é um ano bissexto.")
else:
    print(ano, "é um ano bissexto.")
