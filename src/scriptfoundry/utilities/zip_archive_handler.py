import os
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import List

DIRS_TO_EXCLUDE = [".git", "dist", "venv", ".idea"]
FILES_TO_EXCLUDE = ["credentials.py", "debug.py"]


@dataclass
class ZipDetails:
    script_dir_path: str
    script_dir_name: str
    script_name: str
    zip_file_name: str
    archive_path: str


class InvalidScriptDirectory(Exception):
    """checking for __main__.py in dir"""


def _validate_script_dir(src_path: str):
    """Validate top level folder that it has a __main__.py entry point"""
    files = os.listdir(src_path)
    dir_name = os.path.basename(src_path)
    if "__main__.py" not in files:
        msg = f"No '__main__.py' file found in '{dir_name}' Directory. Not a valid cloudshell script."
        raise InvalidScriptDirectory(msg)


def _is_valid_file(file_name: str, file_path: str, files_to_exclude: List[str]):
    invalid_conditions = [
        file_name.endswith(".pyc"),
        file_name.endswith(".zip"),
        file_name in files_to_exclude,
        file_name == os.path.basename(__file__),  # exclude the updater script
        not os.path.isfile(file_path),
    ]
    if any(invalid_conditions):
        return False
    return True


def _create_dist_folder(script_dir_path: str):
    Path(f"{script_dir_path}/dist").mkdir(exist_ok=True)


def _create_zip_archive(archive_output_path: str, script_dir_src_path: str):
    with zipfile.ZipFile(archive_output_path, "w", zipfile.ZIP_DEFLATED) as archive_file:
        for dirpath, _, filenames in os.walk(script_dir_src_path):
            dir_name = os.path.basename(dirpath)

            # skip dist and other excluded folders
            if dir_name in DIRS_TO_EXCLUDE:
                continue

            # validate files and add to archive
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                if not _is_valid_file(filename, file_path, FILES_TO_EXCLUDE):
                    continue
                archive_file_path = os.path.relpath(file_path, script_dir_src_path)
                archive_file.write(file_path, archive_file_path)

    # validate generated zip archive
    with zipfile.ZipFile(archive_output_path, "r") as archive_file:
        bad_file = zipfile.ZipFile.testzip(archive_file)

        if bad_file:
            raise zipfile.BadZipFile(f"CRC check failed for {archive_output_path} with file {bad_file}")


def get_zip_details(script_name: str = None, script_dir_path: str = None) -> ZipDetails:
    """
    Compile default values
    """
    script_dir_path = script_dir_path or os.getcwd()
    script_name = script_name or os.path.basename(script_dir_path)
    zip_file_name = script_name + ".zip"
    archive_path = os.path.join(script_dir_path, "dist", zip_file_name)
    return ZipDetails(
        script_dir_path=script_dir_path,
        script_dir_name=os.path.basename(script_dir_path),
        script_name=script_name,
        zip_file_name=f"{script_name}.zip",
        archive_path=archive_path,
    )


def create_dist_archive(script_name: str = None, script_dir_path: str = None) -> ZipDetails:
    zip_details = get_zip_details(script_name, script_dir_path)
    _validate_script_dir(zip_details.script_dir_path)
    _create_dist_folder(zip_details.script_dir_path)
    _create_zip_archive(archive_output_path=zip_details.archive_path, script_dir_src_path=zip_details.script_dir_path)
    return zip_details
