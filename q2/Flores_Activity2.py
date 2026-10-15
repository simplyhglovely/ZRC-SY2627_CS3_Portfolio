class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def eat(self):
        print(self.name, "is eating.")

    def sleep(self):
        print(self.name, "is sleeping.")


class Dog(Animal):
    pass


dog1 = Dog("Bruno")
dog1.eat()

dog1.set_name("Max")
print(dog1.get_name())
dog1.sleep()

dog2 = Dog("Buddy")
dog2.eat()