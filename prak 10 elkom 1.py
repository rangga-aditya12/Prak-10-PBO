from bangun_datar import Persegi, Persegi_panjang, Lingkaran, Segitiga, Jajar_genjang

print("===============================\nNama : Rangga Aditya Pradana\nNIM : 064002300026\n===============================")
persegi = Persegi(5)
print("Luas Persegi adalah :",persegi.menghitung())

persegi_panjang = Persegi_panjang(4,5)
print("Luas Persegi Panjang adalah :",persegi_panjang.menghitung())

lingkaran = Lingkaran(7)
print("Luas Lingkaran adalah :",lingkaran.menghitung())

segitiga = Segitiga(10,14)
print("Luas Segitiga adalah :",segitiga.menghitung())

jajar_genjang = Jajar_genjang(20, 25)
print("Luas Jajar Genjang adalah :",jajar_genjang.menghitung())