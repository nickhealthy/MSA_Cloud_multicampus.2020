# while answer is not 0
while 1:
    print('구구단 몇 단을 계산할까요 (1~9)?')
    answer = int(input())
    print('구구단 {}단을 계산합니다'.format(answer))

    if ((0 == answer) | (answer < 9)):
        break
    for count in range(10):
        print('{} X {}'.format(answer, count))
