from scapy.all import *
DEST_IP = '127.0.0.1'

def main():
    a = input("enter msg:")
    for char in a:
        print(ord(char))
        send((IP(dst=DEST_IP)/UDP(dport=ord(char))))
        
main()