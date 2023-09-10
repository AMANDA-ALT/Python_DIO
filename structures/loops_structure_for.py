# text = input('Inform a text: ')
text = ''
VOGALS = 'AEIOU'

#Exemple using iterated

for letter in text:
    if letter.upper() in VOGALS:
        print(letter, end= '')
else:       
    print() #quebra de linha
    print('runs in the end of the loops')

#example using function built-in range

for number in range(0,51,5):
    print(number, end= '')