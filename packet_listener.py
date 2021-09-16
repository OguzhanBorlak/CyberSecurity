import scapy.all as scapy
from scapy_http import http


def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
#if you want save packets >> store=true



def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)
    #packet.show()

listen_packets("your interface(eth0,wlan0...)")