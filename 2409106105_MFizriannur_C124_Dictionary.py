daftar_buku = {
# key : value    
    "Buku1" : "Harry Potter",
    "Buku2" : "Twillight",
    "Buku3" : "Twillight"
} 

print(daftar_buku["Buku1"])
print(daftar_buku["Buku2"])
print(daftar_buku["Buku3"])
# print(daftar_buku)

    
Biodata = {
    "Nama": "Muhammad Fizriannur",
    "NIM": 2409106105,
    "KRS": ["Program Web", "Struktur Data", "Basis Data"],
    "Mahasiswa_Aktif": True,
    "Social Media": {
        "Instagram": "Fizri_907",
        "Discord": "Fizri305",
        "Email": "Fizri907@gmail.com"
    }
}
print(Biodata["Social Media"]["Email"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure")
# Valorant = "FPS"
# print(games["Pokemon"])

# Games = {
#     "Game1" : "PUBG Mobile"
#     "Game2" : "Mobile Legends"
#     "Game3" : "COC"
#   }
# games = dict(Sekiro = "Action", Pokemon = "Adventure")
# Valorant = {"nama" : "dimas"}
# print(games['Valorant']['nama'])

# Games = {
#     "Game1" : "PUBG Mobile"
#     "Game2" : "Mobile Legends"
#     "Game3" : "COC"
#   }
# games = dict(Sekiro = "Action", Pokemon = "Adventure")
# Valorant = {"nama" :{123 : "informatika"}}
# print(games['Valorant']['nama'][123])

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#tanpa menggunakan items
for i in Nilai:
    print(i)
print("")

#menggunakan items
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

    Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
print(Film)

Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller",
             "Rush Hour" : "Comedy",
             "Oblivion" : "Science Fiction"})

# setelah ditambah
# penggunaan del
# del Film['Avenger Endgame']
print(Film)

simpan = Film.pop('Hours')
# Film.clear()
print(Film)
print(simpan)
Film["Hours"] = simpan
print(Film)

#cara mengetahui jumlah projek/
print("Jumlah Film = ", len(Film)) #contah 1
print( len(Film)) #contoh 2
movies = Film.copy()
print(movies)
# print("Jumlah film = " len(Film))

key = "apel", "jeruk", "mangga", "Semangka"
value = 1
buah = dict.fromkeys(key, value)
print(buah)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys/nama saja
for i in Nilai.keys():
    print(i)

#menggunakan value/nilai saja
for i in Nilai.values():
    print(i)

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai Kimia : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

Musik = {
"The Chainsmoker" : ["All we Know", "TheParis"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
    print(f"Musik milik {i} adalah : ")
    for song in j:
        print(song)
print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18}
}
for key, value in mahasiswa.items():
    print("ID Mahasiswa : ", key)
    for nama_1, nama_2 in value.items():
        print (nama_1, " : ", nama_2)
print("")