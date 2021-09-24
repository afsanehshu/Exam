salary = int(input("Enter your Salary : "))


if 0 < salary <= 500:
    tax = 0
    
elif 500 < salary <= 1000:
    tax = 0.1
    
elif 1000 < salary <= 3000:
    tax = 0.2
    
elif 3000 < salary <= 5000:
    tax = 0.3

elif 5000 < salary <= 10000:
    tax = 0.4

else:
    tax = 0.5
    
print("your tax :",int(salary*tax))
