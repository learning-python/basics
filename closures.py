# Accepts a password and a function
# Returns a function that acts like the given function
# at all times except when the password is given as
# an argument.
# If password is given, returns list of arguments ever
# given (except passwords).

def saveHistory(password, func):
    # Add code here

def addHello(string):
    return string + ' hello'

magicHello = saveHistory('chips', addHello)
print(magicHello('Jerry')) # 'Jerry hello'
print(magicHello('Elaine')) # 'Elaine hello'
print(magicHello('chips')) # ['Jerry', 'Elaine']
print(magicHello('George')) # 'George hello'
print(magicHello('chips')) # ['Jerry', 'Elaine', 'George']
print(magicHello('chips')) # ['Jerry', 'Elaine', 'George']
print(magicHello('Kramer')) # 'Kramer hello'
print(magicHello('chips')) # ['Jerry', 'Elaine', 'George', 'Kramer']
