names = ['jin', 'sungchul', 'ronaldo', 'hong', 'seo']
positions = ['mf', 'df', 'cf', 'wf', 'gk']
numbers = [10, 15, 20, 3, 1]

# 2차원 리스트를 사용하여 저장
'''
players = [[name, position.upper(), number] for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])
'''
#play_lists = []
# zip 함수
for na, po, nu in zip(names, positions, numbers):
    print(na, po, nu)

print()
print()
# list comprehension
players = [[na, po, nu] for na, po, nu in zip(names, positions, numbers)]
print('na, po, nu 리스트 출력: ', players)   # 리스트 출력
# hong = players[3]
# print(hong) # players 리스트의 index 3번째 값 출력
# numbers = hong[2]
# print(numbers)
# hong[2] = 25
# print(hong)


print()
print()
# SoccerPlayer 클래스를 import
# from 은 import 하기위해 경로를 정해줌
from mypython.python_programming_stu.mycode.class_oop.three_day.soccer_player import SoccerPlayer

# 객체 생성
player1 = SoccerPlayer('플레이어1', 'MF', 10)
print('요기얌', player1)
player1.change_back_number(20)

players_object = [SoccerPlayer(na, po, nu) for na, po, nu in zip(names, positions, numbers)]
# 인덱스를 정해줘서 뿌려줘야함
print(players_object[0])

# # son = players_object[3]
# # print(son)
# # numbers = son[2]
# # print(numbers)
# # print(son)
