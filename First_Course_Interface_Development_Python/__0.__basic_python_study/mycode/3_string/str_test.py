#문자열 처리
'''
greet = 'Hello' * 4 + '\n'
print(greet)

# print("I like 'Apple' ")

my_int = 100
flag = True
print(type(my_int), type(flag))
result = str(my_int) + str(flag)
print(type(result), type(result))

#문자열 인덱스
greeting = 'HELLO WORLD!'
print(greeting[1])
print(greeting[11])
print(greeting[0:12])

'''
# 문자열 슬라이싱
greeting = 'HELLO WORLD!'
print(greeting[4:9])

# greeting = 'HELLO WORLD!'
# print(greeting[2:5])
# print(greeting[5:])
# print(greeting[:5])
#
# print(len(greeting))

print()
print()

#str의 여러가지 함수 사용하기
word = 'GOOD manufacturing practice'
print(word.upper())
print(type(word.split(' ')), word.split(' '))

print()
print()

# str -> list : packing
my_wordList = word.split() #split은 구분 기호를 정해줄 수 있음
print(my_wordList)

# list() 클래스는 하나씩 인덱스를 나눔
word_list = list(word)
print('list() 함수', word_list)

# list -> str : unpacking
# unpacking 은 개수를 맞춰줘야함
str1, str2, str3 = my_wordList
print(str1)
print(str2)
print(str3)

# 첫단어 앞글자만 대문자
print(word.title())

# 단어마다 첫글자 대문자
print(word.capitalize())

print()
print()

# 문자열 위치 정렬
word2 = 'Hello'
print(word2.strip())
print(word2.rstrip())
print(word2.lstrip())

print()
print()

#naming
print('Product {name:10s}, Price per unit {price:10.3f}'\
      .format(name = "Apple", price = 5.243))