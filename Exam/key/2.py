year = int(input("Enter years : "))

x = 1

while x != 2:
     year +=1
     List = []
     for i in str(year):
          if i not in List:
               List.append(i)
               x = 2
          else:
               x = 1
               break

print(int("".join(List)))
print()
print(year)
