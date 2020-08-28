import pickle

# binary 파일을 만든다. (확장명은 지정해주지 않음)
# 값을 직접 입력해 파일을 binary 방식으로 만든다.

# 사용자로부터 문자열을 몇번 입력할지를 숫자로 입력 받는다.
number_of_data = int(input('Enter the number of data :'))
# 입력받은 데이터를 저장할 list 선언
data = []

# 입력받은 숫자 만큼 for loof으로 문자열을 입력을 받는다.
for idx in range(number_of_data):
    raw = input('Enter data ' + str(idx) + ':')
    # raw 로 받은 데이터들을 리스트에 차례로 저장
    data.append(raw)

# pickle를 dump() 함수를 이용해서 문자열을 저장한 list을 저장한다.
file = open('important', 'wb') # writting binary
pickle.dump(data, file)
file.close()
