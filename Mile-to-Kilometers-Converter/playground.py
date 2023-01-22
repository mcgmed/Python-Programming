def add(*args):
    print(type(args))
    print(f'THe tuple is: {args}')
    print(f'First argument is: {args[0]}')


add(5, 7, 9)  # prints a tuple


def add(*args):
    result = 0
    for x in args:
        result += x
    print(result)


add(5, 7, 9)


def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add=3, multiply=5)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']  # When it's empty, it throws an error.
        self.model = kwargs.get('model')  # It returns None when it's empty.


my_car = Car(make='Nissan', model='GT-R')
print(my_car.make)
print(my_car.model)

my_car = Car(make='Nissan')  # 'model is empty.
print(my_car.make)
print(my_car.model)
