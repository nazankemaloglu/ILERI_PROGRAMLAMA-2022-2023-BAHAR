

carpim=1
sayi=int(input("Lütfen bir sayı giriniz."))

for i in range(1,sayi+1):
    carpim=carpim*i
print(carpim)

#------------ while --------------------------------#

carpim=1
sayi=int(input("Bir sayı girin"))

while sayi>1:
    carpim=carpim*sayi
    sayi=sayi-1
print(carpim)

#Klavyeden 0 girilene kadar pozitif ve negatif sayılar girilecek; Girilen sayıların kaçı negatif? kaçı pozitif? Sayıların ortalaması ?

negSayi=0
pozSayi=0
toplam=0
sifirDegil=True

while sifirDegil:
    sayi=int(input("Sayı girin"))
    if sayi>0:
        pozSayi=pozSayi+1
        toplam=toplam+sayi
    elif sayi<0:
        negSayi=negSayi+1
        toplam=toplam+sayi
    else:
        sifirDegil=False
    
print("Negatif sayı adedi", negSayi)
print("Pozitif sayı adedi",pozSayi)
ortalama=toplam/(pozSayi+negSayi)
print("Ortalama ",ortalama)

#---Toplamda 3 cevap hakkı verilen bir sayı tahmin oyununda;-----#

import random

sayi=random.randint(0, 100)

for i in range(0,3):
    tahmin=int(input("Tahmini girin"))
    if tahmin==sayi:
        print("Tebrikler bildiniz")
        break
    else:
        print("Yanlış tahmin")
        
#--------- Asal sayı--------#

sayi=int(input("Sayı girin"))
asalMi=True
for i in range(2,sayi):
    if sayi%i==0:
        asalMi=False
        break
    
if asalMi:
    print("Sayı asaldır")
else:
    print("Sayı asal değildir")
    




        
        
        





























    
    
    
    
    
    
    
    
    
    
    
