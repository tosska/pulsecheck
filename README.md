# PulseCheck

**A lightweight network and service monitoring tool built with Python.**

PulseCheck is a command-line application designed to monitor network hosts and verify the availability of TCP services.

## Features

- **DNS Resolution:** resolves hostnames into IPv4 addresses.
- **TCP Monitoring:** checks whether a TCP port accepts connections.
- **Latency Measurement:** measures TCP connection establishment time in milliseconds.
- **Multi-target Monitoring:** monitors multiple hostnames in a single execution.
- **JSON Reports:** exports monitoring results to a JSON file.
- **Error Handling:** handles DNS resolution and connection failures.

## Technologies

- Python 3.12+
- Socket
- Argparse
- JSON
- Pytest

## Installation

Clone the repository:

```bash
git clone https://github.com/tosska/pulsecheck.git
cd pulsecheck
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the testing dependency:

```bash
python -m pip install pytest
```

## Usage

Monitor a single host:

```bash
python main.py github.com
```

Monitor multiple hosts:

```bash
python main.py github.com google.com cloudflare.com
```

Specify a custom TCP port:

```bash
python main.py github.com --port 443
```

Export results to JSON:

```bash
python main.py github.com google.com --json report.json
```

## Testing

Run the automated test suite:

```bash
python -m pytest -v
```

## Project Status

Version 0.1.0 — Initial functional CLI implementation.

## Future Improvements

- Concurrent monitoring
- HTTP/HTTPS response checks
- Historical monitoring data with SQLite
- Continuous monitoring
- Web dashboard using FastAPI

## License

MIT License.
