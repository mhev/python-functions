class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0

    def make_deposit(self, amount):
        self.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com") # putting the user guido into the User class
monty = User("Monty Python", "monty@python.com") # putting the user Python into the User class

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100) # setting the User 'guido' account_balance = to account_balance plus 100
guido.make_deposit(200)
monty.make_deposit(50)

print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50