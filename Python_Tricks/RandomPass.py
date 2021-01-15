import random

import string

Nums = "0123456789"

Special = "!@#$%^&*:_-.;/"

Letters = string.punctuation

letter = string.ascii_letters

Let = string.ascii_uppercase

let = string.ascii_lowercase

letdig = string.digits

Symbol = Nums + Letters + Special + let + letter + Let + letdig

len = int(input("\nEnter the Length of your Password (Less than 150) :-\nAns:- "))

print("\n")

password = "".join(random.sample(Symbol, len))

print ("\nYour generated Password is (Between curly braces{}):- { " + password + " }\n\n")