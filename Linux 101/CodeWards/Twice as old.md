### Problem statement:
#### DESCRIPTION:
Your function takes two arguments:

1. current father's age (years)
2. current age of his son (years)
   
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
___
### Solution
This is a linear equation, and we need to solve for _x_: 

_($1-x/$2-x) = 2_

...

x = ( 2 * $2 ) - $1

return |x|

```
#!/bin/bash
dad_years_old=$1
son_years_old=$2
years=$(( ( $2 * 2 ) - $1 )) # solving linear equation
echo $((years < 0 ? -years : years)) # echo Absolute value
```
