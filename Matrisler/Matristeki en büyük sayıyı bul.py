def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()
        
#Matristeki en büyük sayıyı bul.
import random
boyut=int(input("Boyut giriniz:"))

matris = [[int(random.random()*10)for i in range(boyut)]for j in range (boyut)]

yazdir(matris)
print()

max = matris[0][0]
for satir in matris:
        for sayi in satir:
            if sayi > max :
                 max = sayi

print("Matristeki en büyük sayı:" ,max)