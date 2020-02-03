# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 10:53:02 2020

@author: ibrahim
"""

#Pythonda listeler, elemanları sıralanabilir, güncellenebilir ayrıca her bir eleman liste içerisinde birden fazla tekrarlanabilir.

list1 = [1,2,3]
list2 = ['bir',2, True, 5.6]

message = 'Hello There. My name is İbrahim Yıldız'.split()
print(message)    # ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']
print(message[0]) # Hello


kullaniciA = ['İbrahim', 22]
kullaniciB = ['Yıldız', 10]

kullanicilar = [kullaniciA,kullaniciB] #Bu listeleri farklı bir listede gruplandırabiliriz

#Python listelerinde eleman sayısını len() metodu ile öğrenebiliriz.

list1 = ['one','two','there']
list2 = [[1,2,3],[4,5,6],[7,8,9],10]

print(len(list1)) # 3
print(len(list2)) # 4

#Python listelerindeki her bir elemanına soldan itibaren 0' dan başlayarak indeks numarası ile ulaşabiliriz. Aynı şekilde sağdan -1. indeks numarasından başlamalıyız.

message = ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']

print(message[2])   # My
print(message[4])   # is
print(message[-1])  # Yıldız
print(message[-3])  # is

#Liste elemanlarına döngüler ile erişebiliriz.

names = ['ahmet','mehmet','cenk']
for name in names:
   print(name)


#Liste Parçalama
   
message = ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']
print(message[0:2])  # ['Hello', 'There.']   

message = ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']
print(message[:2])  # ['Hello', 'There.']

message = ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']
print(message[2:])  # ['My', 'name', 'is', 'İbrahim', 'Yıldız']

message = ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız']
print(message[::])  #  ['Hello', 'There.', 'My', 'name', 'is', 'İbrahim', 'Yıldız'] # Hepsini seçmiş oluruz.

#Liste Elemanları güncelleme.

list1 = ['one','two','there']
list1[1] = 'updated'
print(list1)  # ['one','updated','there']