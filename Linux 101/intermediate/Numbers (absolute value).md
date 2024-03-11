#### There is no buil-in method for absoulte value in Bash.
##### So, rely on these scripts:
######  if conditional
```
#!/bin/bash
number=$1
if [ $number -lt 0 ]; then
    number=$((number * -1))
fi
```
######  ternary operator
```
#!/bin/bash
number=$1
abs_number=$((number < 0 ? -number : number))
```
