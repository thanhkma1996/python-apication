#Kieu so trong python int float complex
import random

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))
print(random.randrange(1, 10))

#python boolean 
test1 = 3
test2 = 5 
if(test1 > test2):
    print('so test1 lon hon test2')
else:
    print('so test1 nho hon test2')

#Danh gia gia tri cua bien bool()
print(bool("test"))
print(bool(-1))
print(bool(0))

x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2 

#Python Access list item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

print(thislist[:4])

thislist1 = ["apple", "banana", "cherry"]
if "apple" in thislist1:
  print("Yes, 'apple' is in the fruits list")

#Python change list item

thislist2 = ['tao','cam','xoai']
thislist2[1] = 'mut tet'
thislist2[1:2] = 'xin chao','cac ban'
print(thislist2)

#insert item to list
list1 = ['xin chao','cac ban','python']
list1.insert(3,'no that tuyet voi')
print(list1)

#append item to list
thislist22 = ["apple", "banana", "cherry"]
thislist22.append("orange")
print(thislist22)

#extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#remove item to list
mangtest2 = ["1","2","3","4"]
# mangtest2.remove("1")
print(mangtest2)

#xoas chi muc dax chi dinh
mangtest2.pop(2)
# mangtest2.pop() no se phan tu cuoi cung
print(mangtest2)

del mangtest2[0]
print(mangtest2)

# mangtest2.clear() xoa tat ca phan tu trong mang