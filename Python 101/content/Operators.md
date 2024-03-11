## Python Operators
Let's get the obvious ones out of the way:

`>`  `>=`  `<`  `<=`  `==` `+` `-` `*` 

`+=`  `-=` `/=`  `*=`
|operator | example | outcome |
| - | - | - |
| and | 1  and  True | True |
| & |0 & True | 0 |
| or | 1 or False | 1 |
| float division | 10/3 | 3.3333333333333335 |
| floor division | 10//3 | 3 |
| modulo | 123%10 | 3|
| power | 10 ** 4 | 10000 |
| power | 1**0 | 1 |
| pow() | pow(10,4) || 10000 |
| bitwise XOR | 3 ^ 4 | 7 |
| right bit shift| 7 >> 1 | 3 |
| >> | 111>>1 | 011|
| left bit shift | 3 << 1 | 6 |
| << | 11<<1 | 110 |

| A | B | A XOR B |
|---|---|---------|
| X | Y |  X ^ Y  |
| 0 | 0 |    0    |
| 0 | 1 |    1    |
| 1 | 0 |    1    |
| 1 | 1 |    0    |
| 3 | 4 |    7    |
|011|100|   111   |

| A | B | A & B |
|---|---|-------|
| X | Y | bin(X & Y)|
| 0 | 0 |   0   |
| 0 | 1 |   0   |
| 1 | 0 |   0   |
| 1 | 1 |   1   |
| 3 | 5 | 1 |
|011 | 101 | 001 |
