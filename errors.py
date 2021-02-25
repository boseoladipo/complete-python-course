# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Let’s say you have the following code:
"""

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    print('This method is a work-in-progress.')

"""
We’re working on a class and we’ve not yet got around to implementing the `add_car` method. Instead of printing something out, we can raise a `NotImplementedError`.
"""

class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    raise NotImplementedError("We can't add cars to the garage yet.")

# Garage().add_car('Fiesta')  # raises error, comment this line out to run the rest of the file.
 

"""
That way we can’t call the method and assume it works—it will now fail and crash our program. We’ll know that we’re doing something that won’t work (because it’s not implemented yet).

That’s how you `raise` an error: use the keyword and create a new error object from the class you want. All built-in errors (what we looked at in the last video) are available everywhere for you to use.

Let’s say we’re implementing the method and we want to only allow cars of type `Car`:
"""

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
    self.cars.append(car)

ford_garage = Garage()
fiesta = Car('Ford', 'Fiesta')

ford_garage.add_car(fiesta)  # All good
ford_garage.add_car('Fiesta')  # raises error


# %%
"""
Sometimes it can be useful to create and raise errors with names we define, as opposed to only using the built-in errors.

If we want to create a custom error, we can do so very easily by subclassing the `Exception` class:
"""

class MyCustomError(Exception):
    pass

"""
The `pass` keyword just means “nothing here”. It is required because Python expects there to be an indented block after a colon, so we must at least have _something_ so Python can see the indentation.

This `MyCustomError` class just inherits everything from `Exception`, which means it behaves just like any other error.
"""

raise MyCustomError('A message describing the error')

"""
You can of course also create custom errors that have more than just the base `Exception` functionality. For example if you wanted to include an error code in your errors, you could do this:
"""

class MyErrorWithCode(Exception):
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


## Docstrings
"""
Docstrings in Python are just strings that are commonly used to describe what a class or function does or when it should be used.

A docstring has this format:
"""

"""
Your docstring goes here.
"""

"""
It so happens that in Python the triple-quotation mark is a *multi-line string*. You can use it instead of a normal string anywhere, if you want multiple lines.

But back to docstrings! We can add a docstring to our exception to explain when it should be used:
"""

class MyErrorWithCode(Exception):
    """Exception raised when a specific error code is needed."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code

"""
Notice how here the multi-line string is in one line; and that’s OK. We could put it into multiple lines if we want to.
"""

class MyErrorWithCode(Exception):
    """Exception raised when a specific error code is needed."""
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


# %%
"""
One of Python’s core tenets is: “ask for forgiveness, not for permission”.

Now, I know how well this works with friends and family (hint: not so well), but it works fantastically in Python. Remember this piece of code?
"""

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    self.cars.append(car)

"""
We would use these classes in this way:
"""

ford_garage = Garage()
fiesta = Car('Ford', 'Fiesta')

ford_garage.add_car(fiesta)

"""
If we wanted to make sure that we’re only adding `Car` objects to the `Garage`, we could do this:
"""

car = Car('Ford', 'Focus')
if isinstance(car, Car):
  ford_garage.add_car(car)
else:
  print("Your car was not a Car!")

"""
This is a typical structure of calling a function (in this case, the `add_car()` method:

if can_call_function():
  call_function()
else:
  say_error_happened()

What we do there is ask for permission (the `can_call_function()` statement).

Python suggests that, in many cases, our code can be made more readable by asking for forgiveness instead. Doing this (not real Python code):

try to call_function()
if failed:
  say_error_happened

Circling back to raising exceptions, we could modify the `add_car()` method to do this:
"""

class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []

  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage, but you can only add `Car` objects.')
    self.cars.append(car)

"""
And then we could call it like so:
"""

car = Car('Ford', 'Focus')
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")

"""
There are two benefits:

1. Our code reads more nicely: we try to do something that we expect to be able to do, and if we cannot then we say an error happened;
2. Our check for whether it is something we can do is now encapsulated inside the `add_car()` method; we don’t need to have an if statement every time we want to add a car.

The syntax is the `try-catch` syntax.

We try to do whatever is inside the `try` block, and then if an error happens we jump to the `except` block. We only do so for errors that match the one in the block (in this case, `TypeError` would be caught, other errors would not be caught).

We can catch multiple errors (even though our method won’t raise them, just showing you the syntax here):
"""

car = Car('Ford', 'Focus')
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")
except ValueError:
  print("Something was wrong with your Car...")

"""
Over the next few sections we’ll be making use of this, which is why it’s really useful to know how to use `try` and `catch`.


`try` and `catch` also have a final counterpart: `finally`.

We can use `finally` to run a block of code no matter what happens: whether or not an exception is raised. For example:
"""

car = Car('Ford', 'Focus')
try:
  ford_garage.add_car(car)
except TypeError:
  print("Your car was not a Car!")
finally:
  print(f"Your garage has {len(ford_garage)} cars.")

