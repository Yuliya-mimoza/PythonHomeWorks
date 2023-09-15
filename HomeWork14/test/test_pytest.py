from task1 import Triangle
import pytest


@pytest.fixture
def check1():
    return Triangle(3, 6, 6)


@pytest.fixture
def check2():
    return Triangle(5, 5, 5)


@pytest.fixture
def check3():
    return Triangle(4, 5, 6)


def test_get_isosceles(check):
    assert check1() == 'Треугольник - равнобедренный'


def test_get_equilateral(check):
    assert check2() == 'Треугольник - равносторонний'


def test_get_versatile(check):
    assert check3() == 'Треугольник - разносторонний'
