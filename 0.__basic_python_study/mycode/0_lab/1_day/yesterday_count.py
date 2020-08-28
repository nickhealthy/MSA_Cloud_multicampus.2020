'''
yesterday.txt 파일을 읽어서
'YESTERDAY', 'yesterday', 'Yesterday'
단어가 몇번 나오는지 Counting 해보기
'''
#file open
#mode : r(read), w(write), a(append), rb, wb (binary file)
file = open('yesterday.txt', 'r')
#file의 내용을 읽은 값을 저장한 변수
yesterday_lyric = ''
while 1:
    line = file.readline() #한줄씩 읽어라
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + '\n'

print(yesterday_lyric)
#file 읽기 종료
file.close()

n_of_YESTERDAY = yesterday_lyric.upper().count('YESTERDAY') #yesterday가 9번, count안에 있는 'YESTERDAY'는 upper을 썻기떔에
print('Number of a word YESTERDAY = ', n_of_YESTERDAY)

n_of_YESTERDAY = yesterday_lyric.count('Yesterday')
print('Number of a word Yesterday = ', n_of_YESTERDAY)

n_of_YESTERDAY = yesterday_lyric.lower().count('yesterday')
print('Number of a word yesterday = ', n_of_YESTERDAY)

