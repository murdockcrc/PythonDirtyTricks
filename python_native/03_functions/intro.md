# First-class objects

Functions are first class citizens in Python. They can be assigned to variables, passed as arguments, or returned from a function.

```
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
```