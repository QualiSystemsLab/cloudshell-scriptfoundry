import os

from pytest import fixture
from shellfoundry.exceptions import FatalError

from scriptfoundry.commands.update_command import ScriptUpdateExecutor


def _get_script_dir(script_dir_name: str):
    curr_dir = os.getcwd()
    script_full_path = os.path.join(curr_dir, "test-assets", "zip-test-scripts", script_dir_name)
    return script_full_path


@fixture
def simple_script_dir():
    return _get_script_dir("simple_script")


def test_simple_update(simple_script_dir):
    try:
        ScriptUpdateExecutor().update_script(script_dir_path=simple_script_dir)
    except FatalError:
        pass


def test_update_different_name(simple_script_dir):
    try:
        ScriptUpdateExecutor().update_script(script_name="dev_simple_test", script_dir_path=simple_script_dir)
    except FatalError:
        pass
