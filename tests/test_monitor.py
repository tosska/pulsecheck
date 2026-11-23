import socket
from unittest.mock import patch

from pulsecheck.monitor import check_dns

def test_check_dns_return_ip():
    with patch("pulsecheck.monitor.socket.gethostbyname") as mock_dns:
        mock_dns.return_value = "192.0.2.10"

        result = check_dns("example.com")

        assert result == "192.0.2.10"

def test_check_dns_return_none_on_error():
    with patch("pulsecheck.monitor.socket.gethostbyname") as mock_dns:
        mock_dns.side_effect = socket.gaierror

        result = check_dns("invalid-domain")

        assert result is None