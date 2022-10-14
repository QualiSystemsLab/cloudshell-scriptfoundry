import socket

from shellfoundry.exceptions import FatalError

from scriptfoundry.utilities import config_handler


class CloudshellConnectityError(Exception):
    pass


class GithubConnectityError(Exception):
    pass


def is_connected(host: str, port: int) -> bool:
    """Connect to the host -- tells us if the host is reachable"""
    try:
        socket.create_connection((host, port), 5)
    except OSError:
        return False
    return True


def validate_github_connectivity() -> bool:
    if not is_connected(host="github.com", port=443):
        raise FatalError("Failed to connect to Github to pull templates")


def validate_cloudshell_connectivity():
    shellfoundry_config = config_handler.get_shellfoundry_config()
    if not is_connected(host=shellfoundry_config.host, port=shellfoundry_config.port):
        err_msg = f"Cloudshell connectivity Failed. Host: {shellfoundry_config.host}, Port {shellfoundry_config.port}"
        raise FatalError(err_msg)
