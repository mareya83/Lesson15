import unittest
from app import user, admin, developer


class TestCase(unittest.TestCase):

    def test_is_string(self):
        self.assertIsInstance(user.sey_hello(), str)
        

    def test_is_num(self):
        self.assertIsInstance(admin.mend_something(), int)

    def test_is_list(self):
        self.assertIsInstance(developer.write_code(), list)

    def test_is_numbers(self):
        for item in developer.write_code():
            self.assertIsInstance(item, int)

if __name__ == '__main__':
    unittest.main()