# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:58:26 2020

@author: ibrahim
"""

#String tanımlamak için tek veya çift tırnak kullanırız.

a = "İstanbul"
b = 'Ankara'

#Birden fazla string tanımlamak için ardarda 3 tek veya çift tırnak kullanabiliriz.


text = """Ankara,
    İstanbul, 
    Adana,
    İzmir, 
    Sivas,
    Kocaeli"""
print(text)


#String birleştirme işlemini + operatörü ile yapabiliriz.

name = 'İbrahim'
surname = 'Yıldız'
age = 22

text = 'My name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + ' years old.'
print(text)  # My name is İbrahim Yıldız and I am 22 years old.



#String format metodu

print('My name is {} {}'.format(name, surname)) # My name is İBrahim Yıldız

print('My name is {1} {0}'.format(name, surname))  # My name is Yıldız İbrahim

print('My name is {s} {n}'.format(n=name, s=surname))  # My name is Yıldız İbrahim

#Eğer format metodunda bir int değer kullanmak istersek o değeri stringe dönüştürmemiz gerekmez.

print("My name is {} {} and I'm {} years old.".format(name, surname, age))

#Bir başka birleştirme metodu

print(f"My name is {name} {surname} and I'm {age} years old.")



#String Parçalama

result = text[0] 
print(result)  # M  

result = text[3] 
print(result)  # n 

result = text[-1] 
print(result)  # . Dizinin son karakterini gösterir.

result = len(text)
print(result)  # 44 . Dizinin uzunluğunu verir.

result = text[len(text)-1] 
print(result)  # . Dizinin son elemanının indeks nosu uzunluk-1 dir.

result = text[3:7] 
print(result)  # name. Diziyi bu şekilde bölebiliriz.

result = text[:7] 
print(result)  # My name. En baştan 7. indekse kadar böler.7. indeks dahil değil.

result = text[3:] 
print(result)  # name is İbrahim Yıldz and I'm 22 years old.Burada 3. indeksten sona kadar alır.

result = text[0:10:2]
print(result) # M aei.0. indeksten başlayarak 10. indekse kadar ikişer ikişer artarak gider.







