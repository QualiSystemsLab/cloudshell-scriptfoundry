import click
from cookiecutter.exceptions import OutputDirExistsException
from shellfoundry.exceptions import FatalError

from scriptfoundry import constants
from scriptfoundry.utilities import check_connectivity, config_handler, template_handler


class NewScriptExecutor:
    def __init__(self):
        self._shellfoundry_config = config_handler.get_shellfoundry_config()
        self._scriptfoundry_config = config_handler.get_scriptfoundry_config()

    @property
    def online_mode(self) -> bool:
        return self._shellfoundry_config.online_mode.lower() == "true"

    @property
    def local_templates_path(self) -> str:
        return self._scriptfoundry_config.script_template_location

    @staticmethod
    def _validate_local_path(local_path):
        if local_path == config_handler.DEFAULT_SCRIPT_TEMPLATE_LOCATION:
            raise FatalError(f"Please set shellfoundry attribute: '{config_handler.SCRIPT_TEMPLATE_LOCATION}' ")

    def _create_script(self, script_name: str, script_type: str, output_dir: str = "."):
        if self.online_mode:
            check_connectivity.validate_github_connectivity()
            template_handler.create_from_github(
                github_repo=constants.GITHUB_TEMPLATES_REPO,
                script_name=script_name,
                script_type=script_type,
                output_dir=output_dir,
            )
        else:
            self._validate_local_path(self.local_templates_path)
            template_handler.create_from_local(
                local_templates_path=self.local_templates_path,
                script_name=script_name,
                script_type=script_type,
                output_dir=output_dir,
            )

    def create_script(self, script_name: str, script_type: str, output_dir: str = "."):
        script_name = template_handler.format_script_name(script_name)
        try:
            self._create_script(script_name, script_type, output_dir)
        except OutputDirExistsException as e:
            raise FatalError(f"Script '{script_name}' already exists in this directory") from e
        click.echo(f"Created script '{script_name}' from '{script_type}' template")
