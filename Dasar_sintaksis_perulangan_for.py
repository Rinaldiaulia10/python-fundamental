"""
Program berulang membaca buku dengan for
"""
Jumlah_buku = 10
print('Ibu berkata, "Baca semua bukumu"')

Jumlah_buku_yang_sudah_dibaca = 0
print(f'Jumlah buku yang sudah dibaca {Jumlah_buku_yang_sudah_dibaca}')

print("Dengan for")
for jumlah_buku_yang_dibaca in range(1, Jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {Jumlah_buku_yang_sudah_dibaca}")