import os
import pytest

# pytest実行時のオプション設定
def pytest_addoption(parser):
    parser.addoption("--os-name", default="linux", help="os name")

# 自作fixture
@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w') as c:
        print("before test")
        yield c
        print("after test")

