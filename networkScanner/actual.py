import socket
import threading
import queue

from scapy.all import *
def scan(ip, result_queue):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    answered, unanswered = srp(
        packet,
        timeout=2,
        verbose=False
    )
    for sent, rev in answered:
        try:
            hostname = socket.gethostbyaddr(rev.psrc)[0]
        except socket.herror:
            hostname = "Unknown"
        result_queue.put(
            ( rev.psrc, rev.hwsrc, hostname ))
        
def main():
    result_queue = queue.Queue()
    t = threading.Thread(
        target=scan,
        args=("UR _ IP _ ADDRESS", result_queue)
    )
    t.start()
    t.join()
    while not result_queue.empty():
        ip, mac, hostname = result_queue.get()
        print(f"IP: {ip} | " f"MAC: {mac} | " f"Hostname: {hostname}"  )

if __name__ == "__main__":
    main()