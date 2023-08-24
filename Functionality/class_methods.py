'''
@classmethod | Setup_class(cls) | Setup_method(self, method) | teardown_class(cls) | teardown_method(self, method)
When running test cases within a test Class we will use setup and teardown functions
* @classmethod - stetup_class(css) and teardown_class(css) - used for doing actions at the beginning of the class or at the end
* setup_method and teardown method - used for doing actions before every test case
Flow
1 - @classmethod - stetup_class(css)
2 - setup_method(self, method)
3 - test case 1
4 - teardown_method(self, method)
5 - setup_method(self, method)
6 - test case 2
7 - teardown_method(self, method)
8 - @classmethod - teardown_class(css)

Structure:
Test_Class
@classmethod - starupclass(cls) - setting up class such as connecting into DB
Test cases in the class
Test cases in the class
Test cases in the class
Test cases in the class
@classmethod - teardownclass(cls) - tearing down class such as closing connecting with DB
'''
import pytest

class TestExample:
    @classmethod
    def setup_class(cls):
        print("Setting up the test class...")
        # Perform class-level setup operations here

    @classmethod
    def teardown_class(cls):
        print("Tearing down the test class...")
        # Perform class-level teardown operations here

    def setup_method(self, method):
        print("Setting up the test method...")
        # Perform test case-level setup operations here

    def teardown_method(self, method):
        print("Tearing down the test method...")
        # Perform test case-level teardown operations here

    def test_addition(self):
        print("Running test_addition...")
        assert 2 + 2 == 4

    def test_subtraction(self):
        print("Running test_subtraction...")
        assert 5 - 3 == 2



