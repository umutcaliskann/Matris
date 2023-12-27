def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#Satır ve Sütün toplamları
import random

boyut = int(input("Boyut giriniz:"))


matris = [[int(random.random()*10) for i in range(boyut)]for j in range(boyut)]


satirtoplam = []
sütüntoplam = []

for i in range (boyut):
    satirtop = 0
    for j in range(boyut):
        satirtop += matris[i][j]
    satirtoplam.append(satirtop)

for k in range(boyut):
    sütüntop = 0
    for j in range(boyut):
        sütüntop += matris[j][k]
    sütüntoplam.append(sütüntop)
    

yazdir(matris)
print()

#Satır toplamları
for i in range (1,boyut+1):
    print(f"{i}. satır toplamı: {satirtoplam[i-1]}")
print()

#Sütün toplamları
for i in range (1,boyut+1):
    print(f"{i}. sütün toplamı: {sütüntoplam[i-1]}")