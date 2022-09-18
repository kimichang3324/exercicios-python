#  INPUT
from wsgiref import validate


def __universal_print_hour__(time: str):
    global hour
    global minute
    _time = []
    type_hour = ["", "", ""]

    if is_24:
        type_hour[:] = [""]
        if len(time) == 4:
            _time = [4]
            _time[0] = "0"
    else:
        type_hour[0] = "(PM)"
        type_hour[1] = "(AM)"
        if len(time) == 6:
            _time = [6]
            _time[0] = "0"

    for st in time:
        _time.append(st)

    if is_24:
        hour = _time[:-2]
        minute = _time[-2:]
    else:
        hour = _time[:-2]
        minute = _time[3:-2]

 
    def __time_24__(hour: int, minute: int):
        if hour >= 0 and hour <= 4:
            print(f"Boa madrugada! São {hour}:{minute} da madrugada.")
            __time_left__(hour, minute, str(type_hour[0]), "da madrugada")
        elif hour >= 5 and hour <= 11:
            print(f"Bom dia! São {hour}:{minute} da manhã.")
            __time_left__(hour, minute, str(type_hour[0]), "da manhã")
        elif hour >= 12 and hour <= 18:
            print(f"Boa tarde! São {hour}:{minute} da tarde.")
            __time_left__(hour, minute, str(type_hour[0]), "da tarde")
        elif hour >= 19 and hour <= 23:
            print(f"Boa noite! São {hour}:{minute} da noite.")
            __time_left__(hour, minute, str(type_hour[0]), "da noite")


    def __pm__(hour: str, minute: str):
        _hour = int(hour)
        _minute = int(minute)
        h_1 = [12, 1, 2, 3, 4, 5, 6]  # Tarde
        h_2 = [7, 8, 9, 10, 11]  # Noite
        
        for h in h_1:
            if _hour == h or _hour == [0]+[h]:
                print(f"Boa tarde! São {_hour}:{_minute}{type_hour[0]} da tarde.")
                __time_left__(_hour, _minute, str(type_hour[0]), "da tarde")

        for h in h_2:
            if _hour == h or _hour == [0]+[h]:
                print(f"Boa noite! São {_hour}:{_minute}{type_hour[0]} da noite.")
                __time_left__(_hour, _minute, str(type_hour[0]), "da noite")


    def __am__(hour: str, minute: str):
        _hour = int(hour)
        _minute = int(minute)
        h_1 = [5, 6, 7, 8, 9, 10, 11]  # Manhã
        h_2 = [0, 1, 2, 3, 4]  # Madrugada
        for h in h_1:
            if _hour == h or _hour == [0]+[h]:
                print(f"Bom dia! São {_hour}:{_minute}{type_hour[1]} da manhã.")
                __time_left__(_hour, _minute, str(type_hour[1]), "da manhã")

        for h in h_2:
            if _hour == h or _hour == [0]+[h]:
                print(f"Boa madrugada! São {_hour}:{_minute}{type_hour[1]} da madrugada.")
                __time_left__(_hour, _minute, str(type_hour[1]), "da madrugada")
    
    if time.__contains__("pm") and not is_24:
        return __pm__(str(hour[0] + hour[1]), str(minute[0] + minute[1]))
    elif time.__contains__("am") and not is_24:
        return __am__(str(hour[0] + hour[1]), str(minute[0] + minute[1]))
    elif is_24:
        return __time_24__(int(str(hour[0] + hour[1])), int(str(minute[0] + minute[1])))



def __time_left__(h: int, m: int, tph: str, refernce_time: str):
    word = ["", "", "", "", "", ""]
    next_hour = h + 1

    if h != 0:
        count_hour = 24 % h
    else:
        count_hour = 0

    if h == 12 and not is_24:
        next_hour = 1
    elif h == 23 and is_24:
        next_hour = 0
        count_hour = 0
        word[4] = [""]

    if next_hour > 1:
        word[4] = "horas"
        word[5] = "as "
    else:
        word[4] = "hora"
        word[5] = ""

    if count_hour == 1:
        word[0] = "Falta"
        word[1] = "hora"
    elif count_hour > 1:
        word[0] = "Faltam"
        word[1] = "horas"

    n = 60 - m    
    if n == 1:
        word[2] = "Falta"
        word[3] = "minuto"
    elif n > 1:
        word[2] = "Faltam"
        word[3] = "minutos"
        
  
    if count_hour == 1:
        print(f"{str(word[0])} {count_hour} {str(word[1])} e {60 - m} {str(word[3])} para {word[5]}{next_hour}:00{tph} {word[4]}.")
    else:
        print(f"{str(word[2])} {60 - m} {str(word[3])} para {word[5]}{next_hour}:00{tph} {word[4]}.")



check = True
is_24: bool
input_hour = input("Insira a hora: ")
if input_hour.lower().__contains__("pm") or input_hour.lower().__contains__("am"):
    is_24 = False
else:
     is_24 = True


#  OUTPUT
if is_24:
    print("\nFormato (24 horas)")
    __universal_print_hour__(input_hour)
    print("\n")
else:
    print("\nFormato (12 horas)")
    __universal_print_hour__(input_hour)
    print("\n")
