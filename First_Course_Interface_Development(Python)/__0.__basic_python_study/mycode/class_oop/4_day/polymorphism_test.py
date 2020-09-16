# abstract method(추상)를 가진 부모 클래스 선언
class Animal(object):
    def __init__(self, name):
        self.name = name

    # abstract method
    def talk(self):
        raise NotImplementedError('자식클래스에서 반드시 구현해야 함')

# 자식 클래스
# body에 아무것도 구현 안해도 오류는 안남
class Cat(Animal):         # 첫번째 클래스
    def talk(self):
        return 'Meow'
class Dog(Animal):
    def talk(self):           # 첫번째 메서드
        return 'Woof'
    def pet(self):            # 두번째 메서드
        return 'I,m Pet'


my_ani = Animal('동물')
print(my_ani.name)

# 이건 안됌
# my_ani.talk()

print()
print()

animals = [Cat('고양이'), Dog('강아지1'), Dog('강아지2')]        # 클래스('값')
for ani in animals:
    print(ani.talk())
    #print(ani.pet())