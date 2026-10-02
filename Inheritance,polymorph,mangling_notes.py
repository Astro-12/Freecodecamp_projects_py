'''
What is Inheritance:
  -Inheritance is a key concept of oop
  -with inheritance a child class can use the attributes and methods of a base or parent class.
  -allows you to reuse your code, create clear hierarchies, and customize behavior without rewriting everything.

How to implement inheritance:
'''
  class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return f'{self.name} makes a sound'

  class Dog(Animal):
      bark = 'woof! woof!! woof!!!'
  
  jack = Dog('Jack')
  print(jack.sound())  # Jack makes a sound
  print(jack.bark)  # woof! woof!! woof!!!

'''
The Inheritance can be of two types: 
  - single inheritance
  - Multiple inheritance
'''
'''
Following is the example of multiple inheritance:
'''
class Walker:
    def walk(self):
        return 'I can walk on land'

class Swimmer:
    def swim(self):
        return 'I can swim in water'

# Amphibian inherits from both Walker and Swimmer
class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I'm {self.name} the frog. {self.walk()} and {self.swim()}."

frog = Amphibian('Freddy')
print(frog.introduce())
# Output: I'm Freddy the frog. I can walk on land and I can swim in water.

'''
What is polymorphism:
  - Another key concept of oop
  - Polymorphism allows methods in different classes to share the same name but perform different tasks. You call the same method name on different objects, and each responds in its own way.
'''
  class Cat:
   def speak(self):
       return "A cat meow"

  class Bird:
     def speak(self):
         return "A bird tweet"
    
  class Monkey:
     def speak(self):
         return "A monkey ooh ooh aah aah ooh ooh aah aah"
  
  def animal_sound(animal):
     print(animal.speak())
  
  animal_sound(Cat())
  animal_sound(Bird())
  animal_sound(Monkey())
  #Output:
  #A cat meow
  #A bird tweet
  #A monkey ooh ooh aah aah ooh ooh aah aah
'''
  There is another kind of polymorphism called inheritance-based polymorphism:
    -In inheritance-based polymorphism, a parent class defines a method,
      and multiple child classes override that method in their own way. You can then call the same method on any child object, and it behaves differently depending on which child class it is.
'''
    class Animal:
   def speak(self):
       return 'Some generic sound'

    class Cat(Animal):
       def speak(self):
           return 'A cat meow'
    
    class Dog(Animal):
       def speak(self):
           return 'A dog barks woof woof'
    
    class Monkey(Animal):
       def speak(self):
           return 'A monkey ooh ooh aah aah ooh ooh aah aah'
      
    print(Cat().speak()) # A cat meow
    print(Dog().speak()) # A dog barks woof woof
    print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
    print(Animal().speak()) # Some generic sound

'''
Name Mangling:
  -The main purpose of name mangling is to prevent accidental attribute and method overriding when you use inheritance.
'''
    class Parent:
    def __init__(self):
        self.__data = 'Parent data'

    class Child(Parent):
        def __init__(self):
            super().__init__()
            self.__data = 'Child data'
    
    c = Child()
    print(c.__dict__) # {'_Parent__data': 'Parent data', '_Child__data': 'Child data'}
  '''
    -This prevented the child class to override the parent data("self.__data = 'Parent data'"."self.__data ='Child data'")
    -What if python mangling is not used:
  '''
  class Parent:
   def __init__(self):
       self.data = 'Parent data'

  class Child(Parent):
     def __init__(self):
         super().__init__()
         self.data = 'Child data'
  
  c = Child()
  print(c.__dict__)  # {'data': 'Child data'}
'''
