import calc # Import a file in the same folder

print('calc doc string: ', calc.__doc__)
print('test __name__: ', __name__)

# Functions declared in the file are properties of the imported file
added = calc.add(2, 3)
subtracted = calc.subtract(2, 3)
multiplied = calc.multiply(2, 3)
divided = calc.divide(2, 3)

# print function can take multiple arguments of different types
print('added', added)
print('subtracted', subtracted)
print('multiplied', multiplied)
print('divided', divided)

# data types
nothing = None # NoneType
print('None type', type(None))

yes_or_no = True # bool
print('yes_or_no type', type(yes_or_no))

greeting = 'hello' # str
print('greeting type', type(greeting))

six = 6 # int
print('six type', type(six))

seven = 7.0 # float
print('seven type', type(seven))

stuff = ['one', 2, { 'three': 3 }] # list
print('stuff type', type(stuff))

cant_change = ('one', 2, { 'three': 3 }) # tuple
print('cant_change type', type(cant_change))

look_up = { 'a_key': 'a_value', 'another_key': ['another', 'value'] }
print('look_up type', type(look_up))

def say_hi(name): # function
  print('Hello', name)
print(type(say_hi))
