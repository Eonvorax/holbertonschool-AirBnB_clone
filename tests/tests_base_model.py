#!/usr/bin/python3

"""
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """

    def test_1_id(self):
        """
        Test if id is a string.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)

    def test_2_created_at(self):
        """
        Test if created_at is datetime objects.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, datetime)

    def test_3_updated_at(self):
        """
        Test if updated_at is datetime objects.
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_4__str__(self):
        """
        Test if the return type is a string.
        """
        base_model = BaseModel()
        self.assertEqual(str, type(BaseModel.__str__(self)))

    def test_5_save_method(self):
        """
        Test if updated_at has been updated.
        """
        base_model = BaseModel()
        base_model.save()
        self.assertNotEqual(base_model.created_at, base_model.updated_at)

    def test_6_to_dict(self):
        """
        Test if the returned dictionary has the expected keys.
        """
        base_model = BaseModel()

        self.assertIn('id', base_model.to_dict())
        self.assertIn('created_at', base_model.to_dict())
        self.assertIn('updated_at', base_model.to_dict())
        self.assertIn('__class__', base_model.to_dict())


if __name__ == '__main__':
    unittest.main()