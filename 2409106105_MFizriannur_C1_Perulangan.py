# for j in range (2,12,2):
#       print("Hallo")
# print("Hai")

# Ulang = 0
# for i in range (Ulang):
#   print("Hallo")\

# simpan = [12, "udin petot", 14.5, True, 'A',"102"]
# for i in simpan:
#    print(i)
# for i in simpan:
#   print(i)

# print("Menu Makanan Informatika 24: ")
# print("----------------------------")
# simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in range(len(simpan)):
#   print(f"{i}. {menu} ")

print("Menu Makanan Informatika 24: ")
print("----------------------------")
simpan = ["Nasi Goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
for i, menu in enumerate(simpan,start=100):
   print(f"{i+1}. {simpan[i]}")

makanan = ["mie","sop","bakso"]
minuman = ["Es teh", "air putih", "es jeruk"]

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
print(f"Total perulangan: {hitung}")

hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Lanjut? ")
    if ulang == "y" or ulang =="Y":
        print("Oke Kita Lanjut")
        continue

hitung = 0
while True:
    hitung += 1
    ulang = input("Masih Ingin Mengulang? ")
    if ulang == "tidak" or ulang =="Tidak":
        break
print(f"Total Perulangan: {hitung}")

print("Daftar bilangan ganjil dari 1-10")
for i in range(10):
    if i % 2 == 0:
     continue
print(i)
