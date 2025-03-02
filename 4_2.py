#!usr/bin/env python3
import ipaddress

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
            print("Invalid ipv4 netowork")
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
            print("Invalid ipv4 address")
            return

        if add is not ipaddress.AddressValueError:

            ip = add.exploded
            longestPrefix = []
            for bit in ip:
             
                if bit in curr.children:
                    curr = curr.children[bit]
                    longestPrefix.append(bit)
                else:
                    break

            return curr.IsEndOfIp, longestPrefix


trie = Trie()
trie.insert("192.168.0.0/16")  
trie.insert("192.168.1.0/24")  
trie.insert("10.0.0.0/8")  

isEnd, longest = trie.search("192.168.1.100")
print(f"Longest prefix is : {''.join(longest)}" )