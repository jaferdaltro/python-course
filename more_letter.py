# phrase = 'In the beggining we have only darkness ' \
#     'and the spirit of God whas beneath of waters '\
#     'and God said was light'

phrase = 'hhhjjjj kkkkk'

i = 0
more_time_char = ''
qte_more_time_char = 0

while i < len(phrase):
    actual_char = phrase[i]

    if actual_char == " ":
        i += 1
        continue

    qte_more_time_char_actual = phrase.count(actual_char)

    if qte_more_time_char_actual > qte_more_time_char:
        qte_more_time_char = qte_more_time_char_actual
        more_time_char = actual_char
    i += 1


print(
    f'The more time chat is "{more_time_char}" and happen {qte_more_time_char} times')
