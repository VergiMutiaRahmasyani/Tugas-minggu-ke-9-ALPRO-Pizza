"""
    Kelas    : 2023E
    Prodi    : D4 Manajemen Informatika
    Kelompok : 5

    Nama Anggota :
    1. Achmad Syamsudin       - 23091397164
    2. Ahmad Aryobimo         - 23091397151
    3. Vergi Mutia Rahmasyani - 23091397171
"""
#Pelanggan masuk memilih list menu topping pizza
print ("|SELAMAT DATANG DI PIZZA HUT KELOMPOK 5|")
print ("|   SILAHKAN PILIH TOPPING PIZZA       |")
print ("|   1. Frankfurter                     |")
print ("|   2. Meat Monsta                     |")
print ("|   3. Super Supreme                   |")
print ("|   4. Super Supreme Chicken           |")
#!!! HARGA PIZZA DALAM MENU INI DIBUAT SESUAI PIZZA HUT LOKASI WIYUNG !!!
#Setelah Topping Pizza ditentukan maka :
Hargatotal = 0
Topping = int(input("PILIH TOPPING PIZZA 1/2/3/4:"))
if Topping == 1:
#Tampilan jika pelanggan memilih Topping 1 
    Topping = "== Frankfurter =="
    print("== Frankfurter ==")
elif Topping == 2:
#Tampilan jika pelanggan memilih Topping 2
    Topping = "== Meat Monsta =="
    print("== Meat Monsta ==")
elif Topping == 3:
#Tampilan jika pelanggan memilih Topping 3
    Topping = "== Super Supreme =="
    print("== Super Supreme ==")
elif Topping == 4:
#Tampilan jika pelanggan memilih Topping 4
    Topping = "== Super Supreme Chicken =="
    print("== Super Supreme Chicken ==")
else:
#Tampilan jika pelanggan tidak memilih Topping
    print("tidak ada yang dipilih")
