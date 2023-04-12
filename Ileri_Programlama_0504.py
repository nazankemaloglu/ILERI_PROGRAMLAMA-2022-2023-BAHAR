#String içerisinde yer alan sesli harfleri bulan kod

metin=input("Bir metin girin")

sesli="aeiöüuıoAEİÜÖUIO"

for s in metin:
    if s in sesli:
        print(s,end=",")
        
#-----------------Sesli sessiz harf ayıran kod---------------#

metin="python üst düzey bir programlama dilidir." 
 
sesli="aeiöüuıo"
sessiz="rtypğsdfghjklşzcvbnmç"

sesli_harfler=""
sessiz_harfler=""

for s in metin:
    if s in sesli:
        sesli_harfler=sesli_harfler+s
    if s in sessiz:
        sessiz_harfler=sessiz_harfler+s
        
print("Sesli harfler=",sesli_harfler)
print("Sessiz harfler =",sessiz_harfler)

#-------------------------Harf tekrarı-------------------------

metin="python üst düzey bir programlama dilidir." 

harf=input("Bir harf girin")

sayac=0

for s in metin:
    if s==harf:
        sayac=sayac+1
        #sayac+=1
        
print("Cümle içerisinde", sayac," adet", harf, "harfi vardır")

#------------------------Türkçe karakter tespiti---------------

sifre=input("Bir şifre girin")

turkce_karakter="ğüşçıüöĞÜŞİÇÖ"

for s in sifre:
    if s in turkce_karakter:
        print("Şifreniz Türkçe karakter içermemelidir.")
    else:
        print("Şifreniz başarılı")
        
#----------------------İki kelime arasındaki farklı harfler-------------

kelime1=input("Bir kelime girin")
kelime2=input("Bir kelime girin")

for s in kelime2:
    if s not in kelime1:
        print(s,end="-")
     
#-----------Ortak harfler----------------------

kelime1=input("Bir kelime girin")
kelime2=input("Bir kelime girin")

for s in kelime1:
    if s in kelime2:
        print(s,end="-")





     

    
