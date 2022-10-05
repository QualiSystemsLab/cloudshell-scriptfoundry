[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python/)
[![Lint and Test](https://github.com/QualiSystemsLab/cloudshell-scriptfoundry/actions/workflows/lint-test.yml/badge.svg)](https://github.com/QualiSystemsLab/cloudshell-scriptfoundry/actions/workflows/lint-test.yml)
[![PyPI version](https://badge.fury.io/py/cloudshell-scriptfoundry.svg)](https://badge.fury.io/py/cloudshell-scriptfoundry)

# Cloudshell Scriptfoundry

A CLI tool to generate, package and upload cloudshell orchestration scripts.
This tool is an optional add-on to the [shellfoundry](https://github.com/QualiSystems/shellfoundry) shell development
cli tool.
"Scriptfoundry" has shellfoundry as a dependency, and re-uses the same cli configuration.

### Installation

```
pip install cloudshell-scriptfoundry
```

### Basic Usage

Generate new project:

```commandline
scriptfoundry new setup_config_firewall --template setup
```

Zip and upload to cloudshell:

```commandline
cd setup_config_firewall
scriptfoundry update setup_config_firewall
```

### Top Level Commands

```commandline
Usage: scriptfoundry [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  new      Create new script from template
  pack     Create script zip archive
  update   Create zip archive and update on CloudShell
  version  Display scriptfoundry version
```

### New Command Details

Generate new script from available templates. The templates map to the orchestration script "types" in cloudshell (
setup, teardown, etc). Script can optionally be generated to a different directory.

```commandline
Usage: scriptfoundry new [OPTIONS] NAME

  Create new script from template

Options:
  --template [setup|teardown|save|restore|blueprint|resource]
                                  Specify script template 'type'. Defaults to
                                  'blueprint'.  [required]

  --output TEXT                   (Optional) - Specify path to output
                                  directory. Defaults to current directory.

  --help                          Show this message and exit.


```

### Offline Mode

Online mode will pull cookiecutter templates
from [github repo](https://github.com/QualiSystemsLab/cloudshell-script-templates)
For Offline mode:

1. download templates
   from [github release page](https://github.com/QualiSystemsLab/cloudshell-script-templates/releases)
2. Unzip templates and copy to designated location on client dev machine
3. Set Shellfoundry config "online_mode" to False
4. Add custom config key to shellfoundry config, with the templates path as value

Sample Configuration:

```commandline
shellfoundry config online_mode False
shellfoundry config script_template_location "C:\cloudshell_dev_files\cloudshell-script-templates-0.1.0"
```

## Dependencies

Scriptfoundry is built on top of shellfoundry, and its underlying open-source dependencies

- [shellfoundry](https://github.com/QualiSystems/shellfoundry) - cloudshell config management
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) - script template generation
- [Click](https://click.palletsprojects.com/en/5.x/) - CLI interface

### License

Free Software: MIT License