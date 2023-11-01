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
# Menentukan Crust pada Jenis Pizza yang di pesan
print ("| ---  Pilih Crust  ---  |")
print ("| 1. Pan                 |")
print ("| 2. StuffedCrust Cheese |")
print ("| 3. StuffedCrust Sausage|")
print ("| 4. Cheesy Bites        |")
print ("| 5. CrownCrust          |")
#Setelah Crust di pilih maka :
rasacrust = int(input("Pilih Crust 1/2/3/4/5 "))
# Apabila Pelanggan memilih Curst 1 maka :
if rasacrust == 1:
    Hargatotal += 43637
    rasacrust = "== Pan ==" 
# Menambahkan ukuran dari Pizza
    size = input("PILIH UKURAN Personal/Reguler/Large: ")
# Jika memilih ukuran Personal maka tidak ada tambahan harga
    if size == "Personal":
        Hargatotal += 0
# Jika memilih ukuran Reguler maka tambahan harga sebesar 
    elif size == "Reguler" :
        Hargatotal += 57273
# Jika memilih ukuran Large maka tambahan harga sebesar
    elif size == "Large":
        Hargatotal += 89091
# Tampilan Jika memilih tidak memilih ukuran Pizza
    else:
        print("Tidak Ada Yang Dipilih")
# Apabila Pelanggan memilih Crust 2 maka :
elif rasacrust == 2:
    Hargatotal += 55455
    rasacrust == "== StuffedCrust Cheese =="
# Menambahkan ukuran dari Pizza
    size = input("PILIH UKURAN Personal/Reguler/Large: ")
# Jika memilih ukuran Personal maka tidak ada tambahan harga
    if size == "Personal":
        Hargatotal += 0
# Jika memilih ukuran Reguler maka tambahan harga sebesar 
    elif size == "Reguler":
        Hargatotal += 65455
# Jika memilih ukuran Large maka tambahan harga sebesar
    elif size == "Large":
        Hargatotal += 104545
elif rasacrust == 3:
    Hargatotal += 52728
    rasacrust = "== StuffedCrust Sausage =="
    size = input("PILIH UKURAN Personal/Reguler/Large: ")
# Jika memilih ukuran Personal maka tidak ada tambahan harga
    if size == "Personal":
        Hargatotal += 0
# Jika memilih ukuran Reguler maka tambahan harga sebesar 
    elif size == "Reguler":
        Hargatotal += 64545
# Jika memilih ukuran Large maka tambahan harga sebesar
    elif size == "Large":
        Hargatotal += 102727
# Tampilan Jika memilih tidak memilih ukuran Pizza
    else:
        print("Tidak Ada Yang Dipilih")
