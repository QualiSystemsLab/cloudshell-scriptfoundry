import click
from shellfoundry.exceptions import FatalError

from scriptfoundry.utilities import zip_archive_handler


def pack_script(script_name: str = None, script_dir_path: str = None) -> zip_archive_handler.ZipDetails:
    try:
        zip_details = zip_archive_handler.create_dist_archive(script_name, script_dir_path)
    except zip_archive_handler.InvalidScriptDirectory as e:
        raise FatalError(str(e))
    click.secho(f"'{zip_details.script_name}' zip archive created")
    return zip_details
