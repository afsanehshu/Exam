Grade = input("Enter your blood grade : ")


if Grade.lower() == 'o-' :
    print('O+ A+ A- B+ B- AB+ AB-')
elif Grade.lower() == 'o+' :
    print('O+ A+  B+ AB+ ')
elif Grade.lower() == 'a-' :
    print('A+ A- AB+ AB-')
elif Grade.lower() == 'a+' :
    print('A+ AB+')
elif Grade.lower() == 'b-' :
    print('B+ B- AB+ AB-')
elif Grade.lower() == 'b+' :
    print('B+ AB+')
elif Grade.lower() == 'ab-' :
    print(' AB+ AB-')
elif Grade.lower() == 'ab+' :
    print(' AB+')
