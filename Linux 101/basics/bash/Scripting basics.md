`nano firstscript.sh`
```
#!/bin/bash

# First line tells the interpretors what to use for execute the script.
# Eveything else is after a '#' is a commnent.

# store the stdout of 'whoami' into a variable  user notice the wrap $().
user=$(whoami)

hostname=$(hostname)

directory=$(pwd)

# echo a string of the vaiables
echo "Users=[$user] Host=[$hostname] Working Dir=[$directory]"

echo "Contents:"
# here we simply execute the ls command. 
ls
```

###  executing scripts
`ls -l firstscript.sh` To check execute priviledge on the shell file.

`chmod +x firstscript.sh` to add exec.

`bash firstscript.sh`

`./firstscript.sh`
