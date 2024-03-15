## functions `def funct():`
Reusable block of code, exec when called.
```
def no_args_fun():
    print('simple')
```
#### `return`
```
def no_args_return():
    return "simple"

stored_return = no_args_return()

print(stored_return)
```
#### parameters
```
def one_param(s):
    print("\t{}".format(s))

def multi_params(a,b):
    print(f"{str(a)} : {str(b)}")

# multi_params(4,'a')     >>> '4 : a'
# multi_params(b=4,a='a') >>> 'a : 4'
```
#### default parameters
```
def defaulted(s1="default")
    print(s1)

# defaulted(s1) >>> 'default'
# defaulted('new') >>> 'new'
```
#### arbitrary parameters `*`
```
def arbitrary(s1="default", *more):
    print("{}{}".format(str(s1), " ".join([str(s) for s in more])))

# arbitrary() >>> 'default'
# arbitrary('new') >>> 'new'
# arbitrary('new','brand',667) >>> 'new brand 667'

```
#### Dictionary of args `**`
```
def dict_func(**ks):
    # print(type(ks)) >>> <class 'dict'>
    for a in ks:
        print(a, ks[a])
dict_func(a=1,b=2,c=3)
```

### global vs local variables with, `global`
Variables __global__ can be accessed by functions.

variables __local__ can only be accessed in function scope.

```
v = 100
def fun():
    v += 1
print(v) 
```
__>>>__

`UnboundLocalError: local variable 'v' referenced before assignment`

__Use `global`__ to reffer global variables while in funciton scope
```
v = 100
def fun():
    global v
    v += 1
print(v)
```
__>>>__

`101`

#### function invocations
```
def fun1():
    print(1)

def fun2():
    fun1()
    print(2)

fun2()
```
### reccusion
Make sure to include exit condition/terminations in reccursive functions.

__Else:__ RecursionError: maximum recursion depth exceeded while calling a Python object

Majority of recursive functions can be writen as while loops.

Mission-critical systems tend to avoid recursive functions, unless high benefits.
```
def recursion(x):
    if x < 11:
        print(x)
        recursion(x + 1)
recursion(1)
```
