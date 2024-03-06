# Searching and Processing Text
## `grep`
`grep keyword file.txt` returns all lines with 'keyword'

`grep -v avoid file.txt` returns all lines with**out** 'avoid', (`-v` flag)

`grep keyword -B 1 -A 1 /var/etc/*.log` returns lines *before, mathcing, after*.

(`-B` before with number, `-A` after with number)

Note: check the `grep --help` for more options.

## `sort`
`sort file.txt` returns sorted file, use `-r` for reserve order. See man pages.

## `uniq` 
`uniq file.txt` returns unique words, **eliminates adjacent repeated lines**, so lines can repeat if *non-adjecent*

To get fully unique lines:

`sort file.txt | uniq` All adjecent lines will be neighboured and passed to uniq.

## `wc` (lines, characters, bytes)
`wc file.txt`

`-l` lines , `-m` characters, `-c` bytes.

example: `grep error /var/log/*.log | wc -l` Returns the number of lines with errors.

# Manipulating Text
## `sed` *process text as a stream*
***Note: use man pages or info. This is a very poowerfull command***
`sed 's/task/rabbit/' errors.log > rabbit.log` Substitutes (first instance of) 'task' with 'rabbit' in errors.log.

`echo red red | sed 's/red/blue/` **>>**  blue red

`echo red red | sed 's/red/blue/g` **>>**  blue blue  | `g` global substitution.

`sed 's/$/\n/g' file.txt` Replace all lines ends with new lines (Adds spacing)

`echo red red | sed '$s/red/blue/` **>>**  red blue  | `$` last match found.

`sed '/error/d` errors.log` The`d` delete match found in its output.

We can use multiple `sed` commands together in a single line:

`sed '/error/ s/log/bug/g' errors.log` Here, sed will find lines with error and substitute all 'log' with 'bug'.

OR 

`sed -e '/error/' -e 's/log/bug/g' errors.log' This will do the same but using `-e` as sepperators.

## `awk` *breaks input into field, collumns*
**The default delimiter of input is a space**

Use the `-F 'delimiter type'` to chose delimiter type.

***Note: use man pages or info. This is a very poowerfull command***

`echo I love you | awk '{print $2}'` **>>** love

`echo I love you | awk '{print $1, $2, "doritos"!}'` **>>** I love doritos!








