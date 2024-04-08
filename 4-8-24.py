'''

self keyword .. It's used inside class methods to refer to the instance of the class itself. 

When i define a class, methods within that class need to have 'self' as hteir first parameter.
This allows thosemethods to acces and manipulate the attributes and methods of the class instance.
'''

class myClass:
    def __init__(self, name):
        self.name = name

    
    def display_name(self):
        print(f"my name is {self.name}")

obj = myClass('Allice') ## Create the instance of the myClass
#obj.display_name()


''' 
Inheritaince.
where one class can inherit attributes and methods from another.
'''
class Animal:  ## (base or Parent)
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f"I am a {self.species}")

class Dog(Animal): ## (child class)
    def __init__(self,breed):
        super().__init__("Dog")
        self.breed = breed

    
    def display_breed(self):
        print(f"I am a {self.breed} dog")


#dog_obj = Dog("Labrador")
#dog_obj.display_species()  # Output: I am a Dog
#dog_obj.display_breed()  # Output: I am a Labrador dog




'''
Challenge: Create a basic program that mimics inheritance in OOP. 
Model a basic banking system using OOP concepts.

Account class:

Attributes: account_number, balance
Methods: deposit(amount), withdraw(amount), display_balance()
SavingsAccount class (inherits from Account):

Additional attribute: interest_rate
Additional method: add_interest()
'''

class Account:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        return f"You made a deposit of {amount}"

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            return f"You made a withdrawal of {amount}"
        else:
            return "Insufficient balance"

    def display_balance(self):
        return f"Account Balance is {self._balance} for Account Number {self._account_number}"

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def add_interest(self):
        self._balance += self._balance * self._interest_rate
        return f"Added {self._interest_rate * 100}% interest to the balance"

# Example usage
sav_account = SavingsAccount("SAV_5421", 200, 0.025)  # 2.5% interest rate
print(sav_account.deposit(400))
print(sav_account.display_balance())
print(sav_account.add_interest())
print(sav_account.display_balance())


'''
newAcc = Account('FY34', 100)
newAcc.display_balance()
newAcc.deposit(100)
newAcc.display_balance()

'''
