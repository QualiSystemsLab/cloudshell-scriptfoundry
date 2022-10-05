from scriptfoundry.utilities import config_handler


def test_scriptfoundry_reader():
    config = config_handler.get_scriptfoundry_config()
    template_location = config.script_template_location
    print(f"\nscript template path: '{template_location}'")
    assert isinstance(template_location, str)
