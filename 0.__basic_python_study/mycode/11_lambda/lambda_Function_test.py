# 일반적인 함수 정의
def add(x, y):
    return x + y

print(add(10, 20))

print()
print()
# lambda 함수 정의 : 함수를 좀 더 간결하게 하기 위해서
# 파라미터랑 함수안에 바디 코드만 적는다. (대신 앞에 lambda 선언)
add2 = lambda x, y: x + y
print(add(100, 200))

# 제곱승, 곱하기, 나누기 람다함수로 정의해서 호출
square = lambda x: x * x
print('제곱승 람다: ', square(10))

division = lambda x, y: x / y
print('나누기 람다: ', int(division(10, 5)))

square2 = lambda x, y: x * y
print('곱하기 람다: ', square2(10, 20))

my_pow = lambda x: x ** 2
print(my_pow(5))
# 위와 똑같음
print((lambda x: x ** 2)(5))

print()
print()

# map() 함수 연습
my_arr = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, my_arr)
print(result)
print(list(result))

# 위의 코드와 동일함
result = list(map(lambda x: x * 2, my_arr))
print(result)

print()
print()

#   [1,2,3,4,5]
# + [1,2,3,4,5]
#      2,4,6,8,10
# add(1, 1) add(2,2) add(3,3)
f_add = lambda x, y: x + y
print(f_add(1, 1))
# 하나씩 하지말고 한번에
result = list(map(f_add, my_arr, my_arr))  # lambda 함수 선언 = f_add / my_arr 2번은 각각 인자(파라미터) x, y
print('다 묶어서 리스트화', result)

print()
print()
# my_arr 리스트의 값을 제곱승 해서 다른 리스트에 저장하세요
# lambda 함수와 map() 함수 사용합니다.
f_pow = lambda x: x ** 2
result = map(f_pow, my_arr) # f_pow 람다 함수의 인자 호출 / my_arr 리스트 하나씩 뿌림

# next 로 하나씩 뿌림
print(next(result))  # type map
print(next(result))
print(next(result))
print(next(result))
print(next(result))


print()
print()
# filter 함수 : 조건에 맞는 애들만 걸러내겠다.
result = filter(lambda x: x > 2, my_arr)
print(result) # 리스트로 변환 해줘야함 / 변환 안할시 인터러블 오브젝트 파일로 출력
print(list(result))

# 리스트 말고 for문으로 출력
for val in filter(lambda x: x > 2, my_arr):
    print(val)

print()
print()

# reduce()
# functools.py 라는 모듈안에 reduce() 함수가 존재
from functools import reduce
result = reduce(lambda x, y: x + y, my_arr)
print(result)
