def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#iki matris toplamı 

import random
boyut = int(input("Boyut Giriniz:"))

a = [[int(random.random()*10) for i in range(boyut)] for j in range (boyut)]
b = [[int(random.random()*10) for i in range(boyut)] for j in range (boyut)]
toplam = [[0 for i in range(boyut)] for j in range (boyut)]

yazdir(a)
print()
yazdir(b)
print()

for i in range (boyut):
    for j in range(boyut):
        toplam[i][j] = a[i][j] + b[i][j]
    

yazdir(toplam)