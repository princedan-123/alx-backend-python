#!/usr/bin/env python3
"""A unit test script for access_nested_map function."""
from utils import access_nested_map
import unittest
from parameterized import parameterized


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
