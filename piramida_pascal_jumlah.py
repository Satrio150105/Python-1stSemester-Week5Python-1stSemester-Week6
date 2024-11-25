n = int(input("Masukkan angka: "))

for i in range(n):
    print(' '*(n-i), end='')

    coef = 1
    row_sum = 0
    for j in range(0, i + 1):
        print(coef, end=' ')
        row_sum += coef
        coef = coef * (i - j) // (j + 1)
    print(f"Jumlah: {row_sum}")