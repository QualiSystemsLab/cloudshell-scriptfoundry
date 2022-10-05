import os
from pathlib import Path

import pytest
from cookiecutter.exceptions import OutputDirExistsException
from pytest import fixture

from scriptfoundry import constants
from scriptfoundry.utilities import template_handler


@fixture
def local_templates_path():
    current_dir = os.getcwd()
    templates_path = os.path.join(current_dir, "test-assets", "template-test-scripts")
    return templates_path


@fixture
def github_repo():
    return constants.GITHUB_TEMPLATES_REPO


@fixture
def output_dir() -> str:
    current_dir = os.getcwd()
    output_path = os.path.join(current_dir, "template-dist")
    Path(output_path).mkdir(exist_ok=True)
    return output_path


def test_local_create(local_templates_path, output_dir):
    try:
        template_handler.create_from_local(
            local_templates_path=local_templates_path,
            script_name="setup local test",
            script_type="setup",
            output_dir=output_dir,
        )
    except OutputDirExistsException:
        pass


def test_github_create(github_repo, output_dir):
    try:
        template_handler.create_from_github(
            github_repo=github_repo, script_name="setup github test", script_type="setup", output_dir=output_dir
        )
    except OutputDirExistsException:
        pass


def test_invalid_script_name(local_templates_path, output_dir):
    with pytest.raises(template_handler.InvalidScriptType):
        template_handler.create_from_local(
            local_templates_path, script_name="setup pytest invalid", script_type="lol", output_dir=output_dir
        )
