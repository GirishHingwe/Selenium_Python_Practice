class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

class Cat(Animal):
    def bark(self):
        print("meow")

dog =Dog()
cat = Cat()
dog.eat()
dog.bark()
cat.eat()
cat.bark()
