from enum import Enum

from cookiecutter.main import cookiecutter


class ScriptTypes(Enum):
    SETUP_TYPE = "setup"
    TEARDOWN_TYPE = "teardown"
    SAVE_TYPE = "save"
    RESTORE_TYPE = "restore"
    BLUEPRINT_TYPE = "blueprint"
    RESOURCE_TYPE = "resource"

    @classmethod
    def script_type_values(cls):
        return [x.value for x in cls]


class InvalidScriptType(Exception):
    pass


def _validate_script_type(script_type: str):
    if script_type not in ScriptTypes.script_type_values():
        raise InvalidScriptType(f"{script_type} is not valid. Select from {ScriptTypes.script_type_values()}")


def format_script_name(script_name: str) -> str:
    """
    Normalize script input to be valid command name
    Example: "Setup Script Name" --> "setup_script_name"
    """
    return script_name.strip().lower().replace(" ", "_").replace("-", "_")


def _create_template(template_path: str, script_name: str, script_type: str, output_dir: str = ".") -> str:
    _validate_script_type(script_type)
    script_name = format_script_name(script_name)
    ec = {"script_name": script_name}
    return cookiecutter(template=template_path, no_input=True, extra_context=ec, directory=script_type, output_dir=output_dir)


def create_from_local(local_templates_path: str, script_name: str, script_type: str, output_dir: str = ".") -> str:
    return _create_template(local_templates_path, script_name, script_type, output_dir)


def create_from_github(github_repo: str, script_name: str, script_type: str, output_dir: str = ".") -> str:
    return _create_template(github_repo, script_name, script_type, output_dir)
