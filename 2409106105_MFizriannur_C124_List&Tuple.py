nama = ["shandy",106,True,
        ["yuyun",145, 3.96]
        [123,"alvito",False, 3.66],"Rehan"
        ]
print(nama[4][2])  
print(nama[4][1])
print(nama[4][3])
print(nama[5][0])
print(nama[4])

matkul = ["APD",
          "APL",
          "WEB",
          "JARKOM",
          "jarkom",
          "BASDAT",
          "STRUKDAT",
          "PTI",
          "KALKULUS",
          "PROBAS"
          ]
print(matkul[6])

print(matkul)
print(matkul[-1])
print(matkul[-3])

makanan = ["Bakso", "Sate","Soto","Nasi Goreng","Mie Ayam","Cumi Goreng"]
print("Sebelum: ")
print(makanan[2:5])
#   makanan.append("Nasi Goreng")
print("Sesudah: ")
del makanan[5]
data = makanan.pop(5)
print(makanan)
#   print(makanan)
makanan.insert(1,"Nasi Goreng")
print(makanan)

#   makanan.insert(2,"Nasi Goreng")
#   makanan[1] = "Nasi Goreng"
#   makanan[0] = ["Ayam bakar warung bu tin","Sate Madura"]
#   print(makanan)


#   minuman 6. 3(dihapus) 6(air putih) 1(jus tomat)

minuman = ["susu","jus mangga","jus sirsak",
           "es teler","es teh","es buah"]
print("Sebelum")
print(minuman)

del minuman[2]
print("sesudah")
print(minuman)
minuman[4] ="air putih"
print(minuman)

minuman.insert(0,"jus tomat")
print(minuman)

makanan = ["Bakso","Soto","Sate","Ikan","Bebek"]

for i in makanan :
    print(i)
    print(i, end="&")  
    print(i, end="")
    print(i, end=", ")

    makanan = [["Bakso","Soto","Sate","Ikan","Bebek"],["Teh","kopi","air"]]

for i in makanan :
    
    for j in i :
        print(j, end=" ")

        makanan = [["Bakso","Soto","Sate","Ikan","Bebek"],["Teh","kopi","air"]]

for i in makanan :
    if isinstance(i, list):
        for j in i :
            print(j, end=" ")
        else:
            print(i)

makanan = [["Bakso","Soto","Sate","Ikan","Bebek"],["Teh","kopi","air"]]

# for i in makanan :
#     if isinstance(i, list):
#         for j in i :
#             print(j)
#         else:
#             print(i)

