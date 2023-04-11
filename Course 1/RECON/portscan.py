from scapy.all import sr,IP,TCP
ports=[21,80,143,443,8080,8443]

def SynScan(host):
    ans,unans= sr(IP(dst=host)/TCP(sport=5555, dport=ports,flags="S"),timeout=2,verbose=0)
    print("Open Ports at ", host)
    for (s,r) in ans:
        if s[TCP].dport==r[TCP].dport:
            print(s[TCP].dport)
            
host ="203.124.44.78"
SynScan(host)