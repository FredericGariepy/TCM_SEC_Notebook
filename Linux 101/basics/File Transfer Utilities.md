# File Transfer Utilities `scp`
`scp` Secure copy using SSH protocol.

`scp file.txt 192.168.100.4:/home/michealjackson/` Sends the file.txt to the machines' michealjackson home directory.
> If the machine had a name on the network, it can be used instead of the IP.

`scp -r directory 192.168.100.4:/home/michealjackson/` Send a directory (`-r` recursively).

`scp 192.168.100.4:/home/michealjackson/beatit.mp3 backup/` Download the file **from** the remote machine to the local backup.

`scp -r 192.168.100.4:/home/michealjackson/album /home/` Download the file **from** the remote machine.

