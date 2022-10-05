from scriptfoundry.utilities import custom_config_reader


def test_scriptfoundry_reader():
    config = custom_config_reader.get_scriptfoundry_config()
    template_location = config.script_template_location
    print(f"\nscript template path: '{template_location}'")
    assert isinstance(template_location, str)
