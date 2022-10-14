from cloudshell.api.cloudshell_api import CloudShellAPIError, CloudShellAPISession
from shellfoundry.exceptions import FatalError

from scriptfoundry.utilities import config_handler


class AutomationApiGenerator:
    """Read Shellfoundry config and create automation api client instance with credentials"""

    def __init__(self):
        self._shellfoundry_config = config_handler.get_shellfoundry_config()

    def create_client(self) -> CloudShellAPISession:
        """
        Custom automation api port other than 8029 not supported - pass from config key to here if support requested
        """
        client = None
        try:
            client = CloudShellAPISession(
                host=self._shellfoundry_config.host,
                username=self._shellfoundry_config.username,
                password=self._shellfoundry_config.password,
                domain=self._shellfoundry_config.domain,
            )
        except CloudShellAPIError as e:
            if e.code == "118":
                raise FatalError(f"Login to CloudShell failed. {str(e)}")
        except Exception as e:
            raise FatalError(f"Failed to connect to cloudshell: {str(e)}")
        return client
