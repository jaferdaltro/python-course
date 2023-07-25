while True:
    numero_1 = input('Digite o número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')

    numeros_validos = False
    operators = '+-/*'
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = False
        print(error)

    if numeros_validos is False:
        print('Invalidos...')
        continue

    if operador not in operators:
        print('Coloque um operador válido')
        continue

    if len(operador) > 1:
        print('Coloque apenas um operador')
        continue

    if operador == '+':
        print(f'{numero_1}+{numero_2} =', num_1_float+num_2_float)
    elif operador == '-':
        print(f'{numero_1}-{numero_2} =', num_1_float-num_2_float)
    elif operador == '/':
        print(f'{numero_1}/{numero_2} =', num_1_float/num_2_float)
    elif operador == '*':
        print(f'{numero_1}*{numero_2} =', num_1_float*num_2_float)

    sair = input('Whants exit? [y]es: ').lower().startswith('y')

    if sair:
        break
