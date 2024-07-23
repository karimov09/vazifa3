
class MyListDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'{self.name} should be a list')
        instance.__dict__[self.name] = value