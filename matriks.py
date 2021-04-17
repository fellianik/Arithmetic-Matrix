def penjumlahan():      #Addition A + B function
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

def pengurangan_ab():       #subtraction A - B function
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

def pengurangan_ba():           #subtraction B - A function
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

def perkalian_ab():         #Multiplication A * B function
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

def perkalian_ba():         #Multiplication B * A function
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

#determinant A function
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

#determinant B function
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

#looping function
def perulangan():
    lanjut = input("\nIngin melanjutkan[Y/T]? = ")      #want to continue?
    for i in lanjut:
        if lanjut == 'Y':
            continue
            print()
        else:
            print("\nTerima kasih telah menggunakan program ini!\U0001F600\n")      #Thank you for using this program
            exit()

# MAIN PROGRAM
print("==========PROGRAM PERHITUNGAN MATRIKS==========")

while True:
        try:
            ordo = int(input("Masukkan ordo: "))        #input ordo
            if ordo < 1:
                raise ValueError
            break
        except ValueError:
            print("Input anda bukan angka lebih dari 0")        #the input not a number > 0

print("Masukkan", ordo*ordo, "Elemen dalam Matriks\n")  #input the elemen in matrix

print("Matriks A =")
a = []   # a = matriks A
for i in range(ordo):
    a.append([])
    for j in range(ordo):
        while True:
            try:
                a[i].append(int(input("Masukkan elemen [%d][%d]: " %(i+1, j+1))))       #Insert elements
                break
            except ValueError:
                print("Input anda bukan angka")     #input not a number

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
                b[i].append(int(input("Masukkan elemen [%d][%d]: " %(i+1, j+1))))       #Insert elements
                break
            except ValueError:
                print("Input anda bukan angka")         #input not a number

print("\nMatrik B =")
for baris in b:
    print("|\t", end='')
    for kolom in baris:
        print("%d\t" %kolom, end='')
    print("|")

print()

while True:
    print("Pilihan Perhitungan Matriks:")       #menu of arithmetic matrix
    print("1. Penjumlahan Matriks")     #addition
    print("2. Pengurangan Matriks")     #subtraction
    print("3. Perkalian Matriks")       #multiplication
    print("4. Determinan Matriks")      #determinant
    print("===============================================")
    pilihan = int(input("Masukkan Pilihan:"))       #enter the option
    if pilihan == 1:
        penjumlahan()
        perulangan()
    elif (pilihan==2):
        print("\nPilihan pengurangan:")     #reduction options
        print("1. A - B")
        print("2. B - A")
        pilih = int(input("Masukkan pilihan: "))            #enter the option
        if pilih == 1:
            pengurangan_ab()
        elif pilih == 2:
            pengurangan_ba()
        else:
            print("Pilihan salah")      #input wrong
        perulangan()
    elif (pilihan==3):
        print("\nPilihan perkalian:")       #multiplication options
        print("1. A x B")
        print("2. B x A")
        pilih = int(input("Masukkan pilihan: "))        #enter the option
        if pilih == 1:
            perkalian_ab()
        elif pilih == 2:
            perkalian_ba()
        else:
            print("Pilihan salah")      #input wrong
        perulangan()
    elif (pilihan==4):
        pilih = input("\nMatriks apa yang dihitung?[A/B] = ")           #What matrix is calculated?
        if pilih == 'A':
            determinan_a(a)
            print("\nHasil determinan matriks A adalah =", determinan_a(a))     #The result of the determinant of matrix A is
        elif pilih == 'B':
            determinan_b(b)
            print("\nHasil determinan matriks B adalah =", determinan_b(b))     #The result of the determinant of matrix B is
        else:
            print("Pilihan salah")      #input wrong
        perulangan()
    else:
        print("Masukkan Anda Salah!")       #input wrong
        print("Coba lagi!")         #try again

'''
Program by:
Felliani Kurniawati
'''
