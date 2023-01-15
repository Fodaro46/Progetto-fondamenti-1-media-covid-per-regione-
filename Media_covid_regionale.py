import json
import requests
import matplotlib.pyplot as plt

# URL del repository: https://github.com/pcm-dpc/COVID-19
URL_dati_completi_regioni = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"

response = requests.get(URL_dati_completi_regioni)
dati = json.loads(response.text)
lista_dati_ricercati=['totale_positivi','tamponi','deceduti','totale_casi']

#Imposto i dati in base alla regione desiderata
def zona(dati,regione):
    Dati_da_Graficare_regione={}
    for dati_regione in dati:
        if dati_regione["denominazione_regione"] == regione:
            for chiave in lista_dati_ricercati:
                if chiave in dati_regione:
                    Dati_da_Graficare_regione[chiave]=dati_regione[chiave]
    return Dati_da_Graficare_regione

def dati_per_data(dati, regione):
    dati_per_data = {}
    for dati_regione in dati:
        if dati_regione["denominazione_regione"] == regione:
            data = dati_regione["data"]
            dati_per_data[data] = {}
            for chiave in lista_dati_ricercati:
                if chiave in dati_regione:
                    dati_per_data[data][chiave] = dati_regione[chiave]
    return dati_per_data

'''

#Ora non ci resta che graficare i dati ottenuti
def Grafico_regionale(regione, lista_dati_ricercati):
    dati_regione = dati_per_data(dati, regione)
    for data in dati_regione:
        Dati_da_Graficare = dati_regione[data]
        plt.bar(Dati_da_Graficare.keys(), Dati_da_Graficare.values(), color='red')
        plt.title("Dati COVID-19 per la regione di " + regione)
        plt.xticks(rotation=90)
        plt.suptitle("Data: " + data, fontsize=10)
        plt.xlabel("Dati")
        plt.ylabel("Valori")
        plt.yscale('log')
        plt.grid()
        plt.show()
    return

'''
#mettiamo caso che la regione da noi considerata è l'umbria
#dati giornalieri
'''print(Grafico_regionale('Umbria',lista_dati_ricercati))'''
#dati ultimi
'''print(zona(dati,'Umbria'))'''


def media_regionale(dati, regione, lista_dati_ricercati):
    dati = dati_per_data(dati,regione)
    media_per_dato = {}
    for dato in lista_dati_ricercati:
        somma = 0
        conteggio = 0
        for data in dati:
            if dati[data][dato] is not None:
                somma += dati[data][dato]
                conteggio += 1
        media_per_dato[dato] = somma/conteggio
    return media_per_dato

print(media_regionale(dati,'Calabria',lista_dati_ricercati))

def Grafico_mediano_regionale(regione):
    dati_mediani_regionali = media_regionale(dati, regione, lista_dati_ricercati)
    plt.bar(dati_mediani_regionali.keys(), dati_mediani_regionali.values(), color='red')
    plt.title("Dati COVID-19 per la regione di " + regione)
    plt.xticks(rotation=90)
    #plt.suptitle("Data: " + data, fontsize=10)
    plt.xlabel("Dati")
    plt.ylabel("Valori")
    plt.yscale('log')
    plt.grid()
    plt.show()
    return
print(Grafico_mediano_regionale('Calabria'))
