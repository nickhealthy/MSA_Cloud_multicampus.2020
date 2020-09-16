# mode를 설정하지 않으면 default가 r(read)

# myfile = open('i_have_a_dream.txt', 'r')
# contents = myfile.read()
# print(contents)
# myfile.close()

# with 구문 사용
# with open('i_have_a_dream.txt') as my_file:
#     contentes = my_file.read()
#     word_list = contentes.split(' ')
#     line_list = contentes.split('\n')
#
# print('Total Number of character: ', len(contentes))
# print('Total Number of words', len(word_list))
# print('Total Number of lines', len(line_list))

# readline() 함수 사용
with open('i_have_a_dream.txt') as my_file:
    # line number
    i = 0
    while True:
        line = my_file.readline()
        if line.strip() != '':
            print(str(i) + " === " + line.strip())
        if not line:
            break
        i += 1