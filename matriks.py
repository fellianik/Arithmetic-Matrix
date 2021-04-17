def penjumlahan():
    print("\nPenjumlahan Matriks A + B =")
    plus = []
    total = 0
    for i in range(ordo):
        row = []
        for j in range(ordo):
            total = a[i][j] + b[i][j]
            row.append(total)
        plus.append(row)

    for i in range(ordo):
        print("|\t", end='')
        for j in range(ordo):
            print(plus[i][j], end='\t')
        print("|")

def pengurangan_ab():
    print("\nPengurangan Matriks A - B =")
    minus = []
    total = 0
    for i in range(ordo):
        row = []
        for j in range(ordo):
            total = a[i][j] - b[i][j]
            row.append(total)
        minus.append(row)
    
    for i in range(ordo):
        print("|\t", end='')
        for j in range(ordo):
            print(minus[i][j], end='\t')
        print("|")

def pengurangan_ba():
    print("\nPengurangan Matriks B - A =")
    minus = []
    total = 0
    for i in range(ordo):
        row = []
        for j in range(ordo):
            total = b[i][j] - a[i][j]
            row.append(total)
        minus.append(row)
    
    for i in range(ordo):
        print("|\t", end='')
        for j in range(ordo):
            print(minus[i][j], end='\t')
        print("|")

def perkalian_ab():
    print("\nPerkalian Matriks A x B:")
    multi = []
    for i in range(ordo):
        row = []
        for j in range(ordo):
            total = 0
            for k in range(ordo):
                total += a[i][k] * b[k][j]
            row.append(total)
        multi.append(row)

    for i in range(ordo):
        print("|\t", end='')
        for j in range(ordo):
            print(multi[i][j], end='\t')
        print("|")

def perkalian_ba():
    print("\nPerkalian Matriks B x A:")
    multi = []
    for i in range(ordo):
        row = []
        for j in range(ordo):
            total = 0
            for k in range(ordo):
                total += b[i][k] * a[k][j]
            row.append(total)
        multi.append(row)

    for i in range(ordo):
        print("|\t", end='')
        for j in range(ordo):
            print(multi[i][j], end='\t')
        print("|")

def getcofactor_a(a, i, j):
    return [row[:j] + row[j+1:] for row in (a[:i] + a[i+1:])]

def determinan_a(a):
    det = 0
    if len(a) == 1:
        det = a[i][j]
    elif len(a) == 2:
        det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        det = 0
        for i in range(0, len(a)):
            sign = (-1) ** i
            sub_det = determinan_a(getcofactor_a(a, 0, i))
            det += sign * a[0][i] * sub_det
    return det

def getcofactor_b(b, i, j):
    return [row[: j] + row[j+1:] for row in (b[: i]+b[i+1:])]

def determinan_b(b):
    det = 0
    if len(b) == 1:
        det = b[i][j]
    elif len(b) == 2:
        det = b[0][0] * b[1][1] - b[0][1] * b[1][0]
    else:
        det = 0
        for i in range(len(b)):
            sign = (-1) ** i
            sub_det = determinan_a(getcofactor_b(b, 0, i))
            det += sign * b[0][i] * sub_det
    return det


def perulangan():
    lanjut = input("\nIngin melanjutkan[Y/T]? = ")
    for i in lanjut:
        if lanjut == 'Y':
            continue
            print()
        else:
            print("\nTerima kasih telah menggunakan program ini!\U0001F600\n")
            exit()

# MAIN PROGRAM
print("==========PROGRAM PERHITUNGAN MATRIKS==========")

while True:
        try:
            ordo = int(input("Masukkan ordo: "))
            if ordo < 1:
                raise ValueError
            break
        except ValueError:
            print("Input anda bukan angka lebih dari 0")

print("Masukkan", ordo*ordo, "Elemen dalam Matriks\n")

print("Matriks A =")
a = []   # a = matriks A
for i in range(ordo):
    a.append([])
    for j in range(ordo):
        while True:
            try:
                a[i].append(int(input("Masukkan elemen [%d][%d]: " %(i+1, j+1))))
                break
            except ValueError:
                print("Input anda bukan angka")

print("\nMatrik A =")
for baris in a:
    print("|\t", end='')
    for kolom in baris:
        print("%d\t" %kolom, end='')
    print("|")

print()

print("Matriks B =")
b = []   # b = matriks B
for i in range(ordo):
    b.append([])
    for j in range(ordo):
        while True:
            try:
                b[i].append(int(input("Masukkan elemen [%d][%d]: " %(i+1, j+1))))
                break
            except ValueError:
                print("Input anda bukan angka")

print("\nMatrik B =")
for baris in b:
    print("|\t", end='')
    for kolom in baris:
        print("%d\t" %kolom, end='')
    print("|")

print()

while True:
    print("Pilihan Perhitungan Matriks:")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinan Matriks")
    print("===============================================")
    pilihan = int(input("Masukkan Pilihan:"))
    if pilihan == 1:
        penjumlahan()
        perulangan()
    elif (pilihan==2):
        print("\nPilihan pengurangan:")
        print("1. A - B")
        print("2. B - A")
        pilih = int(input("Masukkan pilihan: "))
        if pilih == 1:
            pengurangan_ab()
        elif pilih == 2:
            pengurangan_ba()
        else:
            print("Pilihan salah")
        perulangan()
    elif (pilihan==3):
        print("\nPilihan perkalian:")
        print("1. A x B")
        print("2. B x A")
        pilih = int(input("Masukkan pilihan: "))
        if pilih == 1:
            perkalian_ab()
        elif pilih == 2:
            perkalian_ba()
        else:
            print("Pilihan salah")
        perulangan()
    elif (pilihan==4):
        pilih = input("\nMatriks apa yang dihitung?[A/B] = ")
        if pilih == 'A':
            determinan_a(a)
            print("\nHasil determinan matriks A adalah =", determinan_a(a))
        elif pilih == 'B':
            determinan_b(b)
            print("\nHasil determinan matriks B adalah =", determinan_b(b))
        else:
            print("Pilihan salah")
        perulangan()
    else:
        print("Masukkan Anda Salah!")
        print("Coba lagi!")

'''
Program oleh:
Felliani Kurniawati
NPM 20081010085
Kelas F
MK: Aljabar Linier & Matriks
'''