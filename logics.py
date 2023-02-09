from datetime import datetime

def possibility(): # если последний вызов бота был вчера, но меняет дату на сегодня и возвращает True, либо возвращает False
    last = 0
    today = datetime.now().day
    with open('files\last_time.csv', 'r', encoding='utf-8') as file:
        last = int(file.readline())
    if today == 1 or (today - last) >= 1:
        with open('files\last_time.csv', 'w', encoding='utf-8') as f:
            f.write(str(today))
        return True
    else:
        return False

