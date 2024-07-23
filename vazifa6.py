class TypedAttribute:
    def init(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def get(self, instance, owner):
        if instance is None:
            return self
        return instance.dict.get(self.name)

    def set(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type} for attribute {self.name}, got {type(value)} instead.")
        instance.dict[self.name] = value


class User:
    username = TypedAttribute('username', str)
    first_name = TypedAttribute('first_name', str)
    last_name = TypedAttribute('last_name', str)
    age = TypedAttribute('age', int)
    groups = TypedAttribute('groups', list)
    status = TypedAttribute('status', bool)
    rating = TypedAttribute('rating', float)

    def init(self, username, first_name, last_name, age, groups, status, rating):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.groups = groups
        self.status = status
        self.rating = rating


user1 = User("john_doe", "John", "Doe", 30, ["admins", "users"], True, 4.5)
# Accessing attributes
print(user1.username) 
print(user1.age)       

try:
    user1.age = "thirty"
except TypeError as e:
    print(e) 

