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
            add = ipaddress.IPv6Network(ip)
        except ipaddress.NetmaskValueError:
            print("Invalid ipv6 address")
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
            add = ipaddress.IPv6Address(ip)
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


trie = Trie()
trie.insert("2001:db8::/32")  
trie.insert("2001:db8:1234::/48")

hasPrefix, longest = trie.search("2001:db8:1234:5678::1")
print(f"Longest prefix is : {''.join(longest)}" )


