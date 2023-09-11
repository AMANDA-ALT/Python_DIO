name = 'Amanda'
age = 40
profession = 'Developer'
language = 'Python'
saldo = 45.435

dados = {'name': 'Amanda', 'age': 40}

print('Name: %s Age: %d ' % (name, age))
print('Name: {} Age: {} '.format(name, age))
print('Name: {1} Age: {0} Name: {1} {1} {1}'.format(age, name))
print('Name: {name} Age: {age}'.format(age = age, name = name))
print('Name: {name} Age: {age}'.format( name = name, age = age))
print('Name: {name} Age: {age}'.format(**dados))

#forma correta de usar
print(f'Nome: {name} Age: {age} Saldo: {saldo:10.2f}')




