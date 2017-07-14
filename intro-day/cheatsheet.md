## Python Cheatsheet

Basic syntax clues for the most common scenarios in Python

## Whitespace Matters !

Whitespace counts for more in Python than in many languages which use curly brackets to define blocks of code. Python uses indenting to decide which lines of code belong in a block and are associated with a condition, while, for loop, function body etc. 


## Comments

Comments start with a hash and affect the rest of the line

```python

# this is a cool piece of code !

```

## Strings

### Concatenation

## Numbers

## Booleans


## Variables

### Globals

Because variables are created when first mentioned, it can be difficult to decide (and hint to python) between a variable in a function scope or at the global scope.

```python 

name = 'jake'

def print_name():
    print(name)    # Not assigning so don't need 'global'

def change_name(new_name):
    global name    # hint we are now talking about global variable
    name = new_name

print_name()
change_name('finn')
print_name()  

```

## Console 

### Output

```python

print('hello, world')

```

or 

```python

print("hello, world")

```

### Input

Python 2

```python

answer = raw_input('tell me your name ?')

```

Python 3

```python

answer = input('tell me your name ?')

```

## Lists

## Conditions

### If


## Iteration

## Functions

### No arguments

```python

def say_something():
  print('hello')

```

### Arguments

```python

def say_something(message):
  print(message)

```

### Returning a Value

```python

def make_full_name(first_name, last_name):
  return first_name + " " + last_name
  
```

## Classes

### Definition

```python

class Dog():
 
 def __init__(self, name):
    self.name = name
    
 def sit(self):
    print(name + ' is sitting')
    return True

 def speak(self):
    print(name + ' says woof')
    
 def rate(self):
    print('13/10')
    
```

### Instantiation

```python

my_dog = Dog('Inca')
your_dog = Dog('Rover')

my_dog.sit()
your_dog.speak()

```

