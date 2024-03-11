Note: _Reminder $1 is the first passed arg to the script_
## loop | `for` 
```
#!/bin/bash
n=$1
for (( i=0; i < $1 ; i++ )); do
    (( n += i ))
done
echo $n
```
## loop | brace expansion using sequence `seq` 
```
#!/bin/bash
n=$1
for i in $(seq 0 $(($1 - 1)) ); do
    (( n += i ))
done
echo $n
```
- `for i in $(seq 0 $(($1 - 1)) )` This iterates over the sequence of numbers from 0 to $1 - 1.
-  `seq` command generates the sequence of numbers between 1 and n.
- `$(())` is used to evaluate arithmetic operations/expressions within double parentheses.
___
#### Side Note: Best solution for _Sum UP to N_:
```
#!/bin/bash
n=$1
echo $(( (1 + n) * n / 2))
```
