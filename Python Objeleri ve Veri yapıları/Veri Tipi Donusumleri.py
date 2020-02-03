# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:52:49 2020

@author: ibrahim
"""

#Pythonda bazı durumlarda veri tipi dönüşümüne ihtiyac duyarız.
#Örneğin aldığımız her input değer bize string olarak gelir.
#Bunları matematiksel işlemler gibi bazı yerlerde kullanmak için int, float tiplerine dönüştürürüz.

x = input('1.sayı: ') #str
y = input('2.sayı: ') #str

toplam = x + y
print(toplam) #str

#Dönüşümü şu şekilde yaparız.

toplam = float(x) + float(y)
print(toplam) #float



int(a)
float(b)
str(c)