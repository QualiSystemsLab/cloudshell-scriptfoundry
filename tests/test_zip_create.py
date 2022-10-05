import os

import pytest

from scriptfoundry.utilities import zip_archive_handler


def _test_create(script_dir_name: str) -> zip_archive_handler.ZipDetails:
    curr_dir = os.getcwd()
    script_full_path = os.path.join(curr_dir, "test-assets", "zip-test-scripts", script_dir_name)
    return zip_archive_handler.create_dist_archive(script_dir_path=script_full_path)


def test_simple_create():
    assert _test_create("simple_script").zip_file_name


def test_nested_create():
    assert _test_create("nested_dir_script").zip_file_name


def test_invalid_handler():
    with pytest.raises(zip_archive_handler.InvalidScriptDirectory):
        _test_create("invalid_script")
