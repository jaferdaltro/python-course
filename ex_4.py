number = input('digite um numero inteiro: ')

is_int = number.isdigit

# if is_int:
#     number = int(number)
#     if number % 2 == 0:
#         print(f'{number} é um número par')
#     else:
#          print(f'{number} é um número impar')
# else:
#     print('{number} não é um inteiro')

try:
    number = int(number)
    if number % 2 == 0:
        print(f'{number} é um número par')
    else:
         print(f'{number} é um número impar')
except:
    print(f'{number} não é um inteiro')


try:
    ...
except:
    pass

