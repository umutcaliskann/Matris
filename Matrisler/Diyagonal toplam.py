def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#Diyagonal toplam

import random

boyut = int(input("Boyut giriniz:"))

matris = [[int(random.random()*10) for i in range(boyut)]for j in range(boyut)]
yazdir(matris)
print()

diyagonaltop = 0

for i in range(boyut):
    for j in range(boyut):
        if i == j:
            diyagonaltop += matris[i][j]

print("Diyagonal Toplam:" , diyagonaltop)
