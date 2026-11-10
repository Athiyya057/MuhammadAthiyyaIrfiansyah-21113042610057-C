import pytest

from employee import Employee


@pytest.fixture
def karyawan():
    return Employee("iyan", "putra", 65000)


def test_give_default_raise(karyawan):
    karyawan.give_raise()

    assert karyawan.salary == 70000


def test_give_custom_raise(karyawan):
    karyawan.give_raise(10000)

    assert karyawan.salary == 75000