def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()
        
#Verilen sayıyı matrisin k. indeksine yerleştir?
import random

boyut = int(input("Boyut giriniz:"))
sayi = int(input("Yerleştirilecek sayıyı giriniz:"))
satir = int(input("İndeks satırı:")) ; sütün = int(input("İndeks sütünü:"))

matris = [[int(random.random()*10)for i in range(boyut)]for j in range(boyut)]
yazdir(matris)
print()

for i in range(boyut):
    for j in range(boyut):
        if j+1 == sütün and i+1 == satir:
            matris[i][j] = sayi

yazdir(matris)