## Users and Groups
### View users with: `w` `who` `users`
`users` simply lists users, `w` provides the most information.

`who` provides users with account creation time.

### View user configs: `/etc/passwd`
see `/etc/passwd` file for user configs, this includes system profiles too.

Example: **root:x:0:0:root:/root:/bin/bash**

col.1. `root` username

col.2. `x` see `/etc/shadow` file for hashed passwords, if `*` disabled login

col.3. `0` user unique ID

col.4. `0` user unique Group ID

col.5. `root` additional text filed (can be name. tel. num, etc...)

col.7.  `root` user home directory

col.8. `/bin/bash` user's default shell

Example of non-system, normal user config:
**sally:x:1001:1001:sally, Office B,123-456-789,,:home/sally:bin/bash**

### View users groups: `/etc/group`
Checkout the group file, example **adm:x:4:syslog,bob**

**adm** is the admin group, often called "wheel" group

col.1. group name

col.2. group passwrod (no longer used)

col.3. group unique ID

col.4. member users (In E.g: syslog, bob)

Another example: **sudo:x:27:bob**

## File and Directory Permissions

### drwxrwxrwx lrwxrwxrwx -rwxrwxrwx

`d` directory 
`l` symbolic link
`-` file

`r` read
`w` write
`x` execute

-123 456 789

123 permissions for owner

456 permissions for group users

678 world permissions

### `chmod` permissions changes
| Octal | Permission |
|-------|------------|
| 4     | r          |
| 2     | w          |
| 1     | x          |

Example:  `chmod 777 file.txt` Gives full permissions to all.

Another way,

`chmod a=rwx file.txt`

**a** (all) users get read,write,exec.

`chmod a= file.txt`

**a** (all) users have *no permissions*

`chmod u=rwx,g=rwx,o=rwx file.txt`

**u**(user/owner), **g**(group), **o**(others) get read,write,exec.

### `chown` Change owner | `chgrp` Change group
Example: `sudo chown user file.txt`  Change user ownership

Example: `sudo chgrp group file.txt` Change group ownership

### `sudo` Super User | `su` Changing Users
`sudo` Super User DO , 1 command executed as root.

`sudo -u user command...` 1 command executed as user.

`su user` switch user

### `passwd` Changing Passwords
`passwd` to change user's *own* password.

`sudo passwd user` elevate priviledge to change other user's password.
