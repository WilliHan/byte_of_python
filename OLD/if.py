number = 23
# for python 2.x
# guess = int(raw_input('Enter an integer : '))
# for python 3.x
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print ('Congratulations, you guessed it.')
    print ('(but you do not win any prizes !)')
    # New block ends here
elif guess < number:
    # Another block
    print ('No, it is a little highter than that')
    # You can do whatever you want in a block  ....
else:
    print ('No, it is a little lower than that')
    # you must have guessed > number to reach hear

print ('Done')
# This last statement is always executed,
# after the if statement is executed.
