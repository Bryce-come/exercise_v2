class Animal(object):
    def eat(self):
        print("动物吃")


class Dog(Animal):
    def eat(self):
        print("小狗吃..")


class Cat(Animal):
    def eat(self):
        print("小猫吃..")


class Person(object):
    def eat(self):
        print("人吃五谷杂粮")


def fun(obj):
    obj.eat()

fun(Dog())
fun(Cat())
fun(Person())
fun(Animal())

