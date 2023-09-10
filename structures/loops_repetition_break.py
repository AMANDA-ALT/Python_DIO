'''while True:
    number = int(input('Inform a number: '))

    if number == 10:
        break

    print(number)
    '''


for number in range (100):

    if number  % 2 != 0:
        continue

    print(number, end='')
