import click
import pkg_resources

from scriptfoundry.commands.new_command import NewScriptExecutor
from scriptfoundry.commands.pack_command import pack_script
from scriptfoundry.commands.update_command import ScriptUpdateExecutor
from scriptfoundry.utilities.template_handler import ScriptTypes


@click.group()
def cli():
    pass


@cli.command()
def version():
    """Display scriptfoundry version"""
    click.echo("scriptfoundry version " + pkg_resources.get_distribution("cloudshell-scriptfoundry").version)


@cli.command()
@click.option(
    "--name",
    required=False,
    help="(Optional) - Specify custom script name. Defaults to directory name.",
)
@click.option(
    "--path",
    required=False,
    help="(Optional) - Specify path to directory. Defaults to current directory.",
)
def pack(name, path):
    """Create script zip archive"""
    pack_script(script_name=name, script_dir_path=path)


@cli.command()
@click.option(
    "--name",
    required=False,
    help="(Optional) - Specify custom script name. Defaults to directory name.",
)
@click.option(
    "--path",
    required=False,
    help="(Optional) - Specify path to directory. Defaults to current directory.",
)
def update(name, path):
    """Create zip archive and update on CloudShell"""
    ScriptUpdateExecutor().update_script(script_name=name, script_dir_path=path)


@cli.command()
@click.argument("name")
@click.option(
    "--template",
    required=True,
    type=click.Choice(ScriptTypes.script_type_values()),
    default=ScriptTypes.BLUEPRINT_TYPE.value,
    help="Specify script template 'type'. Defaults to 'blueprint'.",
)
@click.option(
    "--output",
    required=False,
    default=".",
    help="(Optional) - Specify path to output directory. Defaults to current directory.",
)
def new(name, template, output):
    """Create new script from template"""
    NewScriptExecutor().create_script(script_name=name, script_type=template, output_dir=output)
