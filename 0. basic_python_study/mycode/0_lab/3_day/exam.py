# Variable Exchange
a = 10
b = 20

# bad
tmp = a
a = b
b = tmp

a = 100
b = 200

# good
a, b = b, a
print(a, b)

# Sequence UnPacking
a, *rest = [1, 2, 3]
print(a, rest)

a, *middle, c = [1, 2, 3, 4]
print(a, middle, c)

# Judgement, T, F
# Bad
attr = True
if attr == True:
    pass

# Good
if attr:
    pass

attr = None
# Bad
if attr == None:
    pass

# Good
if attr is None:
    pass

print()
print()

# zip() 함수
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))

# print(a, b, c)
for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300)):
    print(type(val), val)

print()
print()

# index가 같은 값을 tuple로 묶어서 합을 계산해서 List에 저장
sum_list = [sum(val) for val in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))]
print(sum_list)

print()
print()

# Enumerate & Zip
a_list = ['a1', 'a2', 'a3']
b_list = ['b1', 'b2', 'b3']
for i, (a, b) in enumerate(zip(a_list, b_list)):
    print(i, a, b)