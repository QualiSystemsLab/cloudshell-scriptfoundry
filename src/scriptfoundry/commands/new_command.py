from cookiecutter.exceptions import OutputDirExistsException
from shellfoundry.exceptions import FatalError
import click

from scriptfoundry.utilities import template_handler
from scriptfoundry.utilities import custom_config_reader
from scriptfoundry import constants


class NewScriptExecutor:
    def __init__(self):
        self._shellfoundry_config = custom_config_reader.get_shellfoundry_config()
        self._scriptfoundry_config = custom_config_reader.get_scriptfoundry_config()

    @property
    def online_mode(self) -> bool:
        return self._shellfoundry_config.online_mode.lower() == "true"

    @property
    def local_templates_path(self) -> str:
        return self._scriptfoundry_config.script_template_location

    @staticmethod
    def _validate_local_path(local_path):
        if local_path == custom_config_reader.DEFAULT_SCRIPT_TEMPLATE_LOCATION:
            raise FatalError(f"Please set shellfoundry attribute: '{custom_config_reader.SCRIPT_TEMPLATE_LOCATION}' ")

    def _create_script(self, script_name: str, script_type: str, output_dir: str = "."):
        if self.online_mode:
            template_handler.create_from_github(github_repo=constants.GITHUB_TEMPLATES_REPO,
                                                script_name=script_name,
                                                script_type=script_type,
                                                output_dir=output_dir)
        else:
            self._validate_local_path(self.local_templates_path)
            template_handler.create_from_local(local_templates_path=self.local_templates_path,
                                               script_name=script_name,
                                               script_type=script_type,
                                               output_dir=output_dir)

    def create_script(self, script_name: str, script_type: str, output_dir: str = "."):
        script_name = template_handler.format_script_name(script_name)
        try:
            self._create_script(script_name, script_type, output_dir)
        except OutputDirExistsException:
            raise FatalError(f"Script '{script_name}' already exists in this directory")
        click.echo(f"Created script '{script_name}' from '{script_type}' template")