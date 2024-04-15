"""
EXERCISE
Cree una clase de Python llamada Usuario que use el método init y 
cree un nombre de usuario y una contraseña. 
Crea un objeto usando la clase.

"""

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def show(self):
        print("Username is", self.username, "and Password is", self.password)

# Creating an object of the class
obj = Usuario("Isabel", "mypassword")


# Accessing object properties
print(obj.username)  # Print the username
print(obj.password)  # Print the password

# Call the show method to show the username and password
obj.show()

#Output:
# Isabel
# mypassword
# Username is Isabel and Password is mypassword

