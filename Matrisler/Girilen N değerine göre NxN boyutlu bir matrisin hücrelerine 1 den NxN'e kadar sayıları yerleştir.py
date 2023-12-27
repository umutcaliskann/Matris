def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.

boyut= int(input("Boyut Giriniz:"))
matris = [[0 for i in range(boyut)] for j in range(boyut)]

sayac = 1
for i in range(boyut):
    for j in range(boyut):
        matris[i][j] = sayac
        sayac += 1

yazdir(matris)