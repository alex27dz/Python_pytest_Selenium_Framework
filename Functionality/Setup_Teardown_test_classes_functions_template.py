import pytest

class TestClass:
    # test_data = None

    @classmethod
    def setup_class(cls):
        # Set up any necessary resources or fixtures for the entire test class
        cls.test_data = [1, 2, 3, 4, 5]
        print(cls.test_data)

    def setup_method(self):
        # Set up any necessary resources or fixtures for each individual test method
        self.mean = sum(self.test_data) / len(self.test_data)
        print(self.mean)

    @classmethod
    def teardown_class(cls):
        # Clean up any resources or fixtures used by the entire test class
        del cls.test_data

    def teardown_method(self):
        # Clean up any resources or fixtures used by each individual test method
        del self.mean


    def test_mean_calculation(self):
        # Test the calculation of the mean of the test data
        assert self.mean == pytest.approx(3.0)



class TestMyClass:

    @classmethod
    def setup_class(cls):
        # This method is run before any tests in the class are run
        cls.my_data = [1, 2, 3]
        print('Hi its setup steps')

    @classmethod
    def teardown_class(cls):
        del cls.my_data
        print('\n Hi its teardown cleanup steps')

    def test_my_data_contains_three_elements(self):
        assert len(self.my_data) == 3

    def test_my_data_contains_four_elements(self):
        self.my_data.append(4)
        assert len(self.my_data) == 4

def test_before_approx():
    print('\n')
    print(0.2 + 0.3)

def test_approx():
    print('\n')
    print(0.1 + 0.2)
    assert 0.1 + 0.2 == 0.3
    assert 0.1 + 0.2 == pytest.approx(0.3)

def test_approx_with_tolerance():
    assert 0.1 + 0.2 == pytest.approx(0.3, rel=1e-6, abs=1e-12)