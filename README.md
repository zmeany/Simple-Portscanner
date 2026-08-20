# Python Port Scanner

A lightweight TCP port scanner written in Python for checking open ports on authorized targets.

## Features

- **TCP Scanning:** Checks whether TCP ports are accepting connections.
- **Custom Port Range:** Choose a specific start and end port to scan.
- **Hostname Support:** Accepts both IP addresses and hostnames.
- **Service Detection:** Identifies common services such as SSH, HTTP, HTTPS and SMB.
- **Connection Timeout:** Prevents the scanner from waiting indefinitely on unreachable ports.
- **Simple CLI:** Easy-to-use command-line interface with clear scan results.

## Tech Stack

- **Language:** Python
- **Networking:** TCP / IP
- **Library:** Python `socket`
- **Interface:** Command Line

## How it works

The scanner uses Python's built-in `socket` module to attempt a TCP connection to every port within the selected range.

The core functionality is handled by `socket.connect_ex()`:

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(timeout)
    result = sock.connect_ex((target, port))

    return result == 0
