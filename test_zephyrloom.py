# test_zephyrloom.py
"""
Tests for ZephyrLoom module.
"""

import unittest
from zephyrloom import ZephyrLoom

class TestZephyrLoom(unittest.TestCase):
    """Test cases for ZephyrLoom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZephyrLoom()
        self.assertIsInstance(instance, ZephyrLoom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZephyrLoom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
