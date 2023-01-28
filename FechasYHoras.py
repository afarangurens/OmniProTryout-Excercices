import datetime
import calendar


def weekday_count(start, end):
    start_date = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%Y')
    week = {}
    for i in range((end_date - start_date).days):
        day = calendar.day_name[(start_date + datetime.timedelta(days=i + 1)).weekday()]
        if day != "Sunday" and day != "Saturday":
            week[day] = week[day] + 1 if day in week else 1
    return week


def substraction_of_dates(start, end):
    start_date = datetime.datetime.strptime(start, '%d/%m/%Y')
    end_date = datetime.datetime.strptime(end, '%d/%m/%Y')

    return end_date - start_date


week = weekday_count("01/01/2017", "31/01/2017")
print("Número de días por día de la semana:")
print(week)
print("\nNúmero de horas laborales entre las dos fechas: " + str(sum(week.values()) * 8))
print("Resta de las dos fechas: ", substraction_of_dates("01/01/2017", "31/01/2017"))