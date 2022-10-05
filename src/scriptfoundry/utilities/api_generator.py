from cloudshell.api.cloudshell_api import CloudShellAPISession, CloudShellAPIError
from shellfoundry.exceptions import FatalError
from shellfoundry.utilities.config_reader import CloudShellConfigReader, Configuration


class AutomationApiGenerator(object):
    """ Read Shellfoundry config and create automation api client instance with credentials """
    def __init__(self):
        self._cs_config = Configuration(CloudShellConfigReader()).read()

    def create_client(self) -> CloudShellAPISession:
        """ TODO: add config setting for automation api port and pass here """
        try:
            client = CloudShellAPISession(
                host=self._cs_config.host,
                username=self._cs_config.username,
                password=self._cs_config.password,
                domain=self._cs_config.domain,
            )
        except CloudShellAPIError as e:
            if e.code == "118":
                raise FatalError(f"Login to CloudShell failed. {str(e)}")
        except Exception as e:
            raise FatalError(f"Failed to instantiate cloudshell automation api client: {str(e)}")
        else:
            return client
