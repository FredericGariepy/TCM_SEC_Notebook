### Loop with while, `while`
```
a = 0
while not False:
   a += 1
```
### Loop with for,`for`
```
a = 0
for i in [1,2,3]
    a += i
```

#### Loop with for range, `for i in range(int)
```
for i in range(3):
    print(i)

```
#### hey, but this is O(n^2), double looping
```
for i in range(3):
    for j in range(3):
        print(i,j)
```
#### with a `continue` statement 
```
for i in range(5):
    if False:
        continue
    print("I will print")
```
#### with a `pass` statement`
```
for i in range(2):
    if False:
        pass
    print("I will print anyways...")
```
#### Looping over characters in a string
```
for c in "String"
    print(c)
```
__>>>__

S

t

r

i

n

g
#### looping over a dictionary with `.items()`
```
for key,val in dict.items():
    print(key, val)
```
