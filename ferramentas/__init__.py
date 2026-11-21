import pandas as pd
from datetime import datetime

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

    horario_novo = []
    horarios_novos = [o for o in horarios_novos if o != "nan"]
    for n, l in enumerate(horarios_novos):
        if ":" in l:
            l = l.replace(":" , "")
            horario_novo.append(l)

    return horario_novo

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

    horario_novo = []
    horarios_novos = [o for o in horarios_novos if o != "nan"]
    for n, l in enumerate(horarios_novos):
        if ":" in l:
            l = l.replace(":" , "")
            horario_novo.append(l)

    return horario_novo

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

    horario_novo = []
    horarios_novos = [o for o in horarios_novos if o != "nan"]
    for n, l in enumerate(horarios_novos):
        if ":" in l:
            l = l.replace(":" , "")
            horario_novo.append(l)

    return horario_novo
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

    horario_novo = []
    horarios_novos = [o for o in horarios_novos if o != "nan"]
    for n, l in enumerate(horarios_novos):
        if ":" in l:
            l = l.replace(":" , "")
            horario_novo.append(l)

    return horario_novo

def separe(list):
    horarios_novos =[ l.split(":") for l in list]
    return horarios_novos

def pegar_datas():
    df = pd.read_csv('ponto.csv')
    texto = df["Data"]
    texto = [l.split(" ") for l in texto]
    datas = []

    for n,l in enumerate(texto):
        if "sáb" in l or 'dom' in l:
            pass
        else:
            datas.append(l[1])

    return datas

def calcular_horas_trabalhadas(chegada, pausa_inicio , pausa_fim , saida):
    formato = "%H%M"
    chegada = datetime.strptime(chegada , formato)
    pausa_inicio = datetime.strptime(pausa_inicio , formato)
    pausa_fim = datetime.strptime(pausa_fim , formato)
    saida = datetime.strptime(saida , formato)

    trabalho_total = (saida - chegada) - (pausa_fim - pausa_inicio)
    print(trabalho_total)

pegar_chegada()

chegada = pegar_chegada()
pausa1 = pegar_pausa1()
pausa2 = pegar_pausa2()
saida = pegar_saida()
datas = pegar_datas()
horas_trabalhadas = []

for n, l in enumerate(chegada):
    horas = calcular_horas_trabalhadas(l , pausa1[n] , pausa2[n] , saida[n])
    horas_trabalhadas.append(horas)

print(horas_trabalhadas)