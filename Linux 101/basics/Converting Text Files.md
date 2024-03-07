# Converting Text Files
Diffrent Operating systems use diffrent **line terminator characters**.

- Windows (Dos) : /r (controll) /n (line feed)
- Mac OS : /r (controll)
- Unix : /n (line feed)

Example:
dos.txt  macos.txt  unix.txt

`file *.txt` Tells us the line termination information:
> dos.txt:    ASCII text, with CRLF line terminator
> 
> macos.txt:  ASCII text, with CR line terminator
> 
> unix.txt:   ASCII text

## `unix2dos` `dos2unix`
**`Sudo apt install` If not avaialble.**

`tr` `awk` `sed` can also be used, but `unix2dos` is much easier.

`unix2dos unix.txt` changes the unix file into a dos file.

`unix2dos -n unix.txt newdosfile.txt` Using `-n` creates a new file as dos file.

`unix2dos -c mac unix.txt` changes the unix file into a mac file.

`dos2unix dos.txt` changes the dos file into a unix file.

`dos2unix -c mac .txmact` changes the mac file into a unix file.
