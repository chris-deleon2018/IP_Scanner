# IP_Scanner
Simple IP Scanner using Scapy

Limitations: The scanner uses ARP broadcasts to scan a subnet and is limited to a broadcast domain.

## How to Run
```
python network_scanner-v2.0.py -t <target_ip/CIDR>
```
## Help Menu
```
python network_scanner-v2.0.py --help
```
```
network_scanner-v2.0.py [-h] [-t TARGET]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target IP/CIDR. Ex: 192.168.1.0/24
```
