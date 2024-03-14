# Reading and writing files
## Opening files, `open(filename.txt)`
`f =  open('hello.txt')`

`print(f)`

__>>>__

<_io.TextIOWrapper name='hello.txt' mode='r' encoding='UTF-8'>

As we can see from the stdout the default mode is `r` for read, and encoding is `UTF-8`.
### File information `f.name` `f.closed` `f.mode`
`f.name` Returns the file that is open

`f.closed` Returns boolean True if closed, False if Open.

`f.mode` returns `r`:read `w`:write  `a`:append
### Read whole file, `.read()`
`print(f.read())` to read the entire open file as string.
### Read file lines, `.readlines()`
`print(f.readlines())` to read file lines as strings. Stdout will be array of Strings.
### Re-reading files, `.seek(0)`
`print(f.readlines())` __>>>__ ['string1','string2','...']

`print(f.readlines())` __>>>__ []

Empty Array is returned on second exec of .readlines (or any read) because the reading head reached the end of the openned file.

Reset the read head (file position) with `.seek(line number)`
`f.seek(7)` 

`print(f.readlines())` __>>>__ ['string2','...']

`f.seek(0)` 

`print(f.readlines())` __>>>__ ['string1','string2','...']

Note: _The seek int value specifies a character postion, not a line position_
### Itterate over lines with for loop.
```
f = open('passwords.txt')
for line in f:
    print(line.strip())
```
### Write file, `.write()` 
```
f = open('newfile.txt', 'w')
f.write('new line')
f.close()
```


