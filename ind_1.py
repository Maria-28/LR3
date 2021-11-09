#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ввести список А из 10 элементов, найти сумму элементов кратных 2, их количество и
# вывести результаты на экран.

if __name__ == '__main__':
    u = tuple(map(int, input('Введите 10 чисел -->').split(maxsplit=10)))
    s = 0
    for i in u:
        if i % 2 == 0:
            s += i
            print('Кратные 2 =', i)
    print('Сумма кратных 2 =', s)
