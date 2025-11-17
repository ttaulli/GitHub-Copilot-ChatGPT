# Enable Next Edit Suggestions in VS Code
# Go to Settings
# macOS: Cmd + ,
# Windows/Linux: Ctrl + ,
# In the search bar, type:
# github.copilot.nextEditSuggestions.enabled
# Check the box ✔️ to enable it.


# Rename pizza to pizzaType.
# pizzaType = 'Pepperoni'
# print(pizza)





# Changing class/method/function names
# change class to 3DPoint

import math

class Point3D:
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y

    def get_distance(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)
    
# Refractoring
# Change greet to farewell

# Function with Default Parameters

def multiply(a: float, b: float = 1) -> float:
    return a * b

# Function with Optional Parameters; use farewell
def farewell(name: str, greeting: str = None) -> str:
    return f"{greeting or 'Hello'}, {name}!"

# Fibonacci function
def fib(n: int) -> int:
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

