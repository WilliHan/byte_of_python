def print_max(a, b):
    if a > b:
        max = a
    elif a == b:
        print(a, 'is equal to', b)
        return()
    else: # a < b:
        max = b
    print(max, 'is maximum')

# directly pass literal values
print_max(3, 4)

x = 5
y = 7

# pass variables as arguments
print_max(x, y)


x = 9
y = 9

# pass variables as arguments
print_max(x, y)


