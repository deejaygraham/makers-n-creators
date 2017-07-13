## Python Cheatsheet

## Comments

Comments start with a hash and affect the rest of the line

```python

# this is a cool piece of code !

```

## Variables

### Scope


### Globals


## Strings

### Concatenation

## Numbers

## Booleans


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

class Horse():
 
 def __init__(self):
    # initialization code goes here
    self.colour = 'black'
    
 def canter(self):
    self.run(slowly)
    return True

 def speak(self, message):
    print(message + ", neigh")
    
```

### Instantiation

```python

my_lovely_horse = Horse()

```

