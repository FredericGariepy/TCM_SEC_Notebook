### Shells (This doc will use Bash)

`bash` is the most common Shell on linux.

`ksh` is another shell. It acts just like Bash.

`csh` is another shell. `tcsh` upgraded version of `csh`.

`zsh` is the default shell in Kali Linux.

### Environment Variables

Basically varibales like in programing. Shells have variables too.

`printenv` to show enviroment variables. They are all in UPPERCASE.

**PATH** is the list of directories searched *in order* for the commands to be executed.

Note: If you eddit the path to inclde the current workign directory, 
Attackers can put custom commands (custom `ls` for example) inside directory, and when you execute the command, the custom attacker commnad will be executed first. 

### Global Variables (Global: Environment Variables) 
Global Variables: can be accessed by anything executing in the shell script

### Local Variables (Local: Shell Variables)

Local Variables: no access by script executing in *sub-shell*

#### Global and Local variable examples:
`COUNT_LOCAL=42` creates a local varriable. **Notice `$` was not used !!**

`echo $COUNT_LOCAL` echoes '42', add $ to tell Shell that COUNT_LOCAL is a variable

`bash` creates a sub-shell

`echo $COUNT_LOCAL` Does nothing.

`exit` exit sub-shell

`export COUNT_GLOBAL=69` using `export` Creates a global variable. **Notice `$` was not used !!**

`printen` You will see COUNT_GLOBAL=69 in the list of global variables.

`bash` creates a sub-shell

`echo $COUNT_GLOBAL` shows 69, since the varible is global

`exit` exit sub-shell

`unset COUNT_GLOBAL` Use `unset` to unset a variable. **Notice `$` was not used !!**

## Startup Files (interactive non-login shell)
When starting a new bash shell, the shell is configured using startup  files.

At /home/user `ls -al`, `.bashrc` The interactive non-login shell.

`nano .bashrc` open the shell file. The file has shell configs.

`alias` is like a shortcut. Let's make our own!

**Making our own alias called 'del'**

`alias del='rm -rfi'` 

`del` will now execute `rm` with `rfi` flags, meaning it is reccursive forced and interactive (prompts for delete).

Here's another alias where `c` will clear the screeen:

`alias c='clear'

To run our new aliases, we need to open a new shell so that the starup file takes effect.

## Redirecting Input and Output `>` `>>` `<` `2>`
**Standard In, Out, Error**

### `>` redirect standard out.

Example: `ls /etc/ > etc-content.txt`

`ls / > etc-content.txt` This will over-write the 'etc-content.txt' file

`>>` appends the standard out.

`head /etc/passwd >> etc-content.txt` This will append the passwd file content to the etc-content.txt file.

### `<`  standard in.

Most commands that take a file name, also accept inuput from standard in.

`head < /etc/passwd` and `head /etc/passwd` *have the same ouput.*

**However!** in the first case, the whole 'passwd' file is fed to the head command, and in the second the head command *opens* the file to read the first 10 lines and then quit. (important later)

### `2>` error out.
`2>` redirect errors.

Example: `find / -name 'sample.txt' 2> errors.txt` refirect errors to file.

`find / -name 'sample.txt' 2> /dev/null` **/dev/null** is a blackhole in linux.

`&>` redirect standard out and stardard error

Example: `find / -name 'sample.txt' &> all.txt` redirect out and error to file. 

We can also direct standard out and error out to diffrent places:

`find / -name 'secretsauce*' > secretformula.txt 2> /dev/null`

## Pipes






