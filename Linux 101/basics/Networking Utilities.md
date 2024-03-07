# Networking at the Command Line
***This is a very short list of networking commands, this is the basics after all..***
## `ping` *can you hear me?* Test network connection
`ping -c 3 google.com` Ping google.com 3 times. 
## `ifconfig` See & configure network interfaces
## `ip` *Replacement to ifconfig*
`ip -s address` see address information 

`ip link` see network interfaces

`sudo ip link set dev enp0s3 down` Bring down enp0s3 network connection.

`sudo ip link set dev enp0s3 up` Bring up enp0s3 network connection.

`ip route` | `route`  Routing information in diffrent format.

`sudo ip route add 10.0.03.0/24 via 10.0.2.1` Add a route(10.0.03.0) via gateway(10.0.2.1).

`sudo ip route delete 10.0.03.0/24 via 10.0.2.1` Delete the route.

`nslookup domain.com` | `dig domain.com` Find DNS, dig provides more infomation.

`dig -x 8.8.8.8` Reverse DNS lookup on ip address.

`netstat -at` Current network connection and statistics.

`netstat -lt` Listening TCP ports

`ip neigh` View the neighbor table, information about devices on the local network.
