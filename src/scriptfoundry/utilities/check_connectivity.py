import socket

from scriptfoundry.utilities import config_handler


def is_connected(host: str, port: int) -> bool:
    """Connect to the host -- tells us if the host is reachable"""
    try:
        socket.create_connection((host, port), 5)
    except OSError:
        return False
    return True


def is_github_connected() -> bool:
    return is_connected(host="github.com", port=443)


def is_cloudshell_connected() -> bool:
    shellfoundry_config = config_handler.get_shellfoundry_config()
    return is_connected(host=shellfoundry_config.host, port=shellfoundry_config.port)
