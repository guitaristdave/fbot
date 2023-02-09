def plus_gay(username: str):
    file = open('files\stat.csv', 'r', encoding='utf-8')
    result = ''
    for line in file.readlines():
        item = line.strip('\n').split(';')
        if item[0] == username:
            result += f'{item[0]};{int(item[1]) + 1}\n'
        else:
            result += line
    file.close()
    with open('files\stat.csv', 'w', encoding='utf-8') as f:
        f.write(result)
        
def show_gays():
    result = ''
    with open('files\stat.csv', 'r', encoding='utf-8') as file:
        for line in file:
            result += line
    return result[0:-1]

print(show_gays())