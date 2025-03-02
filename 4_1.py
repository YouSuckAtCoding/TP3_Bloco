import ipaddress


address = ipaddress.ip_address("192.168.1.5")
net = ipaddress.ip_network("192.168.1.0/24")

contains = address in net

print(contains)


