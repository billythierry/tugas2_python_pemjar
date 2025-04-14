# Program Nilai Mahasiswa

import matplotlib.pyplot as plt

nilaiMahasiswa = []
nilaiHurufCounter = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

def inputNilai():
    namaMahasiswa = input("Nama Mahasiswa : ")
    tugas = int(input("Nilai Tugas : "))
    kuis = int(input("Nilai Kuis : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    akhir = (tugas + kuis + uts + uas) / 4
    huruf = rating(akhir)
    
    #Menyimpan list ke array nilaiMahasiswa
    nilaiMahasiswa.append((namaMahasiswa, tugas, kuis, uts, uas, akhir, huruf))
    
    #Update counter nilai huruf
    if huruf in nilaiHurufCounter:
        nilaiHurufCounter[huruf] += 1

def rating(nilai):
    if nilai >= 88:
        return 'A'
    elif 77 <= nilai < 88:
        return'B'
    elif 60 <= nilai < 77:
        return'C'
    elif 45 <= nilai < 60:
        return'D'
    elif 0 <= nilai < 45:
        return'E'
    else:
        return'Nilai invalid'

def tampilkanHasilNilai():
    print("------------------------------------------------------------")
    print("| No |   Nama   | Tugas | Kuis | UTS | UAS | Akhir | Huruf |")
    print("------------------------------------------------------------")
    
    for i, (nama, tugas, kuis, uts, uas, akhir, huruf) in enumerate(nilaiMahasiswa, start=1):
        print(f"| {i:<3}| {nama:<8} | {tugas:<5} | {kuis:<4} | {uts:<3} | {uas:<3} | {akhir:<5.2f} | {huruf:<5} |")

def tampilkanJumlahHuruf():
    print("\nJumlah Nilai Huruf: ")
    for huruf, jumlah in nilaiHurufCounter.items():
        print(f"Jumlah {huruf}: {jumlah}")
        

def diagramBatang():
    huruf = list(nilaiHurufCounter.keys())
    jumlah = list(nilaiHurufCounter.values())
    
    plt.bar(huruf, jumlah, color='skyblue', edgecolor='black')
    plt.title("Jumlah Mahasiswa per Nilai Huruf")
    plt.xlabel("Nilai Huruf")
    plt.ylabel("Jumlah Mahasiswa")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

#Input
jumlahMahasiswa = int(input("Berapa jumlah mahasiswa yang akan diberi nilai ? : "))
for _ in range(jumlahMahasiswa):
    inputNilai()
    

tampilkanHasilNilai()
tampilkanJumlahHuruf()
diagramBatang()