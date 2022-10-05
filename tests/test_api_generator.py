from scriptfoundry.utilities.api_generator import AutomationApiGenerator


def test_api_client_generator():
    api = AutomationApiGenerator().create_client()
    all_topologies = api.GetTopologiesByCategory().Topologies
    print(f"\ntopology count: {len(all_topologies)}")
    assert isinstance(all_topologies, list)
