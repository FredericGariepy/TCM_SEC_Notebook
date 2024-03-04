## Paths
### Absolute path
`/path/from/the/root/direcotory/target`

Contain the full path to a target. 

Operations (`ls` , `cp`, etc...) on the absolute path will regardless of current working direcotry. 

### Relative path

`./relative/path/target`

Target path is relative to the current working directory. `.` 

`../changed/relative/path/target`

Notice here that `..` stands for the current working directory's parent. 

And so, the operations on this path will apply to the relative path starting at the parent.

`..` can be chained togehter e.g.: `../../dir/target`

### touch 
`touch file.txt` is used to update the modfication time.

`touch new-file.txt` will create a new file if it does not exist.

### copy
`cp source destination`

coppies existing file to destination, use `-n` flag to avoid overwritting existing files.

### move
`mv source destination`

Moves a source file to its destination.

#### `mv` Can also be used to rename a file and directory

`mv file new-filename`

`mv dir new-dirname`
(works on non-empty dir too!)

### remove files
`rm target`

add `-i` flag to prompt before removal.

### make and remove directory

`mkdir directory-to-create` creates a new directory

`rmdir directory-to-delete` deletes target directory

#### remove non-empty directory
`rm -rf non-empty-directory-to-delete`

Use `rm` with the `-rf` flags to forecfully reccursively remove directory files 

### spaced-named files and directories

use litteral strings quotes `"with space"`

**OR**

escape the space with `\` e.g. `with\ space`

### File and Path expansion (a.k.a Globbing) `**` `*` `?`

**Enable Globbing**
`shopt -s globstar`

e.g. using listing

`ls file*.type`

Will return all .type files starting with "file" and 0 or + followign characters

`ls file?.type' 

Will return all files with 1 character following "file"

`ls **/*.type`

Search across current directory, multiple sub-directories

#### regex

`ls file[123].txt`

return .txt with either 1,2 or 3 

`ls file[1-3].txt`

return .txt in range 1 through 3

`ls file[a-zA-Z].txt`

return .txt with lower & upper characters.

### head & tail

`head text.txt`

view first 10 lines of file

`tail text.txt` 

view last 10 lines of file

add `-n` flag with a number to specifify line output

#### monitor end of files for changes with tail

`tail - f /var/log/auth.log`

this will monitor the tail of the auth.log file 

### `diff` differences in files

`diff file1.txt file2.txt`

prints all diffrences
**... no changes**
**< change from first file**
**> change from second file**

### symbolic Links (Hard, Soft)

`ln target link` (Hard link)

This is a **hard** link, refference to target location on storage.

Meaning it will persist if the taget is moved, changed or deleted.

`ln -s ./target link` (soft link)

This is a **soft** link, refference to file/directory on life system.

Meaning if target is *moved or deleted*, symbolic link will not work.

This more like a shortcut in windows as an example.

Soft links need absolute or relative paths.

#### Where are symbolic links used?

Nginx is uses symbolic links between directories in sites-available and sites-enabled


You can use a symboloc link for a Development Kit, so when a update occurs, 

the link is changed and the enviroment configurations can stay the same.

e.g. /opt/java 

jdk -> /opt/java/jdk-16

Soft symbolic links can also cross partions.

### Compressing and Archiving Files (zip, tar)
**make sure to name your zipped file as .zip**
#### `zip` files
`zip tmp/zipfile.zip file1 file2 file3` zip files together in tmp directory
#### `unzip` files
`unzip -l tmp/zipfile.zip` list zipfile content without decompressing

#### `zip` directories
`zip -r  tmp/zipfile.zip dir1 dir2`

`zip` with the `-r` flag to reccursively compress directory files

#### `tar` Archiving (does NOT compress files)

`-c` creates an archive 

`-f` sends archive to file

`-t` tests archive

`-v` increase verbosity 

E.g. `tar -cvf tarfile.tar file*.txt dir? requirements.txt`

Will create tarfile.tar to archive all files starting with "file", directory with wildcard and a requirement.txt file.

If you want to make a compressed archive:

`tar -cvfz zippedtar.tar.gz file*.txt`

Note: that you **must** add `.tar` and `.gz` manually

### `gzip` (compression)

`gzip tarfile.tar`
**>>** tarfile.tar.gz




