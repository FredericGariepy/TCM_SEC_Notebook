#### Run the socket.py demo file to open a server or a client (2 or 1)
`netstat -an`

Find the socket listening (waiting for connections)
> TCP    127.0.0.7:8080         0.0.0.0:0              LISTENING

Open up Putty to test the connection
| Option | Setting |
| - | - | 
| Host Name | 127.0.0.7 |
| Post | 8080 |
| Connection type | Raw |
| Close window on exit | Never |

### In wireshark the server - client connection can be shown in the packet sniffer
![image](https://github.com/FredericGariepy/TCM_SEC_Notebook/assets/96602008/f54009e4-7b02-4b91-945d-85a1064e0003)
![image](https://github.com/FredericGariepy/TCM_SEC_Notebook/assets/96602008/7cb230db-9094-4c35-9b6c-4b56f5ecb687)


