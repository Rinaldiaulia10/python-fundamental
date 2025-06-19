"""
Program berulang membaca buku dengan while
"""

Book_Count = 10
print('Ibu berkata, "Baca semua bukumu"')
Read_Count = 0

Understood_Count = 0
print(f'Jumlah buku yang sudah dibaca dan dipahami {Understood_Count}')

while Read_Count < Book_Count * 2:
    Read_Count = Read_Count + 1
    if Understood_Count == 9:
        print(f" Buku ke {Understood_Count + 1} belum paham")
    else:
        Understood_Count = Understood_Count + 1
        print(f"Buku ke {Understood_Count} sudah dibaca dan dipahami")

print(f"Jumlah buku yang dibaca dan dipahami {Understood_Count}")
if Understood_Count == Book_Count:
    print('"Bu, semua buku sudah dibaca dan dipahami')
else:
    print(f'"Bu, tidak semua buku bisa dipahami.'
          f' Budi hanya bisa memahami {Understood_Count} buku')