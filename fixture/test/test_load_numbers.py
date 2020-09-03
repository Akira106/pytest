import sys
sys.path.append("../")
from load_numbers import load_numbers_sorted
import pytest
import os

@pytest.fixture
def txt(tmpdir):
    tmpfile = tmpdir.join('numbers.txt')

    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)

    tmpfile.remove('numbers.txt')

def test_load_numbers_sored(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
