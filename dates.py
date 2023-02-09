from datetime import datetime

# Даты нужны для того, чтобы делать запрос по вчерашним матчам

def dateFrom(): #возвращает вчерашнюю дату в формате гггг-мм-дд
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day - 1)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return f'{year}-{month}-{day}'

def dateTo(): #возвращает сегодняшнюю дату в формате гггг-мм-дд
    year = str(datetime.now().year)
    month = str(datetime.now().month)
    day = str(datetime.now().day)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    return f'{year}-{month}-{day}'