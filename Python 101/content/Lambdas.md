## lambda functions, `lambda`
Single line anonymous functions
### single param
`add7 =  lambda x : x + 4` | add7(3,7) __>>>__ 10
### multi-param
`addxy =  lambda x, y : x + y` |  addxy(3,3) __>>>__ 6
### boolean returns
`isEven =  lambda x: x%2==0` | isEven(3) __>>>__ False
### list comprehension
###### single param
`to_ord = lambda x: [ord(i) for i in x]
###### multi-param
`blocks =  lambda x, y : [x[i:i+y] for i in range(0, len(x), y)]`

`blocks("string",3)` __>>>__ ['str', 'ing']
### express and evaluate lambda in one line
`print( (lambda x , y : x / y)(9, 4))` __>>>__ 2.25
