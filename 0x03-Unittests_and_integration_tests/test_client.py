#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """A class that test the client.GithubOrgClient class."""
    @parameterized.expand([
        ('google_test', 'google', {"login": "google","id": 1342004}),
        ('abc_test', 'abc', {"message": "Not Found", "status": "404"})
    ])
    @patch('client.get_json')
    def test_org(self, name, org, expected, mock_get_json):
        """A test case to test the org method of GithubOrgClient class."""

        mock_get_json.return_value = expected
        git_client = GithubOrgClient(org)
        output = git_client.org
        mock_get_json.assert_called_once_with('https://api.github.com/orgs/{org}'.format(org=org))
        self.assertEqual(output, expected)
    
    def test_public_repos(self):
        """A test case to test GithubOrgClient.public_repos."""
    
    @parameterized.expand([
            (
                'test_google',
                'google',
                'https://api.github.com/orgs/google/repos'
            ),
            (
                'test_abc',
                'abc',
                'KeyError: repos_url'
            )

        ]
    )
    
    def test_public_repos_url(self, name, org_name, expected):
        """
        A test case to test GithubOrgClient._public_repos_url.
        GithubOrgClient._public_repos_url depends on GithubOrgClient.org
        therefore GithubOrgClient.org will be mocked using patch
        """
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            google_payload = {
                "login": "google",
                    "id": 1342004,
                    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
                    "url": "https://api.github.com/orgs/google",
                    "repos_url": "https://api.github.com/orgs/google/repos","events_url": "https://api.github.com/orgs/google/events","hooks_url": "https://api.github.com/orgs/google/hooks","issues_url": "https://api.github.com/orgs/google/issues","members_url": "https://api.github.com/orgs/google/members{/member}"
            }
            bad_payload = {
                "message": "Not Found",
                    "documentation_url": "https://docs.github.com/rest/orgs/orgs#get-an-organization",
                    "status": "404"   
            }
            client = GithubOrgClient(org_name)
            if org_name == 'google':
                mock_org.return_value = google_payload
                result = client._public_repos_url
                self.assertEqual(result, expected)
            if org_name == 'abc':
                mock_org.return_value = bad_payload
                with self.assertRaises(KeyError):
                    client._public_repos_url

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """A test case to test GithubOrgClient.public_repos."""
        payload = [
            {
                "name": "google-repo-one",
                "license": {
                    "key": "apache-2.0"
                    }
            },
            {
                "name": "google-repo-two",
                "license": {
                    "key": "mit"
                    }
            },
            {
                "name": "google-repo-three",
                "license": None
            },
            {
                "name": "google-repo-four"
            }
        ]
        mock_get_json.return_value = payload
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com/orgs/google/repos'
            client = GithubOrgClient('google')
            public_repo = client.public_repos()
            expected_public_repo = [
                "google-repo-one", "google-repo-two",
                "google-repo-three", "google-repo-four"
                ]
            self.assertEqual(public_repo, expected_public_repo)
            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()