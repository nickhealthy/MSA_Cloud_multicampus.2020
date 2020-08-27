# guess_number

import random

print('guess_Number---------')

guessNumber = random.randint(1, 100)
print(guessNumber)

answer = int(input())
count = 0

# 입력받은 숫자와 정답 숫자 값이 같지 않은 동안 loop
while answer is not guessNumber:
    count += 1
    print(guessNumber)

    num = int(input('숫자 입력'))

    if num > guessNumber:
        print('숫자가 너무 커요')
        print("다시 입력")
        num

    elif num < guessNumber:
        print('숫자가 너무 작아')
        print("다시 입력")
        num

    else:
        print('정답입니다.', count, '번만에 맞춤')
        break