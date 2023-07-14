name =  input('Insira o seu nome: ')
age =  input('Insira a sua idade: ')

if name and age:
    print(f'seu nome é {name} e sua idade é {age}')
    print(f'seu nome invertido é {name[::-1]}')
    if ' ' in name:
        print(f'seu nome contém espaços em branco')
    else:
        print('seu nome não contém espaços em branco')
    print(f'seu nome contém {len(name)} letras')
    print(f'a primeira letra do seu nome é {name[0]} e a ultima é {name[-1]}') 
else:
    print('vc n digitou nada!!')   