import socket 

domain = "youtube.com";

try:
    ip = socket.gethostbyname(domain);
    print(f"Ip address of the given {domain} is : {ip}");
except Exception:
    print("Socket connection failed");
    
     