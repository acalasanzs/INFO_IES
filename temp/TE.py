print("\n")
class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')
# create a new object of Person class
harry = Person()
print("\n")
# Output: <function Person.greet>
print(Person.greet)
print("\n")
# Output: <bound method Person.greet of <__main__.Person object>>
print(harry.greet)
print("\n")
# Calling object's greet() method
# Output: Hello
harry.greet()