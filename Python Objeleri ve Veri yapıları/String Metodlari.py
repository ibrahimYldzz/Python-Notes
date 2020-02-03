# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 00:02:49 2020

@author: ibrahim
"""

#Split metodu, karakter dizisinde belirtilen bir karaktere göre parçalama işlemi yapar.
#defaultu boşluktur. 

message = 'Hello, World.'
message = message.split(',')   # ['Hello',' World']

#Upper metodu, karakterleri büyük harfe çevirir.

message = 'Hello World.'
message = message.upper()  # HELLO WORLD.

#Lower metodu, karakterleri büyük harfe çevirir.

message = 'HELLO WORLD.'
message = message.lower()  # hello world.

#title() metodu, karakter dizisindeki her kelimenin baş harfini büyük harfe çevirir.

message = 'hello world.'
message = message.title()  # Hello World.

#capitalize(), karakter dizisindeki sadece ilk kelimenin baş harfini büyük harfe çevirir.

message = 'hello world.'
message = message.title()  # Hello world.


#Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. 
#Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.
#lstrip() soldan, rstrip() sağdan siler.

username = "     ibrahim     "
x = username.strip()
print("my username is +  x")  # my username is ibrahim


#Replace metodu karakter güncellemesi için kullanılır. 
#replace() metotlarını ard arda kullanabiliriz.

message = 'My name is İbrahim Yıldız'
message = message.replace('İbrahim','Ahmet')  # My name is Ahmet Yıldız

#Find metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa exception döndürür.
#index metodu verilen string ifade içinde arama yapar ve bulduğu ilk indeks numarasını döndürür. Eğer bulamazsa find metodundan farklı olarak geriye -1 değerini döndürür.

txt = "My name is İbrahim Yıldız."
x = txt.find("name")
print(x)  # x = 3


#Ayrıca index ve find metodu için bir arama kapsamı belirtebiliriz.
index("aranılacak ifade", "başlangıç indeksi","bitiş indeksi")

#count() stringde kaç tane karakter olup olmadığını döndürür.
result = website.count('www',0,10)  # 0 ile 10. indeks arasında www ifadesi sayılır.
result = website.count('a')         # a karakteri sayılır.

#startswitch-edswitch
result = website.startswith('www')    # website www ile başlıyor mu ? False
result = website.startswith('http')   # website http ile başlıyor mu ? True
result = website.endswith('com')      # website com ile bitiyor mu ? True









