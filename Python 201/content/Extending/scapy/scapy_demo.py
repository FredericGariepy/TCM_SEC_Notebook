from scapy.all import IP, ICMP, send, srp,  Ether, ARP
#from scapy.all import wireshark

default_target_IP = '192.168.56.1'
def send_ICMP(target_IP):
    ip_layer = IP(dst=target_IP)
    icmp_layer = ICMP()
    # '/' is overloaded 
    packet = ip_layer / icmp_layer
    send(packet)
    print(packet.show())
    #wireshark(packet) #uncomment to show the packet in wireshark

#send_ICMP(target_IP=target_IP)

# Send and receive packets at layer 2
# ARP request packet targeting the 192.168.10.0/24 network
default_target_network = '192.168.10.0/24'
def send_ARP(target_network):
    APR_dst = "ff:ff:ff:ff:ff:ff" # all Fs for ARP DST
    answered, unanswered = srp( Ether(dst=APR_dst)/ ARP(pdst=target_network), timeout=5, verbose=False)
    for a in answered:
        print(a)

from scapy.all import IP, TCP, sr1, RandShort

SYN = 0x02
RST = 0x04
ACK = 0x10

default_dst_IP = "127.0.0.1"
def port_scan(dst_IP=default_dst_IP):
    for port in [22,80,139,443,445, 8080]: 

        # Generate a random source port for the SYN packet
        src_port = RandShort()
        # Send a SYN packet
        tcp_connect = sr1(IP(dst=dst_IP)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=False)
        
        if tcp_connect and tcp_connect.haslayer(TCP):
            response_flags = tcp_connect.getlayer(TCP).flags
            
            if response_flags == (SYN + ACK):
                snd_rst =  send(IP(dst=dst_IP)/TCP(sport=RandShort(), dport=port, flags="AR"), verbose=False)
                print("{} is open".format(port))
            
            elif  response_flags == (RST + ACK):
                print("{} is closed".format(port))
        else:
            print("{} is closed".format(port))

from scapy.all import sniff
from scapy.layers.http import HTTPRequest

def process(packet):
    if packet.haslayer(HTTPRequest):
        host = packet[HTTPRequest].Host.decode() if packet[HTTPRequest].Host else "Unknown"
        path = packet[HTTPRequest].Path.decode() if packet[HTTPRequest].Path else "/"
        print(f"Host: {host}, Path: {path}")

def siff_livepackets():
    sniff(filter='port 80',prn=process, store=False)

