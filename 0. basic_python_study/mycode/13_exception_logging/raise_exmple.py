while True:
    value = input("변환할 정수값을 입력해주세요")

    # 10 입력시 2번 실행됌
    for digit in value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않으셨습니다")   # 형식에 맞지 않게 입력하면 강제 에러 raise
    print("정수값으로 변환된 숫자 -", int(value))
