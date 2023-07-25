'''
Iterando com while
'''

name = 'Jafer Daltro'
new_name = ''

iterator = 0

while iterator < len(name):
    new_name = f"# {name[iterator]}"
    iterator += 1
print(new_name)
