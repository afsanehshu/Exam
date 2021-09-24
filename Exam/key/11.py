sentence=input('Enter your sentence: ')
sp=sentence.split(' ')
print (sp)
final_s=''
for i in sp:
    if i[0].islower()== True :
        final_s+=i[::-1]
    else:
        final_s+=i
    final_s+= ' '
print(final_s)
