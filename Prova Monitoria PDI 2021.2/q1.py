from time import sleep
import os

def main():
    # Obtem o horário do usuário
    s = obterHorario()
    # Começa a cronometrar
    cronometrar(s)

def obterHorario():
    text = input('Diga um horário para a contagem regresiva (hh:mm:ss): ')
    return textSeg(text)

# Transforma texto em segundos
def textSeg(text):
    lista = text.split(':')
    if len(lista) == 3:
        h = int(lista[-3])*60*60 + int(lista[-2])*60 + int(lista[-1])
    elif len(lista) == 2:
        h = int(lista[-2])*60 + int(lista[-1])
    else:
        h = int(lista[-1])

    return h

# Transforma segundo em Texto
def segText(s):
    h = m = 0
    if s >= 3600:
        h = s // 3600
        s -= h *3600
    if s >= 60:
        m = s // 60
        s -= m * 60

    return f'{h:02}:{m:02}:{s:02}'

# Cronometra diminuindo 1 segundo e usando sleep por 1 segundo
def cronometrar(s):
    while s != 0:
        print(segText(s))
        s -=1
        sleep(1)
        os.system('clear')

main()