# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:37:49 2020

@author: ibrahim
"""

#Pythonda veri saklamak için oluşturdugumuz alanlara değişken denir.

x = 5
y = 10
z=x+y  # 15
k

print(x)  # 5
print(y)  # 10
print(z)  # 15
print(k)  # NameError: name 'k' is not defined.



#String bir değişken oluştururken tek veya çift tırnak kullanmalıyız.

name = "İbrahim"
surname = 'Yıldız'
age = "50" #String bir değerdir.

a = 50             # sayısal olarak 50 değeri tanımladık.
b = "50"           # sözel (string) olarak 50 değeri tanımladık.
toplam = a + b     #100 değerini döndürmesi beklenirken 5050 gibi bir değer döndürür.
print(type(toplam)) #Bu tiü bir yazdırma işlemi hata verir.String bir değer ile int değer toplanamaz!



x = 10
x = 20 #x'in içindeki değer silinir ve 20 değerini alır.
x += 10 #x en son 20 iken +10 değer alır ve 30 olur.



#Değişken isimleri rakam ile başlayamaz!!!

1ad => hatalı
ad1 => geçerli
_ad => geçerli



#Büyük küçük harf duyarlılığı vardır.

yas = 50
Yas = 100

#bool(Boolean) veri tipi bir durumun doğru(True, 1) yada yanlış(False, 0) olması hakkında bilgi tutar.

isStudent = True
isEngineer = 0

print(type(isStudent)) # <class 'bool'>

#Pythonda aynı satırlarda değişkenler tanımlayabiliriz.

a, b, name, isStudent = 1, 5.0, 'Ahmet', True

