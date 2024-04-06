#!/usr/bin/env python3
"""A unit test script for access_nested_map function."""
from utils import access_nested_map, get_json
import utils
import unittest
from parameterized import parameterized
from unittest.mock import (patch, Mock)


class TestAccessNestedMap(unittest.TestCase):
    """A class that provides test cases to test acess_nested_map function."""
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1), ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
                ]
            )
    def test_access_nested_map(self, map, key, expected):
        """A test case for acess_nested_map function."""
        self.assertEqual(access_nested_map(map, key), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, map, key):
        """
        A test case that test if the acess_nested_map raises an exception.
        """
        with self.assertRaises(KeyError):
            access_nested_map(map, key)


class TestGetJson(unittest.TestCase):
    """A subclass of unitttest.TestCase used for testing."""
    @parameterized.expand(
            [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]
            )
    def test_get_json(self, url, payload):
        """
            A test case that checks if a function
            returns a particular result.
        """
        mock_respone = Mock()
        mock_respone.json.return_value = {"payload": True}
        with patch('utils.requests.get') as mock_object:
            data = get_json(url)
            mock_object.return_value = mock_respone
            mock_object.assert_called_once_with(url)
            self.assertEqual(data, payload)
