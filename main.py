from types import TracebackType
import pandas as pd
import os
from datetime import date

percorsoFile = 'C:/Users/sistemi/OneDrive/Desktop/Gestionale spese locale/database.csv'

cols = ['DataScrittura', 'NomeProdotto', 'NumArticoli', 'SpesaAcquisto', 'Vendita', 'Guadagno']

price = {
    'peroni': 1,
    'snack': 0.5,
    'bibita': 1,
    'dolci piccoli': 0.5,
    'dolci grandi': 1,
    'acqua': 0.5
}

product = ['peroni', 'snack', 'bibita', 'dolci piccoli', 'dolci grandi', 'acqua']


def checkData(path):
    """
    funzione che controlla se il database esiste, se non esiste ne crea uno nuovo
    in entrambi i casi restituisce la tabella contenente i dati dei prodotti
    """

    if os.path.isfile(path):
        df = pd.read_csv(path)
        print('Database caricato correttamente...')

    else:
        df = pd.DataFrame(columns=cols, index=None)
        print('Database creato correttamente...')

    return df


def aggiungiProdotto(df):
    """
    Funzione che serve per aggiungere/creare un database contenente i dati degli acquisti
    """

    continua = True

    while continua:

        print('1 - peroni (1€)')
        print('2 - snack (0.50€)')
        print('3 - bibita (1€)')
        print('4 - dolci piccoli (0.50€)')
        print('5 - dolci grandi (1€)')
        print('6 - acqua (0.50€)')

        prodotto = input('Seleziona i prodotti da inserire: ')
        numArticoli = input('Quanti sono i prodotti da vendere?\n')

        spesaProdotto = float(input('Quanto hai speso? (usa il punto per indicare il prezzo)\n'))
        prezzoVendita = float(price[product[int(prodotto) - 1]])
        guadagnoVendita = prezzoVendita * float(numArticoli)

        data = date.today()
        nomeProdotto = product[int(prodotto) - 1]
        numArticoli = int(numArticoli)
        spesaProdotto = float(spesaProdotto)
        guadagnoVendita = float(guadagnoVendita)
        guadagno = float(guadagnoVendita - spesaProdotto)

        to_append = [data, nomeProdotto, numArticoli, spesaProdotto, guadagnoVendita, guadagno]
        df_length = len(df)
        df.loc[df_length] = to_append

        print(df)

        df.to_csv(percorsoFile, index=False)

        risp = input('Vuoi continuare a inserire prodotti? s/n\n')

        if risp == 'n':
            continua = False


def leggiProdotto(df):
    print(df)


if __name__ == '__main__':
    tabProdotti = checkData(percorsoFile)
    flag = True

    while flag:

        print('1 - Leggi prodotti inseriti')
        print('2 - Inserisci prodotti')
        print('3 - Esci')

        ris = input("Scegli l'operazione da svolgere: ")
        ris = int(ris)

        if ris == 1:
            leggiProdotto(tabProdotti)
        elif ris == 2:
            aggiungiProdotto(tabProdotti)
        elif ris == 3:
            flag = False
