def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number

    for key in keywords:
        count += keywords[key]
        print ("{0:.<20}".format(key) + " : " + str(keywords[key]))
        print ("{0:*>20}".format(key) + " : " + str(keywords[key]))
    return count

print(total(10,1,2,3, vegetables=50, fruits=100))
