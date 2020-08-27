# Stack - FIFO(first in first out)

my_stack = [20, 10, 30, 40, 20]
print(my_stack)
my_stack.append(100) # 마지막 인덱스에 추가
print(my_stack)
my_stack.pop() # 마지막 인덱스 아웃
print(my_stack)

'''
# 예제 stack
word = input('input a word:')
word_list = list(word) # 문자 마다 리스트화
for i in range(len(word_list)): # 문자의 개수만큼 출력
    print(word_list)
'''

# Queu - LIFO(Last in first out)
my_stack.pop(0) # 인덱스로 pop 설정 가능
print('Queu', my_stack)
print("중복제거", set(my_stack))

my_stack.append(30)
my_tuple = tuple(my_stack)
print(type(my_tuple), my_tuple)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 50
print('')
print(my_tuple * 2)
print(len(my_tuple))

my_int = (1)
print(type(my_int), my_int)
my_tuple2 = (1,)
print(type(my_tuple2), my_tuple2)


print()
#Set
my_set = set([40, 20, 49, 50, 20, 50])
print(my_set)
my_set.add(49) # add 추가하지만 중복 값이라 set 허용 x
print(my_set)


print()
# remove 값 삭제(에러발생), discard 값 삭제(값이 없어도 에러 x)
my_set.remove(49) # remove 값 삭제
print(my_set)
# discard() 함수는 해당 값이 존재하지 않더라도 에러를 발생시키지 않는다.
my_set.discard(20) # discard 값 삭제
print('여기', my_set)
my_set.add(60)
my_set.add(30)
print(my_set)
my_set.discard(10)
print(my_set)

# my_set.remove(10) # 값 없음
# print(my_set)
# remove 없는 값을 입력했을때 에러를 강제로 발생시킴
# KeyError: 10

print('')
print('합집합')


s1 = set([1, 2, 3, 4, 5])
s2 = set([3, 4, 5, 6, 7])
# 합집합
print(s1.union(s2))
print(s1 | s2)

print('')
print('교집합')

# 교집합
print(s1.intersection(s2))
print(s1 & s2)

print('')
print('차집합')

# 차집합
print(s1.difference(s2))
print(s1 - s2)
print(s2 - s1)

print('')
print('dictionary')

# dict
# 중복된 값 허용 X
my_dict = {}
my_dict2 = dict()
print('둘다 동일', type(my_dict), type(my_dict2))

print()
# 값넣기
my_dict['java'] = '자바'
my_dict['python'] = '파이썬'
my_dict['java script'] = '자바스크립트'
print(my_dict)


print()
# 값 출력
print(my_dict['java'])
#print(my_dict['python1']) # 매칭되는 key 값이 없으면 keyError 발생

# get 함수는 매칭되는 key 값이 없으면 에러 발생시키지 않고 'NONE' 값 출력
print(my_dict.get('python1'))

value = my_dict.get('python1')
if value is None:
    print('하위', value)
else:
    print('해당 key가 존재하지 않습니다.')


# 해당 Key 삭제
del my_dict['python']
print(my_dict)

# in 구문을 사용해서 해당 key 있는지를 체크한다.
print('java' in my_dict)

print()
# keys(), values(), items()
print(my_dict.keys())      # Key 값만 호출
print(my_dict.values())    # values 값만 호출
print(my_dict.items())     # 둘다 호출

print()
# 매칭되는 Key가 없으면 추가해 준다. (Value 값이 달라도 Key 값이 동일한게 있으면 안들어감)
print(my_dict)
my_dict.setdefault('python', '파이썬')
my_dict.setdefault('java', '자바2')
print(my_dict)
