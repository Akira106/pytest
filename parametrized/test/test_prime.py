import sys
sys.path.append("../")
from prime import is_prime
import pytest

# 1つ1つ
def test_is_prime():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)

# パラメータ化
@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True)
])
def test_is_prime2(number, expected):
    assert is_prime(number) == expected
