#!/usr/bin/env python3
"""
Tests for the ineed module
"""

import json
import os
import tempfile
import unittest
from ineed import INeed


class TestINeed(unittest.TestCase):
    """Test cases for INeed class"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.manager = INeed(data_file=self.temp_file.name)
    
    def tearDown(self):
        """Clean up after tests"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_add_need(self):
        """Test adding a new need"""
        need = self.manager.add_need("Test need", priority="high")
        self.assertEqual(need["description"], "Test need")
        self.assertEqual(need["priority"], "high")
        self.assertFalse(need["completed"])
        self.assertEqual(need["id"], 1)
    
    def test_list_needs(self):
        """Test listing needs"""
        self.manager.add_need("Need 1")
        self.manager.add_need("Need 2")
        
        needs = self.manager.list_needs()
        self.assertEqual(len(needs), 2)
        
        # Complete one need
        self.manager.complete_need(1)
        
        # Should only show 1 active need
        active_needs = self.manager.list_needs()
        self.assertEqual(len(active_needs), 1)
        
        # Should show both when including completed
        all_needs = self.manager.list_needs(show_completed=True)
        self.assertEqual(len(all_needs), 2)
    
    def test_complete_need(self):
        """Test completing a need"""
        need = self.manager.add_need("Test need")
        need_id = need["id"]
        
        completed = self.manager.complete_need(need_id)
        self.assertIsNotNone(completed)
        self.assertTrue(completed["completed"])
        self.assertIsNotNone(completed["completed_at"])
    
    def test_complete_nonexistent_need(self):
        """Test completing a need that doesn't exist"""
        result = self.manager.complete_need(999)
        self.assertIsNone(result)
    
    def test_remove_need(self):
        """Test removing a need"""
        need = self.manager.add_need("Test need")
        need_id = need["id"]
        
        result = self.manager.remove_need(need_id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.needs), 0)
    
    def test_remove_nonexistent_need(self):
        """Test removing a need that doesn't exist"""
        result = self.manager.remove_need(999)
        self.assertFalse(result)
    
    def test_persistence(self):
        """Test that needs are saved and loaded correctly"""
        # Add some needs
        self.manager.add_need("Need 1")
        self.manager.add_need("Need 2", priority="high")
        
        # Create a new manager instance with the same file
        new_manager = INeed(data_file=self.temp_file.name)
        
        # Should have the same needs
        self.assertEqual(len(new_manager.needs), 2)
        self.assertEqual(new_manager.needs[0]["description"], "Need 1")
        self.assertEqual(new_manager.needs[1]["priority"], "high")
    
    def test_default_priority(self):
        """Test that default priority is medium"""
        need = self.manager.add_need("Test need")
        self.assertEqual(need["priority"], "medium")


if __name__ == "__main__":
    unittest.main()
