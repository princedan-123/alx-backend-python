#!/usr/bin/env python3
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import patch, PropertyMock


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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """
            A test case for public_repos_url property method of
            GithubOrgClient class
        """
        mock_org.return_value = 'https://api.github.com/orgs/example_org/repos'
        client = GithubOrgClient('example_org')
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock,
            return_value='https://api.github.com/orgs/example_org/repos'
            ) as mocked_property:
            result = client._public_repos_url
            self.assertEqual(result, mocked_property.return_value)
