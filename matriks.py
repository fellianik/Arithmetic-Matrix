'''
FUNCTION UNTUK PILIHAN ARITMATIKA
'''
# ==========================================================
def penjumlahan():
    print("\nPenjumlahan Matriks A + B:")
    plus = []
    jumlah = 0
    for i in range(0, s):
        plus_=[]
        for j in range(0, s):
            jumlah = int(a[i][j]) + int(b[i][j])
            plus_.append(jumlah)
        plus.append(plus_)

    for i in range(0, s):
        print("|\t", end='')
        for j in range(s):
            print(plus[i][j], end='\t')
        print("|")

# ==============================================================
def pengurangan():
    print("\nPengurangan Matriks A - B:")
    minus = []
    jumlah = 0
    for i in range(0, s):
        row=[]
        for j in range(0, s):
            jumlah = int(a[i][j]) - int(b[i][j])
            row.append(jumlah)
        minus.append(row)

    for i in range(0, s):
        print("|\t", end='')
        for j in range(s):
            print(minus[i][j], end='\t')
        print("|")

# ==========================================================
def perkalian():
    print("\nPerkalian Matriks A x B:")
    multi = []
    for i in range(0,s):
        row = []
        for j in range(0,s):
            total = 0
            for k in range(0,s):
                total += int(a[i][k])*int(b[k][j])
            row.append(total)
        multi.append(row)

    for i in range(s):
        print("|\t", end='')
        for j in range(s):
            print(multi[i][j], end='\t')
        print("|")

# =======================================================
def perulangan():
    lanjut = input("\nIngin melanjutkan[Y/T]?")
    for i in lanjut:
        if lanjut == 'Y':
            continue
        else:
            print("\nTerima kasih telah menggunakan program ini!\U0001F600\n")
            exit()


# MAIN PROGRAM

print("==========PROGRAM PERHITUNGAN MATRIKS==========\n")

'''
Deklarasi variabel
s =  ordo
a = matriks 1
b = matriks 2
'''

s = int(input("Masukkan Ordo: "))
a = [x[:] for x in [[0] * s] * s]
b = [x[:] for x in [[0] * s] * s]

print("\nMasukkan", s*s, "Elemen dalam Matriks\n")

# INPUTAN ELEMEN

print("================== Matriks A ==================")
for i in range(0, s):
    for j in range(0, s):
        print("Elemen ke", [i+1], [j+1], ":")
        a[i][j] = input()

print("\nMatrik A")
for i in range(0, s):
    print("|\t", end='')
    for j in range(0, s):
        print(a[i][j], end='\t')
    print("|")

print()

print("================== Matriks B ==================")
for i in range(0, s):
    for j in range(0, s):
        print("Elemen ke", [i+1], [j+1], ":")
        b[i][j] = input()

print("\nMatriks B")
for i in range(0, s):
    print("|\t", end='')
    for j in range(s):
        print(b[i][j], end='\t')
    print("|")

# PERULANGAN MENU PILIHAN ARITMATIKA

lanjut='Y'
while lanjut == 'Y':
    print("\n===============================================")
    print("Pilihan Perhitungan Matriks:")
    print("1. Penjumlahan Matriks")
    print("2. Pengurangan Matriks")
    print("3. Perkalian Matriks")
    print("4. Determinan Matriks")

    print("===============================================")

    pilihan = int(input("Masukkan Pilihan:"))
    print("===============================================")
    if (pilihan==1):
        penjumlahan()
        perulangan()
    elif (pilihan==2):
        pengurangan()
        perulangan()
    elif (pilihan==3):
        perkalian()
        lanjut = input("Ingin melanjutkan[Y/T]?")
        perulangan()
    elif (pilihan==4):
        determinan()
        lanjut = input("Ingin melanjutkan[Y/T]?")
        perulangan()
    else:
        print("Masukkan Anda Salah!")
        print("Coba lagi!")
    