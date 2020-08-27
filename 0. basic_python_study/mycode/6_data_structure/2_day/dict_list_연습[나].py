users = [{'id' : 1, 'name' : 'hong kildong', 'email' : 'hong@mail.com', 'hp_num' : '010-2343-9870'},\
         {'id' : 2, 'name' : 'dada', 'email' : 'alska@naver.com', 'hp_num' : '010-3135-0000'}]


for key in users:
    for value in key.keys():
        print(f'{value} = {key[value]}')

print()
print()

for item in users:
    for s, v in item.items():
        print('{} == {} '.format(s, v))