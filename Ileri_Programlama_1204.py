#0 ile 100 arasında rastgele olacak şekilde 10 sayı oluşturup bu sayıları bir liste içerisine aktaran ve yine bu liste içerisindeki sayıların kaç tanesinin 50’den küçük olduğunu yazdıran Python uygulamasını kodlayınız.


import random as rnd

liste1=[]

for i in range(0,10):
    sayi=rnd.randint(0, 100)
    liste1.append(sayi)
    
sayac=0

for j in liste1:
    if j<50:
        sayac=sayac+1
        
print(sayac," adet sayı 50'den küçüktür.")

#0 ile 100 arasında rastgele olacak şekilde 10 sayı oluşturup bu sayıları bir liste içerisine aktaran ve yine bu liste içerisindeki sayıların kaç tanesinin ortalamadan yüksek olduğunu bulan kodu yazın.

import random as rnd

liste1=[]
liste2=[]
for i in range(0,10):
    sayi=rnd.randint(0, 100)
    liste1.append(sayi)
    
toplam=sum(liste1)

ort=toplam/(len(liste1))

sayac=0

for i in range(0,len(liste1)):
    if liste1[i]>ort:
        liste2.append(liste1[i])
        sayac=sayac+1
        

print(sayac, " adet sayı ortalamanın üstündedir")
print(liste2) 

#Yukarıdaki cümlenin elemanlarından oluşan bir liste içerinde karakter sayısı 7’ten büyük olan elemanları bulan kodu yazın. 

cumle="Belirli bir düzende otomatik listeler oluşturmak için liste üreteçleri kullanılır" 
    
kelime=cumle.split(" ")

for i in kelime:
    if len(i)>7:
        print(i)

#. 'GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms‘ elemanlarından oluşan liste içerisinde Geek stringinin kaç defa geçtiğini bulan kodu yazın. 

liste=['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

aranan_kelime='Geek'

sayac=[a for a in liste if aranan_kelime in a]
boyut=len(sayac)
  
    
    


