# try:
#     angka = int(input("Masukan angka: "))
# except ValueError :
#     print("Input yang anda masukkan bukan angka")


# # contoh try
# try:
#     angka = int(input("Masukan angka: "))

#     if angka % 2 == 0:
#         print("genap")
#     elif angka % 2 != 0:
#         print("ganjil")
#     else:
#         print("input tidak valid") # bisa juga printnya masukan pilihan" lain

# except ValueError :
#     print("Input yang anda masukkan bukan angka")


# # program yang menjalankan mau dia error atau tidak dia bakal terus jalan
# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")
# finally:
#     print("Program selesai")


# # blok try-except = mengecek jikalau except valueerrornya jalan elsenya tidak masuk,jikavelueerrornya tidak jalan elsenya jalan
# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")


# # membuat kustom error dengan raise
# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5karakter")
# except ValueError as e:
#     print(e)    

# # contoh lain dari kustom error dengan raise
# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError
# except ValueError as e:
#     print(e)


# # contoh membikin code modul 10
# def penjumlahan():
#     try:
#         angka1 = int(input("Masukkan angka pertama: "))
#         angka2 = int(input("Masukkan angka kedua: "))
#         print(f"Hasil penjumlahan: {angka1 + angka2}")
#     except ValueError:
#         print("Input tidak valid, mohon masukkan angka yang benar.")
#         penjumlahan()

# def menu():
#     print("1. Penjumlahan")
#     print("2. Exit")
#     try:
#         pilihan = int(input("Pilih menu: "))
#         if pilihan == 1:
#             penjumlahan()
#         elif pilihan == 2:
#             print("Program berhenti.")
#             exit()
#         else:
#             print("Pilihan tidak valid, coba lagi.")
#             menu()
#     except ValueError:
#         print("Input tidak valid, mohon masukkan angka (1 atau 2).")
#         menu()
# menu()


