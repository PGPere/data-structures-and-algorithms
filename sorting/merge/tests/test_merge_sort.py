import pytest

from merge_sort.merge_sort import Merge


def test_exists():
    assert Merge


@pytest.mark.skip("TODO")
def test_array_1():
    array1 = [8, 4, 23, 42, 16, 15]
    actual = Sort.insertion_sort(array1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_array_2():
    array1 = [1, 1, 0]
    actual = Sort.insertion_sort(array1)
    expected = [0, 1, 1]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_array_3():
    array1 = [10, 9, 7, 5, 15, 1]
    actual = Sort.insertion_sort(array1)
    expected = [1, 5, 7, 9, 10, 15]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_array_4():
    array1 = [48, 1000, -1, 15, 0]
    actual = Sort.insertion_sort(array1)
    expected = [-1, 0, 15, 48, 1000]
    assert actual == expected
