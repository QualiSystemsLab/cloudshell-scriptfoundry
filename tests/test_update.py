import os

from pytest import fixture
from shellfoundry.exceptions import FatalError

from scriptfoundry.commands.update_command import ScriptUpdateExecutor


@fixture
def updater():
    return ScriptUpdateExecutor()


def _get_script_dir(script_dir_name: str):
    curr_dir = os.getcwd()
    script_full_path = os.path.join(curr_dir, "test-assets", "zip-test-scripts", script_dir_name)
    return script_full_path


def test_simple_update(updater):
    try:
        updater.update_script(script_dir_path=_get_script_dir("simple_script"))
    except FatalError:
        pass


def test_update_different_name(updater):
    try:
        updater.update_script(script_name="dev_simple_test", script_dir_path=_get_script_dir("simple_script"))
    except FatalError:
        pass
