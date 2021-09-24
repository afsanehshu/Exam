Dict = {}

stu_num = int(input("Enter number of student : "))
lesson_num = int(input("Enter number of lesson : "))

print()

for i in range(stu_num):
     code = input("code : ")
     Dict[code] = {}
     Dict[code]["Name"] = input("Enter the Name : ")

     for j in range(lesson_num):
          Dict[code]["Mark%d"%(j+1)] = int(input("Enter the Mark%d : "%(j+1)))

print()
print("DIct is : \n",Dict)


Dict_Ave = {}

for i in Dict:
     Dict_Ave[i] = {}
     Sum = 0
     k = 0
     for j in Dict[i]:
          if j != "Name":
               Sum+=Dict[i][j]
          else :
               Dict_Ave[i]["Name"]=Dict[i][j]
               
          average = Sum/lesson_num
          Dict_Ave[i]["Average"] = average

print("\nDict of Average : ",Dict_Ave)

Max = 0
for i in Dict_Ave:
     if Dict_Ave[i]["Average"] > Max :
          Max=Dict_Ave[i]["Average"]
          k=i


print ('\nGreat Average is %.2f'%Max)
print ('Student code:%s    Student name:%s'%(k,(Dict_Ave[k]['Name'])))
