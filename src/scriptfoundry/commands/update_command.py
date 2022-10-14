import os

import click
from cloudshell.api.cloudshell_api import CloudShellAPIError
from shellfoundry.exceptions import FatalError

from scriptfoundry.commands.pack_command import pack_script
from scriptfoundry.utilities import check_connectivity
from scriptfoundry.utilities.api_generator import AutomationApiGenerator


class ScriptUpdateExecutor:
    def __init__(self):
        self._api = AutomationApiGenerator().create_client()

    def update_script(self, script_name: str = None, script_dir_path: str = None):
        check_connectivity.validate_cloudshell_connectivity()
        with click.progressbar(length=2, show_eta=False, label="uploading script") as pbar:
            zip_details = pack_script(script_name, script_dir_path)
            pbar.make_step(1)
            pbar.render_progress()

            try:
                # need to change dir before uploading, otherwise full path gets stored in cloudshell and causes issues
                dist_dir = os.path.join(zip_details.script_dir_path, "dist")
                os.chdir(dist_dir)
                self._api.UpdateScript(zip_details.script_name, zip_details.zip_file_name)
            except CloudShellAPIError as e:
                if e.code == "100":
                    raise FatalError(f"'{zip_details.script_name}' not on Cloudshell. Upload manually the first time.")
            except Exception as e:
                raise FatalError(f"Failed to update script. {type(e).__name__}: {str(e)}")
            finally:
                pbar.finish()
                pbar.render_progress()
        click.secho(f"'{zip_details.script_name}' updated on Cloudshell", fg="green")
