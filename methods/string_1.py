name = 'AmAnDa'

print(name.upper())
print(name.lower())
print(name.title())

text = "   Hello World   "

print(text + '.')
print(text.strip() + '.')
print(text.lstrip() + '.')
print(text.rstrip() + '.')

menu = 'Python'

print('####' + menu + '####')
print(menu.center(14, '#'))
print(menu.center(20, '#'))
print('_'.join(menu))

for letra in menu:
    print(letra, end='-')