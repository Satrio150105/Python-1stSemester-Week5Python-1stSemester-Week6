n = int(input("Masukkan angka: "))

for i in range(n):
    print(' '*(n-i), end='')

    coef = 1
    for j in range(0, i + 1):
        print(coef, end=' ')
        coef = coef * (i - j) // (j + 1)
    print()