# cloudshell-scriptfoundry
A CLI tool to generate script templates, package them and upload to cloudhsell.
This tool is an optional, separately downloaded add-on to the [shellfoundry](https://github.com/QualiSystems/shellfoundry) shell development cli tool.
"Scriptfoundry" has shellfoundry as a dependency, and re-uses the same cli configuration. 



### Installation

```
pip install cloudshell-scriptfoundry
```

### Basic Usage

#### Top Level Commands
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

#### New Command
Generate new script from available templates. The templates map to the orchestration script "types" in cloudshell (setup, teardown, etc)

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

#### Sample Flow

Generate new project:
```commandline
scriptfoundry new setup_config_firewall --template setup
```

Zip and upload to cloudshell:
```commandline
cd setup_config_firewall
scriptfoundry update setup_config_firewall
```


### Offline Mode
Online mode will pull cookiecutter templates from [github repo](https://github.com/QualiSystemsLab/cloudshell-script-templates)
For Offline mode:
1. download templates from [github release page](https://github.com/QualiSystemsLab/cloudshell-script-templates/releases)
2. Unzip templates and copy to designated location on client dev machine
3. Set Shellfoundry config "online_mode" to False
4. Add custom config key to shellfoundry config, with the templates path as value

Sample Command:
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