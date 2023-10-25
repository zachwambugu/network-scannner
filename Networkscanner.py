from scapy.all import ARP, Ether, srp

# Create an ARP request packet to discover devices
arp = ARP(pdst="192.168.1.0/24")
eth = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = eth/arp

# Send the packet and capture responses
result = srp(packet, timeout=3, verbose=0)[0]

# List the discovered devices
devices = []
for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})

# Print the list of devices
for device in devices:
    print(f"IP Address: {device['ip']} | MAC Address: {device['mac']}")
