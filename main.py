import ferramentas as f
import pandas as pd

chegada = f.pegar_chegada()
pausa1 = f.pegar_pausa1()
pausa2 = f.pegar_pausa2()
saida = f.pegar_saida()
datas = f.pegar_datas()

f.calcular_horario()

#horarios = {}
#
#for n,l in enumerate(datas):
#    horarios[l] = chegada