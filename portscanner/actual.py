import socket
import concurrent.futures
import time

GREEN   = "\033[92m"
RED     = "\033[91m"
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
MAGENTA = "\033[95m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

open_ports = 0


def header(ip):
    print(f"""{CYAN}{BOLD}
═══════════════════════════════════════════════════════
                    PORT SCANNER
═══════════════════════════════════════════════════════

Target : {WHITE}{ip}{CYAN}

┌──────────┬────────┬────────────────┐
│ PORT     │ STATUS │ SERVICE        │
├──────────┼────────┼────────────────┤{RESET}""")


def footer():
    print(f"""{CYAN}
└──────────┴────────┴────────────────┘
{RESET}""")


def format_result(port, status, service):
    if status == "OPEN":
        color = GREEN
    else:
        color = RED

    print(
        f"│ {port}/tcp".ljust(10) +
        f"│ {color}{status:<6}{RESET} │ "
        f"{service:<14} │"
    )


def banner__(message):
    print(f"""{YELLOW}
╭──────────── Banner ────────────╮
│ {message.strip()}
╰────────────────────────────────╯
{RESET}""")


def scan(ip, port):
    global open_ports

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports += 1
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "unknown"
            format_result(port, "OPEN", service)
            try:
                banner = sock.recv(1024).decode(errors="ignore")
                if banner.strip():
                    banner__(banner)

            except socket.timeout:
                pass
    except Exception as e:
        print(f"{RED}[ERROR]{RESET} Port {port}: {e}")
    finally:
        sock.close()

def port_scan(target, start_port, end_port):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{RED}Unable to resolve hostname.{RESET}")
        return
    header(ip)
    start = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        for port in range(start_port, end_port + 1):
            futures.append(executor.submit(scan, ip, port))
        concurrent.futures.wait(futures)
    footer()
    end = time.time()
    print(f"""{MAGENTA}
═══════════════════════════════════════
            Scan Summary
═══════════════════════════════════════
Host          : {ip}
Ports Scanned : {end_port-start_port+1}
Open Ports    : {open_ports}
Time Taken    : {end-start:.2f} sec
═══════════════════════════════════════
{RESET}""")
if __name__ == "__main__":

    target = input("Target Host/IP : ")

    start_port = int(input("Start Port    : "))
    end_port = int(input("End Port      : "))

    port_scan(target, start_port, end_port)