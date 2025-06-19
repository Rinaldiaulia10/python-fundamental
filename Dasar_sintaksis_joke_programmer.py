"""
Semua sintaksis dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan: Langkah melompat  jika kondisi terpenuhi
3. Perulangan: Mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
#Sekuensial
print('Ibu berkata:"Pergilah ke toko"')
print('Budi menjawab,"Baik apa yang harus dilakukan ditoko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print('Maka Budi berangkat ke toko')
print('Dan mulai berbelanja')

#Percabangan
jumlah_botol_susu = 173
jumlah_butir_telur = 1587
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_butir_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya dan ternyata uangnya cukup")
    if jumlah_butir_telur == 0:
        print('Budi membeli 1 botol susu')
    else:
        print('Budi membeli 6 botol susu')

else:
    print("Budi tidak jadi membeli 1 botol susu")

print('Budi pulang kerumah')
print('Dan menyerahkan hasil belanjaannya ke ibu')


