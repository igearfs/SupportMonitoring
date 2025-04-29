# resourcemonitor/tcp_monitor.py
import socket

def check_tcp_port(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, socket.error):
        return False
