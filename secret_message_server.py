from scapy.all import *

def empty_udp_sniffer(packet):
    return UDP in packet and len(packet[UDP].payload) == 0

def main():
    print('listening')
    while True:
        a = sniff(lfilter=empty_udp_sniffer,count = 1)
        print(chr(a[0][UDP].dport))
main()