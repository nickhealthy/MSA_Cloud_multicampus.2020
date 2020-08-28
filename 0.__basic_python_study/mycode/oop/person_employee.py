class Person():  # 부모 클래스 Person 선언
    def __init__(self, name, age, gender):
        # 속성값 지정, 해당 변수가 클래스의 attribute(속성) 임을 명확히하기 위해 self 를 붙임
        self.name = name
        self.age = age
        self.gender = gender

    # Method 선언
    def about_me(self):
        print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")

    # 내가 추가 해본것
    def __str__(self):
        return f"저의 이름은 : {self.name} 이구요, 제 나이는 : {self.age} 살 입니다."

# 부모 클래스 Person 으로부터 상속
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)  # 부모객체(인스턴스)를 사용
        self.salary = salary
        self.hire_date = hire_date  # 속성값 추가

    # 새로운 메서드 추가
    def do_work(self):
        print("열심히 일을 합니다.")

    # 부모 클래스 함수 재정의
    def about_me(self):
        super().about_me() # 부모 클래스 함수 사용
        print("제 급여는 ", self.salary, "원 이구요, 제 입사일은 ", self.hire_date, " 입니다.")

myPerson = Person("John", 34, "Male")
# print('dd', myPerson) = 내가 추가 해본것
myEmployee = Employee("Daeho", 34, "Male", 300000, "2012/03/01") # 아규먼트(인자) 순서에 맞게 기입하고 출력 해야함
# 부모 클래스꺼
myPerson.about_me()
# 상속 받은 자식 클래스
myEmployee.about_me()
