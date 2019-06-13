x = 50
y = 30

def func(x):

    print('x is ', x)

    x = 2
    print('Changed local x to', x)

def func_np():
    global y

    print('y is ', y)

    y = 2
    print('Changed local y to', y)


func(x)
print ('x is staill', x)

print ('#########################################')
func_np()
print ('y is not staill', y)

