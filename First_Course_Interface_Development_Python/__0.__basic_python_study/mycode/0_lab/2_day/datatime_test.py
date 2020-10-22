from datetime import datetime as dt
dt.today().year

age = int(input('태어난 연도를 입력하세요'))
print(age)

age = dt.today().year - age + 1

if 17 <= age < 20:
    print('고등학생입니다.')

if 20 <= age < 27:
    print('대학생 입니다.')

else:
    print('학생이 아닙니다.')

