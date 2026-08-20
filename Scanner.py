import socket


COMMON_PORTS = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP Proxy"
}


def scan_port(target, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)

            result = sock.connect_ex((target, port))

            return result == 0

    except socket.error:
        return False


def main():
    print("=" * 40)
    print("          Python Port Scanner")
    print("=" * 40)

    target = input("Target: ").strip()

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if not 1 <= start_port <= 65535:
            raise ValueError

        if not 1 <= end_port <= 65535:
            raise ValueError

        if start_port > end_port:
            raise ValueError

    except ValueError:
        print("\nInvalid port range.")
        return

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\nCould not resolve target.")
        return

    print(f"\nTarget: {target}")
    print(f"IP:     {target_ip}")
    print(f"Ports:  {start_port}-{end_port}")
    print("\nScanning...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            service = COMMON_PORTS.get(port, "Unknown")

            print(f"[OPEN]  {port:<5} {service}")

            open_ports.append(port)

    print("\n" + "=" * 40)
    print(f"Scan completed.")
    print(f"Open ports: {len(open_ports)}")
    print("=" * 40)


if __name__ == "__main__":
    main()
