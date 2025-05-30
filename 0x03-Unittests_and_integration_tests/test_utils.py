#!/usr/bin/env python3
"""A test module to test the utils.access_nested_map function."""
from parameterized import parameterized
import unittest
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json

class TestAccessNestedMap(unittest.TestCase):
    """A test class to test access_nested_map function."""
    @parameterized.expand(
        [
            ('single_dictionary', {"a": 1}, ("a",), 1),
            ('double_nested_dictionary', {"a": {"b": 2}}, ("a",), {"b": 2}),
            ('two_keys', {"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, name, map, path, expected):
        self.assertEqual(access_nested_map(map, path), expected)
    
    @parameterized.expand([
        ('no dictionary', {}, ("a",), KeyError),
        ('excess keys', {"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, name, map, path, expected):
        """A test case to check for exceptions."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(map, path)
            self.assertEqual(path, str(context.exception))

class TestGetJson(unittest.TestCase):
    """This class uses mocks a function."""
    @parameterized.expand([
        ('True', 'http://example.com', {'payload': True}),
        ('False', 'http://holberton.io', {'payload': False})
    ])
    def test_get_json(self, name, url, expected):
        """Test that utils.get_json returns the expected result."""
        with patch('utils.requests.get') as mock_get:
            def mock_behaviour(url):
                response = Mock()
                if url == 'http://example.com':
                    response.json.return_value = {"payload": True}
                    return response
                if url == 'http://holberton.io':
                    response.json.return_value = {"payload": False}
                    return response
                response.json.return_value = ValueError('error no value')
                return response
            mock_get.side_effect = mock_behaviour
            output = get_json(url)
            self.assertEqual(output, expected)
            mock_get.assert_called_once_with(url)
