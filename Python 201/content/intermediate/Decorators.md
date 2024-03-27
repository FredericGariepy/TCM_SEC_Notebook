Decorators allow to modify or extend the behavior of functions/methods without changing their actual code.

Decorators are syntactic sugar `@`
```python 
# outer funtion, takes function as argument
def logger(func):
    def wrapper():
        print("-"*50)
        func()
        print("-"*50)
    return wrapper

@logger
def demo():
    print('executing')

demo()

# Equivalent

logger(demo())
```

Using a decorator with passed arguments.
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print('~'*50)
        func(*args, *kwargs)
        print('~'*50)
    return wrapper

@decorator
def decorated_func(*arg, **kwargs):
    print(*arg,**kwargs)

decorated_func(1,{'a':4,'c':3})
```
