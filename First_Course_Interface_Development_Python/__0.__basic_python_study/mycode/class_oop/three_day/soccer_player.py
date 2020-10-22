# SoccerPlayer 클래스 선언
class SoccerPlayer(object):
    # 생성자 선언 - 객체가 생성될때 호출되는 메서드
    def __init__(self, name, position, back_number):
        # access modifier 가 public
        self.name = name
        self.position = position
        self.back_number = back_number

    # 일반함수 (JAVA = instance method), back_number 값을 입력받아서 변경하는 함수
    # 함수(생성자)의 첫번째 파라미터에 self가 있어야 클래스에 속한 함수가 됩니다.
    # 첫번째 파라미터의 이름은 self 가 아니여도 괜찮음
    def change_back_number(self, new_number):
        print(f'선수의 등번호를 변경합니다. From {self.back_number} to {new_number}')
        self.back_number = new_number

    # toString() 메서드와 동일한 역할
    # 객체의 주소가 아니라 객체가 가진 특정 인스턴스 변수 값을 출력
    def __str__(self):  # __str__ 의 부모는 (object)
        # print(dooly.__str__())
        return f'My Name is {self.name}, I play in {self.position} in center'

def main():                         # 실행시키는 함수
    # 객체생성
    dooly = SoccerPlayer('둘리', 'MF' , 10)
    # __str__ 호출한것
    print(dooly)
    # 위와 똑같은거임
    print(dooly.__str__())

    print()

    # __init__ 생성자 함수 호출
    print('현재 선수의 등번호는 {}'.format(dooly.back_number))
    dooly.change_back_number(5)
    print('변경된 선수의 등번호는 {}'.format(dooly.back_number))

main()