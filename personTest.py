class Person:
    def __init__(self, name, age, country_of_origin):
        self.name = name
        self.age = age
        self.country_of_origin = country_of_origin

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Country of Origin: {self.country_of_origin}'