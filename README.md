ARP Scanner Script

This script utilizes the Scapy library to perform ARP scanning on a local network to discover devices.

Requirements:
- Python 3
- Scapy library (install using: pip install scapy)

Usage:
1. Modify the 'pdst' parameter in the ARP packet to specify the target IP address range.
2. Run the script.

Output:
The script sends ARP requests to all IP addresses in the specified range and prints the discovered devices along with their IP and MAC addresses.
