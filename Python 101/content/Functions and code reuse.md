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


