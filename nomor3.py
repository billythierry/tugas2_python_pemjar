# Menghitung banyaknya bilangan genap dan ganjil

import numpy as np

n = int(input("Masukkan bilangan : "))

val = [i + 1 for i in range(n)]

arr = np.array(val)
print(arr)

def hitungGanjil(arr):
    for i in arr:
        if i % 2 == 0:
            odd = np.array(arr)