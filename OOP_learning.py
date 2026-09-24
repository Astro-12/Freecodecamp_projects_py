'''
Object-oriented programming:
  - A type of programming style in which developers treat everything as an real world objkect
  - OOP has 4 keys principles
      -encapsulation    -inheritance
      -polymorphism     -abstraction
  
    -ENCAPSULATION:
      -bundling of the attributes and methods of an object into a single unit, the class.
      -With encapsulation, you can hide the internal state of the object behind a simple set of public methods and attributes that act like doors. Behind those doors are private attributes and methods that control how the data changes and who can see it.
        For EX:
        -Let's say you want to track a wallet balance. You want to allow people to deposit or withdraw money from the wallet, but no one should be able to tamper with the balance directly.
        -In that case, you can make deposit() and withdraw() public methods, and you hide the balance under the _balance attribute:
'''
          class Wallet:
             def __init__(self, balance):
                 self._balance = balance # For internal use by convention
          
             def deposit(self, amount):
                 if amount > 0:
                     self._balance += amount # Add to the balance safely
          
             def withdraw(self, amount):
                 if 0 < amount <= self._balance:
                     self._balance -= amount # Remove from the balance safely
'''
        Note#1: prefixing attribute and methods with a single underscore means they are meant for internal use.
        Note#2: While a single underscore prefix is just a convention, prefixing attributes and methods with a double underscore effectively prevents them to be accessed from the outside of their class, making those attributes and methods private.
'''
        class Wallet:
         def __init__(self, balance):
             self.__balance = balance # Private attribute
      
         def deposit(self, amount):
             if amount > 0:
                 self.__balance += amount # Add to the balance safely
      
         def withdraw(self, amount):
             if 0 < amount <= self.__balance:
                 self.__balance -= amount # Remove from the balance safely
      
        account = Wallet(500)
        print(account.__balance) # AttributeError: 'Wallet' object has no attribute '__balance'
        #You can also define a private __validate method to check if every deposit or withdrawl amount is a positive number:
            def __validate(self, amount):
                   if amount < 0:
                       raise ValueError('Amount must be positive')
            
            def deposit(self, amount):
                   self.__validate(amount)
                   self.__balance += amount
            
            def withdraw(self, amount):
                   self.__validate(amount)
                   if amount > self.__balance:
                       raise ValueError('Insufficient funds')
                   self.__balance -= amount
            
            def get_balance(self):
                   return self.__balance
'''
    summary: Encapsulation locks down internal data behind clear public methods. That's how you keep your classes safe from tampering and centralize validation in one place.
            You can update or extend your code freely, knowing that outside code only touches the interfaces you expose.
'''
