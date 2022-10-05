import click
from shellfoundry.exceptions import FatalError

from scriptfoundry.commands.pack_command import pack_script
from scriptfoundry.utilities.api_generator import AutomationApiGenerator
from scriptfoundry.utilities.zip_archive_handler import get_zip_details


class ScriptUpdateExecutor:
    def __init__(self):
        self._api = AutomationApiGenerator().create_client()

    def update_script(self, script_name: str, script_dir_path: str):
        zip_details = get_zip_details(script_name, script_dir_path)
        with click.progressbar(length=2, show_eta=False, label="uploading script") as pbar:
            pack_script(script_name, script_dir_path)
            pbar.make_step(1)
            pbar.render_progress()

            try:
                self._api.UpdateScript(script_name, zip_details.archive_path)
            except Exception as e:
                raise FatalError(f"Failed to update script. {type(e).__name__}: {str(e)}")
            finally:
                pbar.finish()
                pbar.render_progress()
        click.secho(f"{script_name} Updated on Cloudshell", fg="green")
