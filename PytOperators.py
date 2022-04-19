# list declaration
a = []
print(type(a))

# populate list
a = [1,2,3,4,5,6,7]

# Retrieve list items
print(a[2])
print(a[-2])                # fetch from last
print(a[0:2], a[3:5])       # range of elements
print(a[-3:-1])             # range from last


# list operations
# update list items
b = ['Red','Green','Blue','Orange','Purple']
print(b)
b[1] = "GREEN"
b[2:4] = ['BLUE','ORANGE']
print(b)

print("Yellow" in b)                # checking an element in list
print("Red" in b)                   # checking an element in list

for i in b:                         # retrieving all elements using for loop
    print(i)

b.append('Yellow')                  # add item at end
b.insert(2, 'Brown')
print(b)

newList = b.copy()
print("Copied list :: \n",newList)  # Copy a list

# Tuples (unmutable list)

tupA = (1,2,3,4,5,6,7,8,9,10)
print("Printing tuples below \n", tupA)     # printing a tuple
print(tupA[1:3])                            # retrieving tuple elements
print(tupA[-1])                             # retrieving tuple elements from back

for i in tupA:                              # retrieving all tuple elements using for loop
    print(i)

# tupA[1] = '7'                               # invalid for a tuple, can't update
