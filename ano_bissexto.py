#!/usr/bin/env python3

import sys

input = int(sys.argv[1])

if input % 4 == 0:
    print(sys.argv[1], "é um ano bissexto.")
    if input % 100 == 0:
        print(sys.argv[1], "não é um ano bissexto.")
        if input % 400 == 0:
            print(sys.argv[1], "não é um ano bissexto.")
        else:
            print(sys.argv[1], "é um ano bissexto.")
else:
    print(sys.argv[1], "não é um ano bissexto.")
