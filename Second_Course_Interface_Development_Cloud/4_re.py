import re

p = re.compile("ca.e") 
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o)  | face (x)


def print_match(m):
    if m:
    # print(m.group())  # 매치되지 않으면 에러가 발생 / 매치가 되면 매칭되는 것을 출력
        print("m.group():", m.group())
        print("m.string:", m.string)
        print("m.start():", m.start())
        print("m.end():", m.end())
        print("m.span():", m.span())
    else:
        print("매칭되지 않음")


m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)