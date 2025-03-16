



from abc import ABC ,abstractmethod




class Massa(ABC):
    @abstractmethod
    def __init__(self):
        self.constrate = constrate
        self.massa = massa

    @abstractmethod
    def Massa_ob(self,peso):...

    @abstractmethod
    def massa_em_Atração(self):...

    @abstractmethod
    def peso(self):...



class materia(Massa):

    def Massa_ob(self,peso) -> int:
        return self.peso * 10




lk = materia
lk.Massa_ob = 10
print(lk.Massa_ob)
print(type(lk))


#
#
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass
#
# class Dog(Animal):
#     def sound(self):
#         print("Woof")
#
# class Cat(Animal):
#     def sound(self):
#         print("Meow")
#
# dog = Dog()
# dog.sound()
#
# cat = Cat()
# cat.sound()


