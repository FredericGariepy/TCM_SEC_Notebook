## Usage information (arguments)
`$0` : is the name of the program itself (exec. script). Stored in arg 0.

`$#` : Number of arguments in command line.

`$@` :  All command line args are stored in `$@` store as **seperate** strings.
```
for arg in $@; do
    echo $arg
done
```
`$*` : All command line args as **single** string.

Use `${}` to access arg with 2 or more digits.

Example:
```
if [ "${10}" != "" ]; then
    echo $10   # This will echho 1
    echo ${10} # This will echho 10
fi
```

#### command substitution ` `` ` `$()`
commands enclosed in backticks or $() are executed first.

## `#` convertions
16#F will convert hexadecimal F to decimal 15.

8#52 will convert octal 52 to decimal 42.

1#1001 will convert binary 1001 to decimal 9.
```
#1/bin/bash
hexa=$((16#F))
echo $hexa #This will stdout 15
octa=$((8#52))
echo $octa #This will stdout 42
binary=$((2#1001)) 
echo $binar y#This will stdout 9
```


