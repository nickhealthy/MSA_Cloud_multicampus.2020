# 부모 클래스 Person 선언
class Person(object):
    # 생성자 = 속성
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print(f'Person의 이름은 {self.name} , 나이는 {self.age} 세 입니다')

# 자식 클래스
class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def about_me(self):
        super().about_me()
        print(f'급여는 {self.salary}, 입사일자는 {self.hire_date}')


# 새로운 변수에 클래스 이름과 각 인자에 맞게 값을 넣어줌
myPerson = Person('길동', 30, '남')
# 메서드 호출
myPerson.about_me()

# 상속 받은 자식 클래스, name, age, gender 은 부모 클래스에 생성자 변수를 생성해줌 / salary, hire_date 는 자식 생성자에 만듬
myEmployee = Employee('둘리', 10, '남', 300000, '2020/02/10')
# 부모에 있는 super(메서드 about_me()) 출력하고, 자식 메서드를 출력
myEmployee.about_me()