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
