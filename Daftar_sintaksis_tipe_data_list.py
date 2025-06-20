daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('Tampilkan variable daftar buku')
print(daftar_buku)

print('\nProses semua dengan for in')
for buku in daftar_buku:
    print(buku)

print('\nTampilkan isi daftar_buku pada indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[2])

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai awal daftar buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
print('\nTambahkan 1 buku baru')
daftar_buku.append('Dunia Matematika Kelas 5')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nGanti elemen pertama')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku[0] = 'Eight Habits'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print('\nAmbil elemen kedua')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop -4')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
del daftar_buku[0:3]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del dengan list comprehension')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku[i])
    
print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4DX']
daftar_buku_baru = daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku[i])