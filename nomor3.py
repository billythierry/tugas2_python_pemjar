# Menghitung banyaknya bilangan genap dan ganjil

import numpy as np

def hitungGanjilGenap(arr):
    odd = [i for i in arr if i % 2 != 0]
    even = [i for i in arr if i % 2 == 0]
    
    oddLength = len(odd)
    evenLength = len(even)
    
    print(f"Jumlah Bilangan Ganjil: {oddLength} yaitu {odd}")
    print(f"Jumlah Bilangan Genap : {evenLength} yaitu {even}")
    

if __name__ == "__main__":
    n = int(input("Masukkan bilangan : "))

    val = [i + 1 for i in range(n)]

    arr = np.array(val)
    print(arr)
    hitungGanjilGenap(arr)