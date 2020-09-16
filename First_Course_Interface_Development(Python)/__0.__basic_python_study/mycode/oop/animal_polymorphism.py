# 다형성
# 부모 클래스 생성
# 자식 클래스가 상속 받음 = object 에 부모 클래스를 넣음

class Animal():
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'),
           Cat('Mr. Mistoffelees'),
           Dog('Lassie')]

# 순서
# 1. animals 리스트들이 animal 에 하나씩 대입
# 2. Cat 클래스의 object(Animal) 가 부모를 호출
# 3. 부모의 __init__ 으로 name 설정 및 출력
# 4. Cat 클래스 안에 있는 메소드 talk 를 return
for animal in animals:
    print(animal.name + ': ' + animal.talk())
