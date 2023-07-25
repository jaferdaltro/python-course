secret_word = input("Digite uma palavra secreta: ")
right_chars = ''

count = 0
while True:
    pointer = input("Digite uma letra para a palavra secreta: ")
    count += 1

    if len(pointer) > 1:
        print("Só uma letra por favor!")
        continue

    if pointer in secret_word:
        right_chars += pointer

    building_word = ''
    for secret_char in secret_word:
        if secret_char in right_chars:
            building_word += secret_char
        else:
            building_word += '*'

    if building_word == secret_word:
        print(building_word)
        print(f'PARABÉNS VOCÊ ACERTOU A PALAVRA COM {count} TENTATIVAS!')
        break
    else:
        print(building_word)
