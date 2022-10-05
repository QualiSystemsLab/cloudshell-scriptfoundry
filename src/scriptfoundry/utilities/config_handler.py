from dataclasses import dataclass

from shellfoundry.utilities.config_reader import CloudShellConfigReader, Configuration, InstallConfig, get_with_default

# config keys
SCRIPT_TEMPLATE_LOCATION = "script_template_location"

# default values
DEFAULT_SCRIPT_TEMPLATE_LOCATION = "Empty"


@dataclass
class ScriptFoundryInstallConfig:
    script_template_location: str

    @staticmethod
    def get_default():
        return ScriptFoundryInstallConfig(DEFAULT_SCRIPT_TEMPLATE_LOCATION)


class ScriptFoundryConfigReader:
    @staticmethod
    def get_defaults():
        return ScriptFoundryInstallConfig.get_default()

    @staticmethod
    def read_from_config(config) -> ScriptFoundryInstallConfig:
        script_template_location = get_with_default(config, SCRIPT_TEMPLATE_LOCATION, DEFAULT_SCRIPT_TEMPLATE_LOCATION)
        return ScriptFoundryInstallConfig(script_template_location)


def get_scriptfoundry_config() -> ScriptFoundryInstallConfig:
    return Configuration(ScriptFoundryConfigReader()).read()


def get_shellfoundry_config() -> InstallConfig:
    return Configuration(CloudShellConfigReader()).read()
