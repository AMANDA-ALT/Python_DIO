LEGAL_AGE = 18
SPECIAL_AGE = 16

age = int(input('Inform your age: '))

if age  >= 18:
    print('Legal age, you can get your driving license')

if  age < LEGAL_AGE:
    print('You cannot get your driving license yet')    

if age >= LEGAL_AGE:
    print('Go for it!')

else:
    print('No way!')

if age  >= 18:
    print('Legal age, you can get your driving license')

elif age == SPECIAL_AGE:
    print('You can only attend theoretical lessons')

else:
    print('No way!')

