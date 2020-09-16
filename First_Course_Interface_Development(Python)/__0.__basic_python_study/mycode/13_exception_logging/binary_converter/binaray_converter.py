user_input = 999
while user_input != "0":
    user_input = input("십진수 숫자를 입력해주세요 : ")
    try:
        decimal_number = int(user_input)
        print(bin(decimal_number))
    # 위에서 정한 자료형에 맞지 않은 값을 입력시 에러 처리
    except ValueError as e:
        print(e)
        print("Error - 10진수 숫자만 입력해주시기 바랍니다.")
