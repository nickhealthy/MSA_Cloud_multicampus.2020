# join() 함수 : list -> str
# #unpacking
colors = ['red', 'yellow', 'green']
result = ' '.join(colors)
print(type(result), result)
result = '/'.join(colors)
print(result)

print(); print()

# split() 함수 : str -> list
# packing
langs = 'python, java, c#, sclar'
result = langs.split(',')
print(type(result), result)

# unpacking
a, b, c, d = langs.split(',')
print('unpacking 한 값들: ', a, b, c, d)

langs = 'python java c# sclar'
# 공백으로 구분하는 문자열인 경우에는
# split() 함수에서 구분자를 주지 않아도 된다.
result = langs.split()
print(result)

print(); print()

# 일반적인 for loop
my_list = []
for val in range(10):
    if val % 2 == 0:
        my_list.append(val)
print(my_list)

print(); print()

# List Comprehension (포괄적인 리스트)
my_list2 = [val for val in range(10)]
print(my_list2)

# 짝수만 리스트에 넣어서 출력해라
my_list3 = [val for val in range(10) if val % 2 == 0]
print(my_list3)

# 0으로 나누어 떨어지면 val 값을, 아니면 10 출력하라
my_list4 = [val if val % 2 == 0 else 10 for val in range(10)]
print(my_list4)

# 위 코드와 동일함
my_list5 = []
for val in range(10):
    if val % 2 == 0:
        my_list5.append(val)
    else:
        my_list5.append(10)
print(my_list5)

print(); print()
result = list()
# 2. 문자열 타입 List Comprehension
word1 = 'Hello'
word2 = 'World'
for i in word1:
    for j in word2:
        print(i+j)
        result.append(i+j)
print('어디냐', type(result), result)

print(); print()

my_list5 = [i+j for i in word1 for j in word2]
print('here', my_list5)

print(); print()

my_list = [i+j for i in word1 for j in word2 if i == j]
print('맞는 값만 출력: ', my_list, len(my_list))

print(); print()

# 위 코드와 동일
my_list10 = []
for i in word1:
    for j in word2:
        if i == j:
            my_list10.append(i+j)
print('합친다', my_list10)

print(); print()

# List Comprehensions 2차원 배열
# list 화 시킴
words = 'Yesterday love was such an easy game to play'.split()
print(words)

# 1. 일반적인 예
# 2차원 배열을 만들 빈 공간
words_lists = []
for w in words:
    word_list = [w.upper(), w.lower(), len(w)]  # 이건 list 여러개
    print('리스트 여러개: ', word_list)
    words_lists.append(word_list)  # 여러개의(대문자, 소문자, 길이) list를 2차원 배열로 만듬
print(words_lists)

# 2. Pythonic Code
stuff = [[w.upper(), w.lower(), len(w)] for w in words]  # 앞에 안에 쓴 '[]' 는 리스트화
print(stuff)

print()
print()

# indexed traversal
langs_lists = 'python java c# sclar'.split()
print(langs_lists)

print()

# Bad
for idx in range(len(langs_lists)):
    print(f'bad idx = {idx}, value = {langs_lists[idx]}')

print()

# Good - enumerate() 함수 : 인덱스와 값을 뿌려줌
for idx, lang in enumerate(langs_lists):   # items 와 거의 유사
    print(f' good idx={idx}, value={lang}')

# object 로 출력 / for, list 로 변환해서 사용해야함
print(enumerate(langs_lists))
print(list(enumerate(langs_lists)))

print()
print()

# Dict Comprehension
my_dict = {idx: val.capitalize() for idx, val in enumerate('Yesterday love was such an easy game to play'.split())}
print(my_dict)

# 위의 코드와 동일
my_dict1 = {}
# practice = 'Yesterday love was such an easy game to play'.split() # 리스트화 안시키면 enumerate 오브젝트형태로 출력
for idx, val in enumerate('Yesterday love was such an easy game to play'.split()):
    my_dict1[idx] = val.capitalize()
print(my_dict1)
