for i in range(0, 10):
    try:
        result = 10 // i
        print(i, "------", result)
    except ZeroDivisionError as dd:
        print("Not divided by 0")
    # 예외 발생 여부와 상관없이 실행
    finally:
        print("종료되었습니다.")
