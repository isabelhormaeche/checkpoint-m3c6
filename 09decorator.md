<div id="index"></div>

<sub>[<<8. What is a dunder method?](08dunder.md) | [<<Back to README index](README.md)</sub>

# 9. What is a python decorator?

Table of Contents:

* [9.1.  How to Create a Python Decorator](#91-how-to-create-a-python-decorator)
* [9.2. Example of decorator](#92-example-of-decorator)
* [9.3. Reusing Decorators](#93-reusing-decorators)
* [9.4. @property Decorator](#94-property-decorator)
* [9.5. @classmethod decorator( getter, setter methods)](#95-classmethod-decorator-getter-setter-methods)
* [9.6. References](#96-references)


A Python decorator is a function that takes another function as an argument (the function to be decorated) and extends or modifies the behavior of the latter without explicitly modifying its code. 

It allows you to wrap additional functionality around the existing function and returns a modified version of it.
<div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
    <img src="images/Primer-on-Python-Decorators_Watermarked.d0da542fa3fc.avif" width="500" height="300" alt="image of class and objects">
    <br<>
    <sub>Python Decorators. By Real Python</sub>
    </div>
    
<br>


Through decorators we will be able to reduce duplicate lines of code, we will make our code readable, easy to test, easy to maintain.
<br>


Common Use Cases for Decorators:

* Logging: You can use decorators to log function calls, input parameters, or execution time.
* Validation: Decorators help validate input parameters or enforce certain conditions before executing a function.
* Access Control: They allow you to control access permissions to specific functions.
* Caching: Decorators can cache function results to improve performance.
* Authentication: You can use decorators to authenticate users before invoking certain functions.

Decorators are a powerful tool in Python, allowing you to enhance and customize functions without cluttering their code.

<br>

# 9.1.  How to Create a Python Decorator
<sub>[Back to index](#index) | [9.2. Example of decorator>>](#92-example-of-decorator)</sub>
<br>


To create a decorator function in Python, You create an outer function that takes a function as an argument. There is also an inner function that wraps around the decorated function.

Here is the syntax for a basic Python decorator:

```Python
def my_decorator_func(func):

    def wrapper_func():
        # Do something before the function.
        func()
        # Do something after the function.
    return wrapper_func

```

To use a decorator ,you attach it to a function like you see in the code below. We use a decorator by placing the name of the decorator directly above the function we want to use it on. You prefix the decorator function with an @ symbol.
```Python
@my_decorator_func
def my_func():

    pass
```
<br>

# 9.2. Example of decorator
<sub>[<<9.1.  How to Create a Python Decorator](#91-how-to-create-a-python-decorator) | [Back to index](#index) | [9.3. Reusing Decorators>>](#93-reusing-decorators)</sub>
<br>

Here is an example where the `@log_datetime`decorator *log the date and time of a function* is executed:

```Python
    def log_datetime(func):
        '''Log the date and time of a function'''

        def wrapper():
            # Log the function name and execution time
            print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
            print(f'{"-"*30}')
            func()  # Call the original function

        return wrapper

#-------------------------------USING @log_datetime DECORATOR ( * )-------
    # we apply the decorator created above
    @log_datetime
    def daily_backup():

        print('Daily backup job has finished.')   

        
    daily_backup()
#-------------------------------------------------
    # Output

    Daily backup job has finished.
    Function: daily_backup
    Run on: 2021-06-06 06:54:14
    ---------------------------
```

Another way instead of using @log_datetime decorator ( * ), we´ll manually apply the Decorator:

```Python
# Define a function to be decorated
def daily_backup():
    print('Daily backup job has finished.')

# Apply the decorator to the function
daily_backup = log_datetime(daily_backup)    # <-------manually apply

# Call the decorated function
daily_backup()
```
As we can see the decorator approach ( @log_datetime decorator ) simplifies the code and promotes better readability.

Using the decorator allows you to achieve the same functionality with a more concise and elegant syntax .

Apart form that, once you define a decorator, you could apply it to multiple functions throughout your program without duplicating the same code (see next section [9.4. Reusing Decorators](#94-reusing-decorators) )

## Example explanation:

In the above example, the **`log_datetime` decorator** is used to enhance the behavior of the `daily_backup()` function. Let's break it down:

   - The `log_datetime` decorator is defined as follows:
     ```python
     def log_datetime(func):
         def wrapper():
             print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
             print(f'{"-"*30}')
             func()
         return wrapper
     ```
   - It takes a single argument, `func`, which is the function to be decorated.
   - Inside `log_datetime`, there's a nested function called `wrapper()`.
   - The `wrapper()` function:
     - Prints the function name and the current date and time.
     - Calls the original function (`func()`).
     - Returns the modified version of the original function.
   - Finally, the decorator returns the `wrapper` function.

<br>

**Applying the Decorator:**
   - The `@log_datetime` syntax is used to apply the decorator to the `daily_backup()` function:
     ```python
     @log_datetime
     def daily_backup():
         print('Daily backup job has finished.')
     ```
   - When you call `daily_backup()`, it actually executes the modified version provided by the `wrapper()` function within the `log_datetime` decorator.
   - As a result, you get the following output:
     ```Python
     Daily backup job has finished.
     Function: daily_backup
     Run on: 2021-06-06 06:54:14
     ---------------------------
     ```

<br>



In summary, the `log_datetime` decorator adds the functionality of logging the execution time and function name to the `daily_backup()` function without altering its original code.
  
<br>

# 9.3. Reusing Decorators
<sub>[<<9.2. Example of decorator](#92-example-of-decorator) | [Back to index](#index) | [9.4. @property Decorator>>](#94-property-decorator)</sub>
<br>


Remember that a decorator is just a regular Python function. All the usual tools for reusability are available. You can create a module where you store your decorators and that you can use in many other functions.

Decorators add behavior that can apply to many different functions.

Let´s see how we can reuse the *log_datetime decorator* (from section [9.2. Example of decorator](#92-example-of-decorator) ):

```Python
def log_datetime(func):
    '''Log the date and time of a function'''
    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper
```
```Python
@log_datetime
def daily_backup():
    print('Daily backup job has finished.')

@log_datetime
def data_processing():
    print('Data processing completed.')

# Call the decorated functions
daily_backup()
data_processing()
```
<br>

<br>



# 9.4. @property Decorator
<sub>[<<9.3. Reusing Decorators>>](#93-reusing-decorators) | [Back to index](#index) | [9.5. @classmethod decorator>>](#95-classmethod-decorator-getter-setter-methods)</sub>
<br>

This decorator allows you to create `getter` and `setter` methods for class attributes in an elegant way. Let´s see an example that uses the `@property` decorator in Python. 


```Python
class Invoice:

    def __init__(self, client, total):
        self._client = client
        self._total = total

    def formatter(self):
        return f'{self._client} owes: ${self._total}'

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self._total

google = Invoice('Google', 100)

print(google.client)

google.client = 'Yahoo'

print(google.client)
```

Explanation:

* Class Definition (Invoice):

    * The Invoice class has the following attributes and methods:
        * `_client` and `_total`: These are private attributes (indicated by the leading underscore _ ). They store the client name and the total amount.
        *  `formatter()`: A method that returns a formatted string indicating the client’s debt.
        * `@property` decorator:
            * client: A getter method for retrieving the value of _client.
            * total: A getter method for retrieving the value of _total.
            * `client.setter`: A setter method for updating the value of _client.

* Instance Creation (google):
    * An instance of the Invoice class is created with the client name 'Google' and a total amount of 100.

* Using the `@property` Decorator:
    * The @property decorator allows us to access the client attribute as if it were a regular attribute, even though it’s backed by the private _client attribute.
    * When we call `google.client`, it invokes the client getter method, which returns the value of _client (in this case, 'Google').
    * The `google.client = 'Yahoo'` line invokes the client setter method, which updates the value of _client to 'Yahoo'.
    Here’s the output of the provided code:
    <br>


```Python
#output
Google
Yahoo
```

In summary:

The @property decorator simplifies the process of creating getters and setters for class attributes.
It allows you to **access and modify private attributes** in a more intuitive way, **without directly exposing them**.


<br>

<br>

# 9.5. `@classmethod` decorator (getter, setter methods)
<sub>[<<9.4. Reusing Decorators](#94-property-decorator) | [Back to index](#index) | [9.6.References>>](#96-references)</sub>
<br>

We can also use a built-in function decorator as the `@classmethod decorator`. Let's illustrate with an example:

```python
     class MyClass:
         class_variable = 42

         @classmethod
         def print_class_variable(cls):
             print(f"Class variable value: {cls.class_variable}")

     # Usage
     MyClass.print_class_variable()  # Output: Class variable value: 42
```

```NOTE:
NOTE: **Class methods** and **decorators** serve different purposes in Python, but they both involve modifying the behavior of functions or methods.
```


Let's explore the distinctions:

* **Class Methods** ([already see at section: 1.8. Class methods](01class.md)): 

   - A **class method** is a special type of method that is bound to the class rather than an instance of the class.
   - It is defined using the `@classmethod` decorator.
   - Class methods take the class itself (usually named `cls`) as their first argument, allowing them to operate on class-level data.
   - They are often used for utility methods related to the class, such as creating instances or performing class-level operations.

* **Decorators**:
   - A **decorator** is a higher-order function that takes another function (or method) as an argument and returns a new function.
   - Decorators allow you to modify or extend the behavior of the wrapped function without changing its code directly.
   - Common use cases for decorators include logging, validation, access control, and caching.
   - You can apply decorators to both regular functions and class methods.

* **Key Differences**:
   - **Purpose**: Class methods are specific to classes and are used for class-level operations. Decorators can be applied to any callable (function or method).
   - **Arguments**: Class methods take the class itself (`cls`) as their first argument. Decorators can take any number of arguments.
   - **Syntax**: Class methods are defined using the `@classmethod` decorator. Decorators are applied using the `@decorator_name` syntax.

<br>

In summary, class methods are specific to classes and operate at the class level, while decorators are more general and can be applied to various functions or methods. Both are powerful tools for customizing behavior in Python.


<br>


# 9.6. References
<sub>[<<9.5. @classmethod decorator](#95-classmethod-decorator-getter-setter-methods) | [<<Back to index](#index)</sub>

<br>


* [Freecodecamp: Python Decorators – How to Create and Use Decorators in Python With Examples](https://www.freecodecamp.org/news/python-decorators-explained-with-examples/)

* [DevCamp:How to Work with Python Properties and Decorators](https://basque.devcamp.com/pt-full-stack-development-javascript-python-react/guide/how-to-work-python-properties)

* [Real Python: Python Decorators](https://realpython.com/primer-on-python-decorators/)


* [This Freecodecamp tutorial will walk you through *11 handy decorators*](https://www.freecodecamp.org/news/the-python-decorator-handbook/)

* [Plazi: Decoradores en Python: qué son y cómo funcionan](https://platzi.com/blog/decoradores-en-python-que-son-y-como-funcionan/)
* [*PythonDecoratorLibrary* is meant to be a central repository of decorator code pieces](https://wiki.python.org/moin/PythonDecoratorLibrary)

<br>

[<<Back to README index](README.md)

