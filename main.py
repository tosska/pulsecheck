import argparse
import json
from datetime import datetime, timezone

from pulsecheck.monitor import check_dns, check_tcp

def monitor_host(hostname: str, port: int) -> dict:
    ip_address = check_dns(hostname)

    if ip_address is None:
        return {
            "hostname": hostname,
            "ip_address": None, 
            "dns_status": "FAILED",
            "tcp_status": "SKIPPED",
            "port": port,
            "latency_ms": None,
        }

    latency = check_tcp(hostname, port)

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "dns_status": "OK",
        "tcp_status": "OPEN" if latency is not None else "FAILED",
        "port": port,
        "latency_ms": round(latency, 2) if latency is not None else None,
    }

def main():
    parser= argparse.ArgumentParser(
        description="PulseCheck - Network & Service Monitoring Tool"
    )

    parser.add_argument(
        "hostnames",
        nargs = "+",
        help = "One or more hostnames to monitor (e.g., example.com)"
    )

    parser.add_argument(
        "-p", "--port",
        type = int,
        default = 443,
        help = "TCP port to check (default: 443)"
    )

    parser.add_argument(
        "--json",
        help="Export monitoring results to a JSON file"
    )

    args = parser.parse_args()

    results = []

    print("\nPULSECHECK - NETWORK MONITOR")
    print("=" * 65)

    for hostname in args.hostnames:
        result = monitor_host(hostname, args.port)
        results.append(result)

        print(f"\nTarget: {result['hostname']}")
        print(f"  DNS:     {result['dns_status']}")

        if result["ip_address"]:
            print(f"  IP:      {result['ip_address']}")

        print(f"  TCP:     {result['tcp_status']} (port {args.port})")

        if result["latency_ms"] is not None:
            print(f"  Latency: {result['latency_ms']} ms")

    if args.json:
        report = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "results": results
        }

        with open(args.json, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        print(f"\nJSON report saved to: {args.json}")

    print("\n" + "=" * 65)
    print(f"Monitoring completed: {len(results)} target(s)")


if __name__ == "__main__":
    main()

