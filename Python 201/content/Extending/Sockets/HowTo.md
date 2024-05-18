#### Run the socket.py demo file to open a server port listening
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

