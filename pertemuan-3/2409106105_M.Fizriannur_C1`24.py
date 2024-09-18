cuaca = "mendung"

if cuaca == "mendung":
    print("diam di rumah")
else:
    print("hari ini mendung")

# # Umur = int(input("Masukan umur Anda: "))
# # if Umur > 0:
# #     if Umur <= 10 :
# #         print( " Umur Anda termasuk kategori anak-anak")
# #     elif Umur <= 18:
# #         print("Umur Anda termasuk kategori remaja")
# #     elif Umur <= 35:
# #         print("Umur Anda termasuk kategori dewasa")
# #     elif Umur <= 65 :
# #         print("Umur Anda termasuk kategori paruh baya")
# #     else:
# #         print("Umur Anda termasuk kategori Tua")
# # else:
# #     print("Input Usia Hrus Bilangan Positif")

# # nim = int(input("Masukan nim: "))
# #    if nim >= 1 and nim <= 25 :
# #         print("Kelas A`1")
# #     else :
# #         print("Kalas A`2")
# # elif nim >= 51 and nim <= 100 :
# #     if nim >= 51 and nim <= 75 :
# #         print("Kelas B`1")
# #     else :
# #         print(Kelas B`2)
# # elif nim >= 101 and nim <= 121 :
# #     if nim (">= 101 and nim <= 110 :
# #         print("Kelas C`1")
# #     else :
# #         print ("Kelas C`2")
# #     else :
# #         print("Anda bukan mahasiswa informatika 24")

nim = int(input("Masukan nim: "))
hasil = "Kelas A" if nim >= 1 and nim <= 50 else "Kelas B" if nim >= 51 and nim <= 100 else "Kelas C" if nim >= 101 and nim <= 121 else "mahasiswa siluman"
print (hasil) 