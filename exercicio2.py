hour_format = input("\nEscolha o formato de hora (24 ou 12): ")

if hour_format == "12":
    print("Inclua 'PM' para 'Pós Manhã' ou 'AM' para 'Anti Manhã'.")

input_hour = input("Insira a hora: ")


def __if_hour_format_are_12__(time: str):
    _time = time
    global my_minutes
    global my_hours
    _time_value = []
        #  Transfere os chars contidos em 'hour' para a lista '_time_value
        #  facilitando a manipulação de todos os valores.

    len_hs = len(_time)
    if len_hs == 6:
        _time_value = [6]
        _time_value[0] = "0"
        for st in _time:
            _time_value.append(st)
        len_hs = len(_time_value)
    # A condicional acima verifica se 'time' possui 6 chars. Caso sim, '_time_value' ganhará esse valor para o total
    # do índice considerei isso pois caso a hora seja 12:00PM, pro exemplo, serão 7 chars, caso seja 3:45PM serão 6
    # chars, com isso é acressido antecipadamente no índice '0' o número 0 em forma de String. E após isso é acressido
    # em sequência o restantes dos chars de '_time'. Após isso é feita uma nova contagem que será usada em condicionais
    # posteriores.

    signal = _time_value.index(":")

    if _time.__contains__("PM" or "pm"):
        if len_hs == 7:
            _hour = _time_value[:signal]
            for time in range(len(_hour)):  # Captura dos dois primeiros números referentes às horas.
                my_hours = str(_hour[0] + _hour[1])

            _minute = _time_value[3:-2]
            for minute in range(len(_minute)):  # Captura dos dois últimos números referentes aos minutos.
                my_minutes = str(_minute[0] + _minute[1])

            print(f"{__pm__(my_hours, my_minutes)}")

    if _time.__contains__("AM" or "am"):
        if len_hs == 7:
            _hour = _time_value[:signal]
            for time in range(len(_hour)):
                my_hours = str(_hour[0] + _hour[1])

            _minute = _time_value[3:-2]
            for minute in range(len(_minute)):
                my_minutes = str(_minute[0] + _minute[1])

            print(f"{__am__(my_hours, my_minutes)}")


def __if_hour_format_are_24__(hour: str):
    _pm_verify = bool(__pm__(hour, "12"))
    _am_verify = bool(__am__(hour, "12"))
    if _pm_verify:
        return __pm__(hour, "12")
    elif _am_verify:
        return __am__(hour, "12")


def __pm__(hour: str, minute: str):
    global message
    _hour = int(hour)
    _minute = int(minute)
    _PM_1_HOURS = [12, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18]  # Tarde
    _PM_2_HOURS = [5, 6, 7, 8, 9, 10, 11]  # Manhã
    for h in _PM_1_HOURS:
        if _hour == h or _hour == [0]+[h]:
            return f"Boa tarde! São {_hour}:{_minute}(PM) da tarde."
            # return f"Boa tarde! São {_hour}:{_minute}(PM) da tarde."

    for h in _PM_2_HOURS:
        if _hour == h or _hour == [0]+[h]:
            return f"Boa noite! São {_hour}:{_minute}(PM) da noite."
            # return f"Boa noite! São {_hour}:{_minute}(PM) da noite."


def __am__(hour: str, minute: str):
    global message
    _hour = int(hour)
    _minute = int(minute)
    _AM_1_HOURS = [7, 8, 9, 10, 11, 19, 20, 21, 22, 23]  # Noite
    _AM_2_HOURS = [0, 1, 2, 3, 4]  # Madrugada
    for h in _AM_1_HOURS:
        if _hour == h or _hour == [0]+[h]:
            return f"Bom dia! São {_hour}:{_minute}(AM) da manhã."
            # return "Bom dia! São {_hour}:{_minute}(AM) da manhã."

    for h in _AM_2_HOURS:
        if _hour == h or _hour == [0]+[h]:
            return f"Boa madrugada! São {_hour}:{_minute}(AM) da madrugada."
            # return "Boa madrugada! São {_hour}:{_minute}(AM) da madrugada."


__if_hour_format_are_12__(input_hour)
