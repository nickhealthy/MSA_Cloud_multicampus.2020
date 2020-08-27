import random

# for ~ in 구문 사용
for val in [0, 1, 2]:
    print(type(val), val)

print('')

#range(start, end : 규칙) 함수
# start의 default 값은 0
# end 는 exclusive 항상 end -1
# 증가치의 default 값은 1
for val in range(0, 10):
    print(val)

print('')

for val in range(0, 10, 2):
    print(val)

print('')

for val in range(10, 1, -1): # 역순 출력
    print(val)

print('')

# 문자열 타입의 리스트
favor_hobby = ['fishing', 'reading', 'shopping']
for hobby in favor_hobby:
    print('{} is my favorite hobby'.format(hobby))

print('')

# dictionary(dict) 타입
wish_travel_city = {'bangkok' : 'THai', 'LA' : 'USA', 'bangkok2' : 'THai2'}
print(type(wish_travel_city))
print(wish_travel_city['LA']) # 키 입력시 값 출력

print('')

# key, value 를 출력할때 keys() 함수
for city in wish_travel_city.keys(): #키만 뽑아내라
    print('{} ds in {}'.format(city, wish_travel_city[city]))

print('')

# key, value 를 출력할때 items() 함수 사용
for city, country in wish_travel_city.items():
    print(f'{city} in {country}')

print('')

# random 모듈
for val in range(1, 11):
    ticket = random.randint(1, 100)
    print(f'index : {val} random value {ticket}')

print('')

# for 구문 대신 while
# for val in range(10):
    # print(val)

print('while', ('-'*5))
idx = 0
while idx < 10:
    print(idx)
    idx += 1

print('break-----------')

# break 문 사용
for i in range(10):
    if i == 5:
        break
    print(i)

print('EOP')

print('continue---------')

# continue 문 사용
for i in range(10):
    if i == 5:
        continue
    print(i)
else:
    print('EOP')

print('')
