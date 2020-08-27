print("구구단 몇단을 계산할까요?")
user_input = input()
print("구구단 " +user_input +"단을 계산합니다")
int_input = int(user_input)
for i in range(1, 10):
    result = int_input  * i
    print (user_input, "X", i, "=", result)


# 구구단 1 ~ 9단
for i in range(1, 10):
    print()
    print('{} 단 입니다'.format(i))
    print()
    for k in range(1, 10, 1):
        print('{} X {}'.format(i, k))



