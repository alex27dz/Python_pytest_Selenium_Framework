import pytest

'''
* @classmethod - stetup_class(css) and teardown_class(css) - used for doing actions at the beginning of the class and at the end
* setup_method and teardown method - used for doing actions before and after every test case

Structure:
Test_Class
@classmethod
stetup_class(cls)
setup_method(self, method)
teardown_method(self, method)
test case 1
test case 2
test case 3
@classmethod
teardown_class(cls)

When running:
@classmethod
stetup_class(cls) -> runs before everything within the class
setup_method(self, method) -> runs before every test case in the class
test case 1
teardown_method(self, method)
setup_method(self, method) -> runs before every test case in the class
test case 2
teardown_method(self, method)
setup_method(self, method) -> runs before every test case in the class
test case 3
teardown_method(self, method)
@classmethod
teardown_class(cls)
'''

class Test_Class_Example:
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



