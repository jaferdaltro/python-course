# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

name = 'Francisco'
heigh = 1.8
weigh = 90
imc = weigh / (heigh ** 2)

"f-strings"
my_string = f'o {name} tem o peso de {weigh} e a altura {heigh:.2f}e o {imc:.2f} de imc'
print(my_string)

option = input('What you want? ')
if option == "go":
    print("go to bed!")
elif option == 'stay':
    print("You've got to be kidding!!")
    
