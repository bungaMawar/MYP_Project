loop = 0
while loop == 0:
    binary_num = input('Enter a binary number: ')

    other_num = 0
    base = int(2 ** (len(binary_num) - 1))
    for letter in binary_num: 
        if letter == '1':
            other_num = other_num + base
            base = base // 2
        elif letter == '0':
            other_num = other_num + 0
            base = base // 2
        else:
            quit()
    print (f'{binary_num} is equal to {other_num}')
           
"""for _ in '123':
    firstNumber = float(input('Enter a number: '))
    secondNumber = float(input('Enter a second number: '))
    thirdNumber = float(input('Enter a third number: '))

    print (f'Your numbers are {firstNumber, secondNumber, thirdNumber}')

    average = (firstNumber + secondNumber + thirdNumber) / 3

    print (f'Your average is {average}')"""



