from datetime import datetime

chegada = "08:08"
pausa_inicio = "12:00"
pausa_fim = "13:50"
saida = "18:00"

formato = "%H:%M"

chegada = datetime.strptime(chegada, formato)
pausa_inicio = datetime.strptime(pausa_inicio, formato)
pausa_fim = datetime.strptime(pausa_fim, formato)
saida = datetime.strptime(saida, formato)

total = (saida - chegada) - (pausa_fim - pausa_inicio)

print(total)