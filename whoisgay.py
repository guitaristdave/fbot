import dicts
from random import randint

def gay(): # возвращает рандомного юзера чата
    x = len(dicts.people) - 1
    return dicts.people[randint(0, x)]