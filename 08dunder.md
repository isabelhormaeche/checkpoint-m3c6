<sub>[<<7. What is polymorphism?](07poliformismo.md) | [<<Back to README index](README.md) | [9. What is a python decorator?>>](09decorator.md)</sub>

# 8. What is a dunder method?

In this section we will see the following dunder methods :`__init__()`, the `__str__()` and `__repr__( )`, `__iter__()` and `__next__()`.


This is just a tiny sample of all the special methods that Python has. For the complete [list of Special methods](https://docs.python.org/3/reference/datamodel.html#specialnames), refer to the special method section on the data model page of Python’s official documentation.


In Python, special methods are also called magic methods, or dunder methods. The convention is to use double leading and trailing underscores in the name, so it looks like \__method__( ).


Python implicitly calls special methods to execute certain operations in your code. They are  given to you from the Python language directly. They are called automatically by the Python interpreter in response to certain operations. 


```Note
Note:
They are called automatically by the Python interpreter in response to certain operations. 

You should NOT overwrite it or change it in any way.
```

Dunder methods are special functions that allow you to define specific behaviors for classes.


<div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <img src="images/Python-Magic-Methods_Watermarked.a69c3876000a.avif" width="500" height="300" alt="image of class and objects">
    <br<>
    <sub>Magic methods or Dunder methods. By Real Python.com</sub>
</div>

<br>

Along with \__init__( ), the \__str__( ) and \__repr__( ) methods are arguably the most commonly used special methods in custom classes.

*  the \__init__ method is used to initialize objects and is automatically invoked when an instance of the class is created. [Click here for more info about the *\__init__ method*.](02init.md)

* \__str__( ) and \__repr__( ) methods provide string representations for objects. The \__str__ method can give us some pretty output for the values and the details with our class. And with the \__repr__ method we can see  the raw data of an instance of the class.
    
<br>

Let´s see an example of a class named *Invoice* using the three dunder methods mentioned above.


```Python
class Invoice:
  def __init__(self, client, total):
    self.client = client
    self.total = total

  def __str__(self):
    return f"Invoice from {self.client} for {self.total}"

  # def __repr__(self):
  #   return f"Invoice({self.client}, {self.total})"

  def __repr__(self):
    return f"Invoice <value: client:{self.client}, total: {self.total}>"   #Invoice(Google, 500)

inv = Invoice('Google', 500)

# Call __str__ method
print(str(inv)) #Invoice from Google for 500

# Call __repr__ method
print(repr(inv))#Invoice <value: client: Google, total: 500>
```

Let´s explain the *methods* implemented in the example:

`__init__` (Initializer / Constructor):
The \__init__ method is called when an instance of the Invoice class is created.
It initializes instance variables (self.client and self.total) with the provided values.
In this case, it sets the client name and the total amount for the invoice.

`__str__` (String Representation):
The __str__ method defines how the object should be represented as a string when using the str() function or printing the object.
It returns a human-readable string that describes the invoice.
In this example, it provides a formatted string with the client name and total amount. (*#Invoice from Google for 500*)

`__repr__` (Object Representation):
The\__repr__ method defines how the object should be represented as a string when using the repr() function or debugging.
It returns a string that ideally allows you to recreate the object. Similar to dunder str but not as pretty.
In this case, it provides a more detailed representation, including the class name and attribute values.(*#Invoice <value: client: Google, total: 500>*)

Some further explanation:

* When you create an instance of Invoice with `inv = Invoice('Google', 500)`, the \__init__ method initializes the instance variables.
* Calling `str(inv)` invokes the \__str__ method, which provides a user-friendly description of the invoice.(*#Invoice from Google for 500*)
* Calling `repr(inv)` invokes the \__repr__ method, which gives a more detailed representation for debugging purposes.

<br>

```Note:
NOTE: Remember that the \__repr__ method is typically used for debugging and should ideally provide information to recreate the object. The \__str__ method, on the other hand, is meant for human-readable output.
```

<br>

# Uses of \__str__ and \__repr__methods:

A common task that you will perform in your Python code is to *display data* or *produce output*. Let´s see when to use: \__str__ or \__repr__ method: 



* `__str__` Method:
  * Use this method when you want the output to be nice and easy to read.
  * It´s ideal to provide user-friendly output. 
  * Helpful for displaying essential information to end users.
  
  <br>

* `__repr__` Method:
  * Employ this method when you want to see the raw data of an instance of the class.
  * To provide developer-friendly output. Useful for sharing information with other programmers using your code.
  * Great for logs and identifying bugs in a program. It is often used for debugging and understanding the internal state of an object. It shows the details inside the class. 
  

<br>

### Example of a *Real Use Case* of \__str__: 

 Imagine you are working with an API. You receive data and encapsulate it within a class. By using the \__str__ method, you can easily inspect the data and identify any issues or discrepancies. It’s a valuable tool for troubleshooting and ensuring the correct functioning of your program.
<br>
<br>
# Creating a custom iterable object with \__iter__ and \__next__dunder methods
[How to Build a Custom Iterator Class in Python by DevCamp](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-build-custom-iterator-class-python)
<br>

By creating our own custom iterable what we're going to be able to do is to have complete control over the behavior of how we loop through this collection.

```Python
class Lineup:

    def __init__(self, players):
        self.players = players
        self.last_player_index = (len(self.players) - 1)

    def __iter__(self):
        self.n = 0
        return self

    def get_player(self, n):
        return self.players[n]

    def __next__(self):
        if self.n < self.last_player_index:
            player = self.get_player(self.n)
            self.n += 1
            return player
        elif self.n == self.last_player_index:
            player = self.get_player(self.n)
            self.n = 0
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
print(next(process))
....
```

<br>

# Example Explanation

** Class Definition (Lineup)**  ⚾:

* The Lineup class is designed to represent a lineup of players.

* It has the following attributes and methods:

  * players: An attribute that stores a list of player names.
  * last_player_index: An attribute calculated as the length of the players list minus 1.
  * `__iter__()`: A special method that initializes the iterator (used for iteration).
  * get_player(n): A method that retrieves the player name at a given index n.
  * `__next__()`: Another special method that defines the behavior when iterating over the Lineup object.

* Instance Creation (astros_lineup):

  * An instance of the Lineup class is created with the list of Astros players: ['Springer', 'Bregman', 'Altuve', ...].
  * The last_player_index is set to the length of the player list minus 1 (in this case, 8).

* Iterator Behavior:

  * When we create an iterator using iter(astros_lineup), it calls the \__iter__() method.
  * The \__iter__() method initializes the index *n* to 0 and returns self (the Lineup object) as the iterator.

* Iteration using next():

Each time we call next(process), it invokes the \__next__() method.
The \__next__() method checks if the current index *n* is less than the last player index. <br>

If true, it retrieves the player at index n, increments n, and returns the player name.<br>

If *n* reaches the last player index, it wraps around to 0 and returns the last player name again.<br>

Here’s the output of the above code:

```Python
Springer
Bregman
Altuve
Correa
Reddick
Gonzalez
McCann
Davis
Tucker
Springer
Bregman
Altuve
Correa
Reddick
Gonzalez
McCann
```
In summary, the Lineup class allows you to iterate through the list of players, cycling back to the beginning when reaching the end. It’s a simple example of creating a custom iterable object in Python.

<br>

# References

* [DevCamp: Overview of Dunder Methods in Python: \__init__](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/overview-dunder-methods-python-__init__)

* [Every dunder method in Python](https://www.pythonmorsels.com/every-dunder-method/)

* [Representing Objects as Strings](https://realpython.com/python-magic-methods/)

* [How to Build a Custom Iterator Class in Python by DevCamp](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-build-custom-iterator-class-python)

<br>

[<<Back to README index](README.md)