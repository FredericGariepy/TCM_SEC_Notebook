## Variables & data types
Store data in case-sensitive name locations.
| type | format (example)|
|-|-|
|int | `x = 1` |
| float | `flt = 3.12` |
| complex | `cplx =  4.14j` | 
|string| `s = "s"` |
| list | `lst = [1,"1"]` |
| tuple | `tpl = (1,"1")` |
| dictionary |  `dict = {"key":"val", 1:0}` |
| boolean | `bool = True` |
| range | `rng = range(5)` |
| bytes | `bt = b"foo"` |
#### find var type
`type(var1)`
#### multiple assignments
`var1, var2 = 'x',1`
### casting
Casting. only applies to appropriate castable tyles.
| cast type | format (example)|
|-|-|
|To Int |`x = int("1")` |
|To Float | `f = float("4.2")` |
|To String | `s = str(55)` |
|To Boolean | `b = bool(0)` |
### Numbers (number system) (int, float, complex)

**int**: `int1 = 1`

**float**: `float1 = 1.0`

**float**: `complex1 = 1.01j`

#### Diffrent number systems can be used, and used _together_
`hex10 = 0xa` | <class 'int'> Therefore, `print(1+0xa)` >>> __11__

`oct8 = 0o10` | <class 'int'> Therefore, `print(1 + 0o10)` >>> __9__ 

### absolute `abs()`
e.g. `abs(-4)` >>> __4__ | `abs(-3.01j)` >>> __3.01__
### rounding `round()`
e.g. `round(8.89)` >>> __8__ | `round(8.85,1)` >>> __8.8__ | `round(8.86,1)` >>> __8.9__
### binary representation `bin()`
e.g. `bin(7)` >>> __0b111__ | Note: Cannot interpret complex and float.
### hexadecimal representation `hex()`
e.g. `hex(79)` >>> __0x4f__ | Note: Cannot interpret complex and float.
