# This is a string object
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string start with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

index = name.find('war')
if index != -1:
    print('Yes, it contains the string "war" at {0:_>3}'.format(index))

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
