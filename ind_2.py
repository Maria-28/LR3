#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# В списке, состоящем из вещественных элементов, вычислить:
# 1) количество положительных элементов списка;
# 2) сумму элементов списка, расположенных после последнего элемента, равного нулю.
# Преобразовать список таким образом, чтобы сначала располагались все элементы, целая часть
# которых не превышает 1, а потом - все остальные.

import math
from random import random

if __name__ == '__main__':
    # количество положительных элементов списка
    m = 0
    u = tuple(map(float, input('Введите вещественные числа -->').split()))
    for i in u:
        if i > 0:
            m += 1
    print(m)
    #сумму элементов списка, расположенных после последнего элемента, равного нулю.
    s = 0
    neg = -1
    for i, n in enumerate(u):
        if n == 0:
            neg = i
            break

    for n in u[neg + 1:]:
        s += abs(n)

    print(s)

    # Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].
    u = tuple(sorted(u))
    print(u)

