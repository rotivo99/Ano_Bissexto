#!/usr/bin/env python3

import sys

ano = int(sys.argv[1])

if 'ano'.isdigit():
    print('Ok, seguindo em frente.')
else:
    print('Sua entrada está errada. Insira um valor válido.')
    sys.exit()

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(ano, 'é bissexto.')
        else:
            print(ano, 'não é bissexto.')
    else:
        print(ano, 'não é bissexto.')
    print(ano, 'não é bissexto.')
print(ano, 'não é bissexto.')
