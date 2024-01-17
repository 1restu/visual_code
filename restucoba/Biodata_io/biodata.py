print("selamat datang di program biodata")
print("=================================")

# Ambil input dari user
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

#format teks
teks = "\nBiodata: \nNama: {}\nUmur: {}\nAlamat: {}".format (nama, umur, alamat)

# buka file unruk di tulis
file_bio = open("Biodata_io/biodata.txt", "a")

# tulis teks ke file
file_bio.write(teks)

file_bio.close()