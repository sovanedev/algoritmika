#Шевченко Михаил
from math import *
from time import *
from test import *
from questions import *
name = input('Ваше имя')
tim1 = time()
right = 0

count_1, count_2 = rate(right, questions, answer)

tim2 = time()
print(name)
print('Время прохождения теста:', round(tim2-tim1), 'сек.')
print('Набрано баллов:', count_1)
print(count_2)
