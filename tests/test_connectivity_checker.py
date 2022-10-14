from scriptfoundry.utilities import check_connectivity


def test_connectivity_checker():
    """This only passes if you are online"""
    assert check_connectivity.is_connected(host="google.com", port=443)


def test_github_connectivity():
    """This only passes if you are online"""
    check_connectivity.validate_github_connectivity()


def test_cloudshell_connectivity():
    """This requires cloudshell server connectivity"""
    check_connectivity.validate_cloudshell_connectivity()
