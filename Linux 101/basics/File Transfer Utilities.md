# File Transfer Utilities `scp` `rsync`
## `scp` Secure copy using SSH protocol.

`scp file.txt 192.168.100.4:/home/michealjackson/` Sends the file.txt to the machines' michealjackson home directory.
> If the machine had a name on the network, it can be used instead of the IP.

`scp -r directory 192.168.100.4:/home/michealjackson/` Send a directory (`-r` recursively).

`scp 192.168.100.4:/home/michealjackson/beatit.mp3 backup/` Download the file **from** the remote machine to the local backup.

`scp -r 192.168.100.4:/home/michealjackson/album /home/` Download the file **from** the remote machine.

`scp lyrics.txt micheal@192.168.100.4:/home/michealjackson/` Sends the lyrics.txt to the machines' michealjackson home directory *as the user* micheal. Use the password for the account micheal.

## `rsync`
**Only copies the files that have been changed.**

*(calculates the diffrence between files being sent)*

> `rsync` has a lot of options, take a look a the man pages.
> Use the flag `--dry--run` to test more complicated uses before actually running the command.

`rsync -avzh file.txt 10.0.2.2:/home/bob` Sends the file.txt to bob's homme. 

Options used: `-a` archive mode. `-z` compress files as they are transfered. `-v` verbose. `-h` human readable.

