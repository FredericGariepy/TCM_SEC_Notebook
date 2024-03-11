Python strings are immutable (cannot be changed after creation).

Therefore, in operations such as concatenation, python creates a new string in the background.

In python3 all strings are represented in Unicode

## String declaration `""` `''` `""" """`
__Single Line Strings__ with `''` `""` and `\` escape:

`str = "I'm a \"String\""`

`print(str)` >>> I'm a "String"

__Multi Line Strings__ with `""" """` :
```
`mltln_str = """
I'm a
multi-line
"string"
"""
```
>>>

I'm a

multi-line

"string"
___

#### escapes `\n` `\"` `\\` `\x41\`
| escape type | format | output |
|-|-|-|
| new line | `\n` | *Makes a new line* |
| quote | `\"` `\'` | " ' |
| backslash  | `\\` | \ |
| hex | `"\x41"` | A |

### String operations (methods)
#### declaration by multiplication
`str = "a"*4` >>> aaaa  | Note: _this `str` will be used as the example_
#### length `len()`
`len(str)` >>> 4
#### substrings `in`
`"a" in str` >>> True

`"b" in str` >>> False
#### Strig starts `str.startswith("char")`
`str.startswith("a")` >>> True

`str.startswith("A")` >>> False
#### String Index `str.index("a")`
`str.startswith("a")` >>> 0 | Note: _finds first occurrence_
#### Uppercase & lowercase
`str.upper()` >>> AAAA

`str.lower()` >>> aaaa
#### Strip `str.strip()`
Removes __leading__ _or_ __trailling__ space

`messy = "  password:x0188b    " 

`messy.strip()` >>> "password:x0188b"

#### Replace `str.replace("a","z")`
`str.replace("a","z")` >>> zzzz

#### Split String `str.split()`
`messy.strip().split()` >>> ['password:', 'x0188b']

`messy.strip().split(":")` >>> ['password', 'x0188b']

#### In python3 all strings are represented in Unicode.
`str.encode()` , `str.encode("utf-8")`

#### Adjust Strings `rjust` `ljust` _Used extensively in hacking_
Default: _Adds leading/trailling white spaces_

`str = 'aaaa'`, `len(str)` >>> 4

`str.rjust(25)`, `len(str)` >>> 25

Change delineator: `str.rjust(25,"X")` _Adds __leading__ X_

Change delineator: `str.ljust(25,"X")` _Adds __trailling__ X_

### format method `{}`
`"str is {} characters long".format(len(str))` >>> str is 4 characters long

`"9 + 9 = {}".format(0x12)` >>> 9 + 9 = 18

With multiple placeholders:

`"{} {} {}".format("\x41","B",'c'.upper())` >>> A B C

With index order:

`"{0} {2} {1}".format("\x41","B",'c'.upper())` >>> A C B

With variable name in placeholder:

`"{length}".format(length=len("aaa"))` >>> 3

### formated String litterals (prepend with `f`)
`secret = 42`

`f"secret is {secret}"` >> 'secret is 42'

Specified as a __float__:
`f"secret is {secret:2f}"` >> 'secret is 42.00'

Specified as a __octal__:
`f"secret is {secret:o}"` >> 'secret is 52.00'

Specified as a __hex__:
`f"secret is {secret:x}"` >> 'secret is 2a'

Specified as a __binary__:
`f"secret is {secret:b}"` >> 'secret is 101010'
