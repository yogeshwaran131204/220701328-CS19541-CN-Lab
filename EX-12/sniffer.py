from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        ip_layer=packet[IP]
        protocol=ip_layer.proto
        src_ip=ip_layer.src
        dst_ip=ip_layer.dst

        #determine the protocol
        protocol_name= ""
        if protocol==1:
            protocol_name="IP"
        elif protocol==6:
            protocol_name="ICMP"
        elif protocol==17:
            protocol_name="UDP"
        else:
            protocol_name="Unknown"

        #print the packet details

        print(f"Protocol: {protocol_name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print("-"*50)

def main():
    sniff( prn=packet_callback, filter="ip", store=0)

if __name__ =="__main__":
    main()
