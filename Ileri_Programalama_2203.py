# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:33:57 2023

@author: nzn_k
"""
#1-10 arasındaki sayıların toplamı
toplam=0

for i in range(1,11):
    toplam=toplam+i
print(toplam)

#1-10 arası tek ve çift sayıların toplamı

cift_toplam=0
tek_toplam=0

for i in range(1,11):
    if i%2==0:
        cift_toplam=cift_toplam+i
    else:
        tek_toplam=tek_toplam+i
        
print("Tek sayıların toplamı=",tek_toplam)
print("Çift sayıların toplamı =",cift_toplam)

#Klavyeden girilen sayının faktoriyeli

carpim=1
sayi=int(input("Lütfen bir sayı giriniz."))

for i in range(1,sayi+1):
    carpim=carpim*i
print(carpim)

# tOPLAM SEMBOLÜ İLE FOR DÖNGÜSÜ

toplam=0
sayi=int(input("Bir sayı girin"))

for i in range(0,sayi+1,1):
    toplam=toplam+(i*5+6)
print(toplam)
    

# Doğru yanlış sayısı ile puan hesaplama

dogru=int(input("Doğru sayısını girin"))
yanlis=int(input("Yanlış sayısını girin"))

if dogru+yanlis==10:
    toplam=(dogru*10)-(yanlis*5)
    print(toplam)
else:
    print("Doğru ve yanlış sayılarının toplamı 10 olmalıdır. ")


    
    
    
    
    
