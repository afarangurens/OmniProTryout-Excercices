from datetime import datetime, timedelta


# La función recibe dos fechas en el formato "dd/mm/yyyy hh:mm:ss +/-offset"
def count_weekdays(date1, date2):
    # Se convierten las fechas que vienen como string a objectos datetime para poder operar sobre estas
    date1 = datetime.strptime(date1, "%d/%m/%Y %H:%M:%S %z")
    date2 = datetime.strptime(date2, "%d/%m/%Y %H:%M:%S %z")

    # Como las fechas se pueden ingresar en cualquier orden, es necesario saber cual fecha es "mayor" esto para
    # poder realizar los calculos, entonces date2 tendrá siempre la mayor fecha
    if date1 > date2:
        date1, date2 = date2, date1

    # Se inicializan en un diccionario los días de la semana mapeando los números del 0 - 6 con el día de la semana
    # al que corresponde
    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    # Se inicializa el diccionario donde se va a relizar el conteo de los días entre las dos fechas
    count = {weekday: 0 for weekday in weekdays.values()}
    current_date = date1

    # En este while se realiza el conteo, va a correr hasta que se haya iterado hasta la fecha dos.
    while current_date <= date2:
        # Incrementa el conteo en 1 de los días en el diccionario count por cada día de la semana, el nombre del día
        # se obtiene con la función weekday() así se sabe qué nombre de día es el día actual en la iteración.
        count[weekdays[current_date.weekday()]] += 1
        # A la date1 se le aumenta en un día para seguir iterando sobre todos los días entre las dos fechas
        current_date += timedelta(days=1)
    # Retorna un diccionario con el conteo de los días.
    return count


# Esta función recibe dos fechas en las cuales se va a contabilizar el número de horas laborales entre las dos fechas
# Asumiendo que se trabajan 8 horas al día
def count_labour_hours(date1, date2):
    # Se obtiene el diccionario que cuenta los días entre las dos fechas categorizados por nombre del día
    weekdays_count = count_weekdays(date1, date2)

    # Se suma los días entre las dos fechas utilizando una lista de comprensión. Solamente se tienen en cuenta los días
    # laborales, es decir todos menos sábado y domingo.
    n_of_labour_days = sum(value for day, value in weekdays_count.items() if day != "Sunday" and day != "Saturday")

    # Por ultimo se retorna el valor de los días laborales multiplicado por las 8 horas laborales por día, que da
    # como resultado el número de horas laborales entre las dos fechas.
    return n_of_labour_days * 8


# En esta función entran las dos fechas las cuales van a ser restadas
def substraction_of_dates(date1, date2):
    # Se crean los objetos datetime dado el formato de entrada de las fechas
    date1 = datetime.strptime(date1, "%d/%m/%Y %H:%M:%S %z")
    date2 = datetime.strptime(date2, "%d/%m/%Y %H:%M:%S %z")

    # Si la fecha 1 es mayor a la fecha dos, se cambian para poder realizar la resta y que el resultado sea positivo
    if date1 > date2:
        date1, date2 = date2, date1

    # Se retorna la resta entre las dos fechas.
    return date2 - date1


# Entrada ejemplo de dos fechas en la misma zona horaria.
date_a = "01/01/2022 00:00:00 +0000"
date_b = "31/12/2022 23:59:59 +0000"

print(count_weekdays(date_a, date_b))
print(count_labour_hours(date_a, date_b))
print(substraction_of_dates(date_a, date_b))

# Emtrada ejemplo de dos fechas en diferentes zonas horarias
date_e = "15/05/2022 00:00:00 -0800"
date_f = "30/06/2022 23:59:59 +0500"

print(count_weekdays(date_e, date_f))
print(count_labour_hours(date_e, date_f))
print(substraction_of_dates(date_e, date_f))