hour_format = input("Escolha o formato de hora (24 ou 12): ")

if hour_format == "12": print("Inclua 'PM' para 'Pós Manhã' ou 'AM' para 'Anti Manhã'.")

hour = input("Insira a hora: ")
minute = input("insira os minutos: ")


def __check_hour__(hour: str, minute: str, hour_format: str):
    if hour_format == "12":
        print(__if_hour_format_are_12__(hour))
    elif hour_format == "24":
        print(__if_hour_format_are_24__(hour))


def __if_hour_format_are_24__(hour: str):
    _pm_verify = bool(__pm__(hour))
    _am_verify = bool(__am__(hour))
    if _pm_verify:
        return __pm__(hour)
    elif _am_verify:
        return __am__(hour)


def __if_hour_format_are_12__(hour: str):
    if hour.__contains__("AM"):
        return __am__(hour)
    if hour.__contains__("PM"):
        return __pm__(hour)


def __pm__(hour: str):
    _hour = hour.replace("PM", "")
    _hour = int(_hour)
    _PM_1_HOURS = [12, 1, 2, 3, 4, 5, 6, 13, 14, 15, 16, 17, 18]  # Tarde
    _PM_2_HOURS = [5, 6, 7, 8, 9, 10, 11]  # Manhã
    for h in _PM_1_HOURS:
        if _hour == h:
            return "Boa tarde!"

    for h in _PM_2_HOURS:
        if _hour == h:
            return "Bom dia!"


def __am__(hour: str):
    _hour = hour.replace("AM", "")
    _hour = int(_hour)
    _AM_1_HOURS = [7, 8, 9, 10, 11, 19, 20, 21, 22, 23]  # Noite
    _AM_2_HOURS = [0, 1, 2, 3, 4]  # Madrugada
    for h in _AM_1_HOURS:
        if _hour == h:
            return "Boa noite!"

    for h in _AM_2_HOURS:
        if _hour == h:
            return "Boa madrugada!"


__check_hour__(hour, minute, hour_format)
