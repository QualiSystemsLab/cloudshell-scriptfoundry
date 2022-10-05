[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python/)
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

Configure "Shellfoundry" Credentials (shared by "Scriptfoundry")

```commandline
shellfoundry config host localhost
shellfoundry config username admin
shellfoundry config password admin
```

To check configured values:

```commandline
shellfoundry config
```

See [Shellfoundry Reference](https://help.quali.com/Online%20Help/0.0/Portal/Content/DevGuide/Reference/Shellfoundry.htm?tocpath=The%20CloudShell%20DevGuide%7CReference%7C_____2)
for more info.

Generate new project:

```commandline
scriptfoundry new setup_config_firewall --template setup
```

Zip and upload to cloudshell:

```commandline
cd setup_config_firewall
scriptfoundry update setup_config_firewall
```

### Commands Overview

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

### Template Generation

"New" command generates script template. 
The templates map to the orchestration script "types" in cloudshell (setup, teardown, default, save, restore, resource).

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

To Setup up Offline mode:
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