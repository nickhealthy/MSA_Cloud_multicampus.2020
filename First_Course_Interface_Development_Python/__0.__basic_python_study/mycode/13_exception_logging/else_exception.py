for i in range(10):
    try:
        result = 10 / i
    except ZeroDivisionError:
        print("Not divided by 0")
    # 예외가 발생하지 않았을떄 동작하는 코드
    else:
        print(10 / i)
