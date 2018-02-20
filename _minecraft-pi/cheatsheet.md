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

```python

# create and assign
greeting = 'hello world'

# or 
greeting = "hello world"

```

### Concatenation

```python

full_path = folder + "\" + file_name

```

## Numbers

```python

house_number = 25
weight = 17.9

```

## Booleans

```python

True 

False

```

## Lists

```python

words = [ 'the', 'quick', 'brown', 'fox' ]
first = words[0]
last = words[-1]

```

### Iteration

```python

for word in words:
    print(word)
    
```

### Append

```python

words = []

words.append('the')
words.append('cat')
words.append('sat')

```

### Comparsions

```

==
!=
>
<
>=
<=

```

## Conditions

### If

If <condition> must be followed by a colon. Code belonging to the if must be indented below it. You will get an error if the indent is too big or too small or inconsistent. 

```python

if name == 'bob':
    print('hi bob!')
    
```

```python

if 'fox' in words:
    print('found a fox')

```

Else and Else If conditions are allowed but not Else If is *elif*. Multiple conditions can be joined together in an if using *and* & *or* keywords.


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

## Iteration

### While

```python

# forever...
while True:
    print('everything is awesome')
    
```

Break and Continue are available and work as expected.

### For

```python

# numbers 0..100
for number in range(101):
    print(str(number))
    
```


```python

# numbers 1..100
for number in range(1, 101):
    print(str(number))
    
```

```python

# numbers 3,4,5,6,7
for number in range(3, 8):
    print(str(number))
    
```

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

### Scope and Globals

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

