from .directory_or_file_name import ClassImported, function_name, other_function
import pytest


def test_alive():
    pass


@pytest.fixture
def empty_list():
    return ClassImported()


@pytest.fixture
def small_list():
    ll = ClassImported()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def other_testing_input(input):
    temp = other_function(input)
    return temp


def test_function_name_exists():
    assert function_name


def test_function_name_results_are_a_certain_way(other_testing_input):
    expected = other_testing_input(44)
    actual = function_name('input')
    assert expected == actual


def test_function_has_some_test_case_results(small_list):
    # do some code
    # assert some conclusion
    pass
