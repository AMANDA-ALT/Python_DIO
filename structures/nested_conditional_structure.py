common_account = True
student_account = False

balance = 2000
withdraw = 1500
overdraft = 450

if common_account:
    if balance >= withdraw:
        print('Withdraw successfully done!')

    elif withdraw <= (balance + overdraft):
        print('Withdraw successfully done, using overdraft')

    else:
        print('Insufficient funds')    

elif student_account:
    if balance >= withdraw:
        print('Withdraw successfully done')

    else:
        print('Insufficient funds')
else:  
        print('Type of account was not identified')  

