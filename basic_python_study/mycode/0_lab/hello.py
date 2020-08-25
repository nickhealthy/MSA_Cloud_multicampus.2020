my_list = [5, 1, 6, 7, 1, 11, 1, 1, 'cat']

print(type(my_list))

my_list2 = my_list

print(my_list2)

print(id(my_list), id(my_list2))
print(list('cat'))

print('1의 개수는 : ', my_list.count('cat'))
print('첫번째 5의 위치는 : ', my_list.index(5))

print(); print(); print()

hi = 'hello every one'
print(hi.split())
print(len(hi))
hi = hi.split()
print(len(hi), type(hi))

print(); print(); print()
stack = ['hello', 5, 1, 4, '날씨가', '좋아연']
stack.append('하위')
print(stack)
stack.pop()
print(stack)