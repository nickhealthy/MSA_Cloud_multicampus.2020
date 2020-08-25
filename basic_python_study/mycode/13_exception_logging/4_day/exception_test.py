# try ~ except ~ else
# try ~ except ~ finally

for i in range(10):
    try:
        result = 10 / i

    # 예외 처리는 계층 구조를 가짐 (Exception 이 최상위 계층)
    # 가독성 면에서 하위 계층를 골라 선택하면 좋음
    except ZeroDivisionError as err:
        print(err)
    # 에러가 발생하지 않았을때 여기
    else:
        print(result)
    # 에러가 발생하든 안하든 실행
    finally:
        print('종료되었음')