def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#İki matrisin çarpımını hesaplayan prog?
import random

boyut = int(input("Boyut giriniz:"))

a = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
b = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
toplam = [[0 for i in range(boyut)]for j in range(boyut)]

yazdir(a)
print()
yazdir(b)
print()

for i in range(boyut):
    for j in range(boyut):
        for k in range(boyut):
            toplam[i][j] += a[i][k]*b[k][j]

yazdir(toplam)