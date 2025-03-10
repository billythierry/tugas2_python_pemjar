# Program Kasir

cart = []

def inputKasir():
    namaBarang = input("Nama Barang : ")
    harga = int(input("Harga : "))
    jumlah = int(input("Jumlah : "))
    subHarga = harga * jumlah
    cart.append((namaBarang, harga, jumlah, subHarga))

if __name__ == "__main__":
    
    while True:
        inputKasir()
        konfirmasi = input("Ada barang lagi? (y/n)").lower()
        if konfirmasi == "n":
            break
        
    print("\n===== Struk Belanja =====")
    print("\nNama       Jumlah      Harga")
    total = 0
    for item in cart:
        print(f"{item[0]}       {item[2]}       Rp{item[1]}")
        total += item[3]
    
    print(f"Total yang harus dibayar: Rp{total}")