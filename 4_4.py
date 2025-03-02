#!usr/bin/env python3
import ipaddress
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.IsEndOfIp = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, ip):

        curr = self.root

        try:
            add = ipaddress.IPv4Network(ip)
        except ipaddress.NetmaskValueError:
            print("Invalid ipv4 network")
            return
      
        ip = add.exploded
        
        for bit in ip:   
            
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
           
        curr.IsEndOfIp = True

    
    def search(self, ip):

        curr = self.root

        try:
            add = ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            print("Invalid ipv6 address")
            return
            
        ip = add.exploded
        longestPrefix = []

        for bit in ip:
             
             if bit in curr.children:
                 curr = curr.children[bit]
                 longestPrefix.append(bit)
             else:
                 break
             
        return curr.IsEndOfIp, longestPrefix

def prefixMatchSearch(prefixes, value):

    temp = []
    longest = ""

    ip = value.exploded
    for prefix in prefixes:
        temp = []
        for i in range(0, len(ip)):
            if ip[i] == prefix[i]:
                temp.append(ip[i])
            else:
                if len(temp) > len(longest):
                    longest = ''.join(temp)
                break
    return longest
    

trie = Trie()
prefixes = []

file = open("ipv4_networks.txt", "r")
for line in file: 
    add = line.replace("\n", "")
    prefixes.append(ipaddress.IPv4Network(add).exploded)
    trie.insert(add)
file.close()

ip = "192.168.1.55"

startime = time.time()

isEnd, longest = trie.search(ip)
print(f"Longest prefix with Trie is : {''.join(longest)} in : {time.time() - startime}" ) 

startime = time.time()

print(f"Longest prefix linear is {prefixMatchSearch(prefixes, ipaddress.IPv4Address(ip))} in: {time.time() - startime}")

