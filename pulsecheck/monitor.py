import socket
import time

def check_dns(hostname: str) -> str | None:
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        return None

def check_tcp(hostname: str, port: int, timeout: float = 3.0) -> float | None:
    start_time = time.perf_counter()

    try:
        with socket.create_connection((hostname, port), timeout=timeout):
            latency = (time.perf_counter() - start_time) * 1000
            return latency
    except OSError:
        return None
