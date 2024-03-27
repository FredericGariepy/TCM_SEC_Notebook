### A generator is a function that returns an iterator
Generators are used in memory-intensive exec. They are lazy executors.

It produces a sequence of values iterated over which we can `yeild`.
We can use the `next()` function to capture the value returned by a `yeild`.
```python
def generator():
    n =1
    yield n
    n +=1
    yield n
    n +=1
    yield n
test = generator()
print(test) #<generator object generator at 0x0000016B7F8E1850>
print(next(test)) #1
print(next(test)) #2
print(next(test)) #3
```
###  `StopIteration` Exeception is raised when generator iterations is done yeilding.
This Exception is automatically handled within a loop.
```python
def generator():
    n =2
    yield n
    n +=2
    yield n
    n +=2
    yield n
loop_test = generator()
for y in loop_test: # loop "knows" `StopIteration` Exeception is raised
    print(y) 
```

##### Using a for loop on a `yield` that is inside a for loop
```python 
def xor_static_key(a):
    key =0x5 #5
    for i in a:
        yield chr(ord(i)^ key) # return char of int ^ key
for i in xor_static_key('test'):
    print(i)
```

#### Anonymous generators (z for x in y)
```python
xor_static_key = (chr(ord(i) ^ 0x5) for i in "word")

print(xor_static_key) # <generator object <genexpr> at 0x000002561A9E17E0>

print(next(xor_static_key))
print(next(xor_static_key))
print(next(xor_static_key))
print(next(xor_static_key))

# Equivalent

for i in xor_static_key:
    print(i)
```





