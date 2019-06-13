shoplist = [ 'apple', 'mango', 'carrot', 'banana' ]
name = 'swaroop'

# Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('\nshoplist are', shoplist)
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string #
print('\ncharacters is', name)
print('characters is 0123456')
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

# Slice step
print('Step 1 :', shoplist[::1])
print('Step 2 :', shoplist[::2])
print('Step 3 :', shoplist[::3])
print('Step -1 :', shoplist[::-1])

bri = set(['brazil', 'russia', 'india'])
print('india in bri : ', 'india' in bri)
print('usa in bri : ', 'usa' in bri)

bric = bri.copy()
bric.add('china')

print('bric.issuperset(bri) :', bric.issuperset(bri))

bri.remove('russia')

print('bri  : ', bri)
print('bric : ', bric)

print('bri & bric : ', bri & bric)

