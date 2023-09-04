# Para identar precisar por : e depois tem de dar 4 espaços , é intrusivo mas é assim que  a linguagem lê a identação dos blocos

def withdraw(ammount):
    balance = 500

    if balance >= ammount:
       print('withdrawed money!')
       print('withdraw your money at the cashier')

    print('Tks for being our customer, have a nice day!')   


def deposit(ammount):
    balance = 500
    balance += ammount


withdraw(1000)

