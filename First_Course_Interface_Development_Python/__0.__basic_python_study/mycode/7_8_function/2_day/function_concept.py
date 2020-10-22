# 평균을 계산하는 함수를 정의
def my_average(numbers):
    # local variable
    total = 0
    for num in numbers:
        total += num
    my_avg = total / len(numbers)
    return my_avg

def connect(server, port):
    return 'http://{}:{}'.format(server, port)

# default parameter 로 정의한 함수
def times(n1 = 10, n2 = 20):
    return n2 - n1

# *p - tuple type parameter, 아규먼트의 갯수가 가변적
def var_param(*p):
    return p

#**p - dict type parameter
def var_param_dict(**p):
    print(type(p), p)
    for k, v in p.items(): # items() 키값과 밸류값 각자 뿌려줌
        print(k, v)

def tuple_dict_param(n1, n2, *n3, **n4):
    print(n1, n2, '튜플:', sum(n3))
    print('딕셔너리', n4)

# 다중값을 리턴하는 함수
def swap(a, b):
    return b, a

def main():                     # 권장 방식

    '''
    def my_average(numbers):
        # local variable
        total = 0
        for num in numbers:
            total += num
        my_avg = total / len(numbers)
        return my_avg
    '''

    prices = [1000, 3000, 2500, 450]
    result = my_average(prices) # 호출했지만 반환은 안함
    print('my_average', type(result), result)
    # 함수 외부에서는 local 변수를 사용할 수 없음
    # print(total)

    print()
    '''
    def connect(server, port):
        return 'http://{}:{}'.format(server, port)
    '''
    # 위치 파라미터
    result1 = connect('server.com', '9080')
    print(result1)
    # 키워드 파라미터
    result1 = connect(port='8087', server='aa.com')
    print(result1)

    print()
    '''
    # default parameter 로 정의한 함수
    def times(n1=10, n2=20):
        return n2 - n1
    '''
    result2 = times()
    print(result2)
    result2 = times(5)
    print(result2)

    result2 = times(19, 30) # n1, n2
    print(result2)

    '''
    # *p - tuple type parameter, 아규먼트의 갯수가 가변적
    def var_param(*p):
        return p
    '''
    print()
    result3 = var_param(1,)
    print(type(result3), result3)
    result3 = var_param(1, 2, 3)
    print(type(result3), result3)

    print()
    '''
    #**p - dict type parameter
    def var_param_dict(**p):
    print(type(p), p)
    for k, v in p.items(): # items() 키값과 밸류값 각자 뿌려줌
        print(k, v)
    '''
    var_param_dict(n1=10, n2=20, n3=30)

    print('')
    '''
    def tuple_dict_param(n1, n2, *n3, **n4):
    print(n1, n2, '튜플:', sum(n3))
    print('딕셔너리', n4)
    '''
    tuple_dict_param(10, 20, 100, 200, 300, a=10, b=20)

    print('')
    print('')

    '''
    def swap(a, b):
        return b, a
    '''

    result4 = swap(200, 100)
    print(type(result4), result4)
    x, y = swap(450, 230)
    print(f'x는 {x}, y는 {y}')

main() # 권장 방식
