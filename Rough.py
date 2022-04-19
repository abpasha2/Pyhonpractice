import math
for i in range(99,200):
    print('------------------------------------------------------')
    print(f'The number is :: {i}')
    fnum = str(i)
    sum = 1
    for j in fnum:
        temp = j
        sum = sum * int(temp)

    sqrt = math.sqrt(int(fnum))
    print(f'Square root of the number using function is :: {sqrt}')
    print(f'Square root of the number using trick is :: {sum-2}')
    print('------------------------------------------------------')
# def printSpecNames(names, val_to_pic):
#    for name in val_to_pic:
#        print("Hello {}".format(names[name]))
# namelist = ['ABu', 'Abubakar', 'Abubakar Pasha', 'Cheena', 'Cheens', 'Macau','some','name']
# printSpecNames(namelist,[0,2,5,7])

# def printName(names="Abubakar"):
#    for name in names:
#        print(f'Hello {name}')
# namelist=['ABu','Abubakar','Abubakar Pasha','Cheena','Cheens','Macau']
# printName(namelist)
