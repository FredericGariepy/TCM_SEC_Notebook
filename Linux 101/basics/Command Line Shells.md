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

`alias del='rm -rfi'` making our own alias called 'del' which will execute  `rm` with `rfi` flags, meaning it is reccursive forced and interactive (prompts for delete).











