def func(a, b=5, c=10):

    print('a is {0:3}'.format(a),
            '\n\tand b is {0:3}'.format(b),
            '\n\t\tand c is {0:3}'.format(c))

func(3, 7)
func(25, c=24)
func(c=50, a=100)

