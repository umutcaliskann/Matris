def yazdir(matris):
    for i in range (len(matris)):
        for j in range (len(matris)):
            print(matris[i][j], end = " ")
        print()

#Matrisin transpozunu alma

import random 

boyut= int(input("Boyut Giriniz:"))

matris = [[int(random.random()*10) for i in range(boyut)]for j in range(boyut)]
yazdir(matris)
print()

for i in range(boyut):
    for j in range (i,boyut):
        matris[i][j],matris[j][i] = matris[j][i],matris[i][j]
        

print("Transpozu")
yazdir(matris)