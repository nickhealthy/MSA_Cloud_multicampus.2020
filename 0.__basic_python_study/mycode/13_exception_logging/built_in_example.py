string_ex = "123abc"

for value in string_ex:
    # 예외 발생 가능 코드
    try:
        print(int(value))

    # 예외 발생시 에러 발생 코드
    except NameError as err:
        print(err)


'''
invalid literal for int() with base 10: 'a'
invalid literal for int() with base 10: 'b'
invalid literal for int() with base 10: 'c'
'''