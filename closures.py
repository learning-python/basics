# Accepts a password and a function
# Returns a function that acts like the given function
# at all times except when the password is given as
# an argument.
# If password is given, returns list of arguments ever
# given (except passwords).

def save_history(password, func):
    history = []
    def new_func(arg):
        if arg == password:
            return history
        history.append(arg)
        return func(arg)
    return new_func


def add_hello(string):
    return string + ' hello'

magic_hello = save_history('chips', add_hello)
print(magic_hello('Jerry')) # 'Jerry hello'
print(magic_hello('Elaine')) # 'Elaine hello'
print(magic_hello('chips')) # ['Jerry', 'Elaine']
print(magic_hello('George')) # 'George hello'
print(magic_hello('chips')) # ['Jerry', 'Elaine', 'George']
print(magic_hello('chips')) # ['Jerry', 'Elaine', 'George']
print(magic_hello('Kramer')) # 'Kramer hello'
print(magic_hello('chips')) # ['Jerry', 'Elaine', 'George', 'Kramer']
