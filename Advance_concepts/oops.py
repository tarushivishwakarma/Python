#multi-level inheritance
# class Parent1:
#     def res(self):
#         print("First class")

#single-level inheritance
# class Parent(Parent1):
#     def show(self):
#         print("Parent class")
# class Child(Parent):
#     def display(self):
#         print("Child class")

# c=Child()
# c.display()
# c.show()
# c.res()

#heirarichal inheritance
# class Animal:
#     def sounds(self):
#         print("Make sounds")
# class Cat(Animal):
#     def cat_sound(self):
#         print("MEOWMEOW.....")
# class Snake(Animal):
#     def snake_sound(self):
#         print("SSSSSSSSSSSSSSSS")

# s=Snake()
# s.snake_sound()
# s.sounds()

# k=Cat()
# k.cat_sound()
# k.sounds()

class Demo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        result=self.a+self.b
        print(result)
d=Demo(10,20)
d.display()