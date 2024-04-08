from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """A class that inherits TestCase."""
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json_object):
        """
            A test case that test GithubOrgClient.org
            returns the correct value.
        """
        client = GithubOrgClient(org_name)
        full_url = client.ORG_URL.format(org=client._org_name)
        client.org()
        mock_json_object.assert_called_once_with(full_url)
