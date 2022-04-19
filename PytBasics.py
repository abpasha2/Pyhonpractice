# Python program to get three numbers and do basics operations
"""
This can be used fpr document serves as multiline comments
Use this for documentation
"""
def docstrfunc():
    """
    This is sample function to explain
    to generate 
    :return:
    """
print(type(1))
print(type(3.14))
print(type('papaya'))
print(type(True))
print(type(False))
print(type(None))
print(type([1, 2, 10]))
print(type({'apple': 'A round fruit', 'banana': 'A long yellow fruit',
            'cucumber': 'A long green fruit'}))

a = input('Enter A number :: ')
b = input('Enter B number :: ')
c = input('Enter C number :: ')

if a > b:
    if a > c:
        print('Number A is greatest')
    else:
        print('Number C is greatest')
elif b > c:
    print('Number B is greatest')
else:
    print('Number C is greatest')

# Program to evaluate Python operators
