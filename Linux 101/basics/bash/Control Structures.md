### variables
`TEST_VAR="test"` call this variable using `$`: `$TEST_VAR`

`x=2` call it `echo x=["$x"]`
## Control Structures (if,elif,else)
Inside the expression evaluation [[ eval me! ]] make sure the variables have space before and after the closing inner brackets.
Remember to add a semicolon too.
```
#!/bin/bash

if [[ -d "./directory1" ]]; then
    echo "true"
else
    echo "false"
fi
```

### Numberical comparisons
Example: 
```
#!/bin/bash
x=1
y=2
if [[ "$x" -lt "$y" ]]; then
    echo "true"
fi
``` 
| comparator | flag |
| - | - |
| != | -ne |
| = | -eq |
| > | -gt |
| >= | -ge |
| < | -lt |
| <= | -le |

### String comparisons
Example:
```
#!/bin/bash
if [[ "A" < "B" ]]; then
    echo "true"
fi
```
| comparator | sign |
| - | - |
| = | == |
| != | != |
| < | < |
| > | > |

## Case
Case mathces essentialy use `grep`.

`./case.sh 1`: Arg between 0 and 4 inclusive

`./case.sh omg` : Arg missing or not in cases
```
#!/bin/bash

case $1 in
[0-4])
    message="Arg between 0 and 4 inclusive"
    ;;
[5-9])
    message="Arg between 5 and 9 inclusive"
    ;;
*)
    message="Arg missing or not in cases"
    ;;
esac
echo $message
```

## Loops
#### Definite loop (for)
Definite loops (for) != Indefinite loops (while)

Loop through hard coded values: 1 2 3 4 5
```
#!/bin/bash
for i in 1 2 3 4 5; do
    echo $i
done
```
Loop through generated sequence: {1...5}
```
#!/bin/bash
for i in {1..5}; do
    echo $i
done
```
Loop through with arithmetic (conventional format)
```
#!/bin/bash
for (( i=1; i<6; i++)); do
    echo $i
done
```
Loop through files example:
``
#!/bin/bash
for FILE in *.sh
do
    echo $FILE
    tail -n 1 $FILE
done
``
#### Indefinite loops (while)
```
#!/bin/bash
counter=5
while[[ $counter -gt 0 ]]; do
    echo $counter
    counter=$(($counter -1))
done
```
