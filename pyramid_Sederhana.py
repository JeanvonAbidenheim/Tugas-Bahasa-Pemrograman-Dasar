x = input("Masukkan karakter pembentuk piramida: ") # Meminta input dari pengguna untuk menentukan karakter yang akan membentuk piramida
height = int(input("Masukkan tinggi piramida: ")) # Meminta input tinggi piramida lalu mengubahnya menjadi tipe data integer

for i in range(1, height + 1): # Perulangan dari baris ke-1 sampai baris ke-height
    spaces = " " * (height - i) # Membuat spasi di sebelah kiri agar piramida berada di tengah
    symbols = x * (2 * i - 1) # Menentukan jumlah karakter pada setiap baris (selalu bilangan ganjil)
    print(spaces + symbols) # Menggabungkan spasi dan simbol lalu mencetak satu baris piramida

# Contoh output jika pengguna memasukkan karakter '*' dan tinggi 5:
#     * 
#    ***
#   *****
#  *******
# *********