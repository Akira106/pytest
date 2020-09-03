import calculation
import pytest
import os

is_release = True
class TestCal():
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = calculation.Cal()
        cls.test_file_name = "test.txt"
        cls.test_dir = "/tmp/test_dir"

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal

    def setup_method(self, method):
        print("method={}".format(method.__name__))

    def teardown_method(self, method):
        import shutil
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        print("method={}".format(method.__name__))


    def test_add_num_and_double(self, request, csv_file):
        os_name = request.config.getoption("--os-name")
        print(os_name)

        print(csv_file)
        assert self.cal.add_num_and_double(1, 1) == 4

    #@pytest.mark.skip(reason="skip")
    def test_add_num_and_double_raise1(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    @pytest.mark.skipif(is_release==True, reason="skip")
    def test_add_num_and_double_raise2(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

