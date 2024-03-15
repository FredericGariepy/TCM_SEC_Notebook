## Catching runtime errors 
Catch runtime errors durring normal execution.
Error examples: IndentationError
### raising exceptions, `raise Exception('custom code')`

### `try` `except` `finally`
```
try:
    f  = open("non_existant.txt")
except Exception as e:
    print(e)
finally:
    raise Exception('custom exception!')
    print("I will not be executed")
```
__>>>__
```
File "exceptions.py", line 6, in <module>
    raise Exception('custom exception!')
Exception: custom exception!
```
### assetions, program will stop executing on `assert()`
```
n = int(input("Enter number: "))
assert(n !=0)
print(1/n)
```
__>>>__
```
File "assertion.py", line 2, in <module>
    assert(n !=0)
AssertionError
```
