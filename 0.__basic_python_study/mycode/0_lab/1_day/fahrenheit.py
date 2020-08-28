# print('본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.')
# print('변환하고 싶은 섭씨 온도를 입력해 주세요:')
#
# go = float(input())
# temp1 = float(((9/5) * go) + 32)
#
# print('섭씨 온도: ', go)
# print('화씨 온도: ', temp1)

'''
섭씨를 입력 받아서 화씨로 변환하기
소수점 이하 둘째자리로 출력하기
'''

a = float(input('변환하고 싶은 섭씨 온도를 입력하세요! \n'))
temp = float(((9/5) * a) + 32)

print("섭씨온도 :", a)
print("화씨온도", temp)

print('화씨온도는 : {0:>10.3f}'.format(temp))
print('화씨온도는 : {key:.2f}'.format(key=temp))
print(f"화씨온도는 : {temp}")
print('화씨온도는 %.4f' % temp)

