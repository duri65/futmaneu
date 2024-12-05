#!/usr/bin/python
from itertools import combinations
from datetime import datetime, timedelta

def generuj_turnaj():
    ucastnici = ['Tím 1', 'Tím 2', 'Tím 3', 'Tím 4', 'Tím 5', 'Tím 6', 'Tím 7']
    ihriska = ['Ihrisko 1', 'Ihrisko 2']
    cas_zaciatku = datetime(2023, 7, 1, 9, 0)  # Zmeniť na požadovaný dátum a čas začiatku

    zapasy = []
    for domaci, hostia in combinations(ucastnici, 2):
        for ihrisko in ihriska:
            zapas = {
                'domaci': domaci,
                'hostia': hostia,
                'cas': cas_zaciatku
            }
            zapasy.append(zapas)
            cas_zaciatku += timedelta(minutes=20)
        cas_zaciatku += timedelta(minutes=5)

    return zapasy

# Testovanie vygenerovanej turnajovej sady
turnaj = generuj_turnaj()
for zapas in turnaj:
    print(f"{zapas['domaci']} vs. {zapas['hostia']} - {zapas['cas']}")
