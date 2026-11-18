import pandas as pd

def pegar_chegada():
    df = pd.read_csv('ponto.csv')
    texto = df["Ponto 1"]
    horarios = []
    horarios_novos = []

    for n,l in enumerate(texto):
        if l == "nan":
            continue

        elif n % 2 == 0:
            horarios.append(l)

    for a,b in enumerate(horarios):
        horarios = str(b)[0:5]
        horarios_novos.append(horarios)

    horarios_novos = [o for o in horarios_novos if o != "nan"]

    return horarios_novos

def pegar_pausa1():
    df = pd.read_csv('ponto.csv')
    texto = df["Ponto 2"]
    horarios = []
    horarios_novos = []

    for n,l in enumerate(texto):
        if l == "nan":
            continue

        elif n % 2 == 0:
            horarios.append(l)

    for a,b in enumerate(horarios):
        horarios = str(b)[0:5]
        horarios_novos.append(horarios)

    horarios_novos = [o for o in horarios_novos if o != "nan"]

    return horarios_novos

def pegar_pausa2():
    df = pd.read_csv('ponto.csv')
    texto = df["Ponto 3"]
    horarios = []
    horarios_novos = []

    for n,l in enumerate(texto):
        if l == "nan":
            continue

        elif n % 2 == 0:
            horarios.append(l)

    for a,b in enumerate(horarios):
        horarios = str(b)[0:5]
        horarios_novos.append(horarios)

    horarios_novos = [o for o in horarios_novos if o != "nan"]

    return horarios_novos

def pegar_saida():
    df = pd.read_csv('ponto.csv')
    texto = df["Ponto 4"]
    horarios = []
    horarios_novos = []

    for n,l in enumerate(texto):
        if l == "nan":
            continue

        elif n % 2 == 0:
            horarios.append(l)

    for a,b in enumerate(horarios):
        horarios = str(b)[0:5]
        horarios_novos.append(horarios)

    horarios_novos = [o for o in horarios_novos if o != "nan"]

    return horarios_novos