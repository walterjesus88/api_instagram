#test_api.py
"""
Employee class tests.
"""
import unittest

from api import Employee

class TestEmployeeComputePayout(unittest.TestCase):
    """Test the compute_payout method of the Employee class."""

    def setUp(self):
        """Set up test fixtures."""
        self.arjan = Employee(name=NAME, employee_id=EMPLOYEE_ID)
