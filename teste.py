from operator import contains


horas = input("> ")

def __hours__(time: str):
    global hour
    _time = []
    if len(time) == 4:
        _time = [4]
        _time[0] = '0'
    
    for l in time:
        _time.append(l)
        
    #for n in range(len(_time)):
     #   hour = str(_time[0] + _time[1])

    hour = _time[:-2]
    hour = int(str(hour[0] + hour[1]))
   
    if time.__contains__("pm") or time.__contains__("am"):
        minute = _time[3:-2]  #  "palavra" [3:-2] [A:B] -> A=a B=v | Com o sufixo '-' a contagem é da direita para a esquerda.
        print("-1")
    else:
        minute = _time[-2:]
        print("-2")
    
    minute = str(minute[0] + minute[1])
    print(hour)

    if hour >= 0 and hour <= 4:
        print(f"Boa madrugada! Agora são {hour}:{minute} da madrugada.")
    elif hour >= 5 and hour <= 11:
        print(f"Bom dia! Agora são {hour}:{minute} manhã.")
    elif hour >= 12 and hour <= 18:
        print(f"Boa tarde! Agora são {hour}:{minute} da tarde.")
    elif hour >= 19 and hour <= 23:
        print(f"Boa noite! Agora são {hour}:{minute} da noite.")

__hours__(horas)
