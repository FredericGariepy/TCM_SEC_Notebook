# Linux commands
## command line

`user@host:~$` 

user indicates the current user
host indicates the host machine

~ short hand for user's home directory 

$ logged in as normal user

\# logged in as administrator 

`$ whoami`
 user

`$ hostname`
> host

`pwd`
prints working directory

`cd sub-directory`
change directory to sub-directory

`cd ..`

## getting help

`man command`
shows information about command

press `q` to quit

`info command`
shows information about command (not as common)

`command --help` 
shows abreviated information about command

[explainshell.com](https://explainshell.com/)
help with more complex commands

## comand line arguments and options

You can combine multiple arguments availble to a command.
Some arguments require parameters.

**example**

`ls -I "File*"` lists all files that do not start with 'File'

`ls --ingnore="File*"` does the same thing

## looking at Text Files: more, less, cat

**more**
`more filename.txt`

shows contents of text file, can only go forward page by page.

**less**

`less filename.txt`

shows contents of text file, can only go forward page by page.

you can search for a string with `/string`, you can find the next occurance with `n`

**cat**

`cat file.extension`

Concatonate the file's content. 

`cat file1.txt file2.py`

Multiple files can be concatonated together:

`cat -b filename.txt`
adds a line index for all non-empty lines.

`cat -n filename.txt`
adds a line index for lines.

`cat` arguments and parameters are optional

to exit cat press `CTRL d`

`cat` can be used to redirect its output with `>`.

For example:

`cat file1.txt file2.txt > combined.txt`

cretes a new file that is the combined concatonation of file1 and file2

`cat > newfile.txt`

`hello`

`goodbye`

CTRL + d (escape cat given no parameters)
Creates a new file with 
```
hello
goodbye
```


---
