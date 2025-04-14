#program seleksi kriteria nilai

def Rating(nilai):
    if nilai >= 88:
        print('A')
    elif 77 <= nilai & nilai < 88:
        print('B')
    elif 60 <= nilai & nilai < 77:
        print('C')
    elif 45 <= nilai & nilai < 60:
        print('D')
    elif 0 <= nilai & nilai < 45:
        print('E')
    else:
        print('Nilai invalid')

if __name__ == "__main__":
    input_user = input('Masukkan nilai Anda : ')
    angka = int(input_user)
    
    Rating(angka)
    

