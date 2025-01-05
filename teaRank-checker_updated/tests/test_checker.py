import pytest
from tearank_checker.checker import check_package_in_pypi, simulate_tearank

def test_check_package_in_pypi():
    # Test with a known package
    assert check_package_in_pypi("requests") == True
    # Test with a non-existent package
    assert check_package_in_pypi("nonexistentpackage1234") == False

def test_simulate_tearank(capsys):
    simulate_tearank("requests")
    captured = capsys.readouterr()
    assert "teaRank for 'requests'" in captured.out
