A closure is a function that retains access to variables from the outer (enclosing) scope even after the outer function has finished executing.

Closures are usefull when a function needs to ref a val in the outer scope.

Only works in nested fucntions, nested funciton __must__ be returned inside the parent function.
```python
def outter(a):
    print('outer {}'.format(a))

    def inner():
        print('inner {}'.format(a))
    return inner

outter('test') #outer test

result = outter('test') # remebers value in enclosing scope 
del outter
result()
#outer test
#inner test
```
