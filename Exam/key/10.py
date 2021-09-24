string = input("Enter : ")

w = ' '
for char in string.lower():
    x=(string.lower()).count(char)
    if char not in w:
        print(char,':',x)
        w+=char

'''

String = input("Enter : ")

Dict = {}

for i in String:
     if i in Dict:
          Dict[i]+=1
     else:
          Dict[i]=1
print(Dict)

'''


'''

from collections import Counter

String = input("Enter : ")

S = list(String)

S1 = Counter(S)

print(S1)

'''
