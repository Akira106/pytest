import unittest
from unittest.mock import MagicMock
from unittest import mock
import salary

class TestSalary(unittest.TestCase):
    def test_calculation_salary(self):
        s = salary.Salary(year=2017)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        assert s.calculation_salary() == 101
        # 本当にこの関数は呼ばれたのか
        s.bonus_api.bonus_price.assert_called()
        # 1回だけ呼ばれたのか
        s.bonus_api.bonus_price.assert_called_once()
        assert s.bonus_api.bonus_price.call_count == 1

        s.bonus_api.bonus_price.assert_called_with(year=2017)

    def test_calculation_salary_no_salary(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=1)
        assert s.calculation_salary() == 100
        # このMockは呼ばれないはず
        s.bonus_api.bonus_price.assert_not_called()

    @mock.patch("salary.ThirdPartyBonusRestApi.bonus_price")
    def test_calculation_salary_patch(self, mock_bonus):
        mock_bonus.return_value = 1

        s = salary.Salary(year=2017)
        assert s.calculation_salary() == 101
        mock_bonus.assert_called()

    def test_calculation_salary_patch_with(self):
        with mock.patch("salary.ThirdPartyBonusRestApi.bonus_price") as mock_bonus:
            mock_bonus.return_value = 1
            s = salary.Salary(year=2017)
            assert s.calculation_salary() == 101
            mock_bonus.assert_called()

    def setup_method(self, method):
        self.patcher = mock.patch("salary.ThirdPartyBonusRestApi.bonus_price")
        self.mock_bonus = self.patcher.start()

    def teardown_method(self, method):
        self.patcher.stop()

    def test_calculation_salary_patcher(self):
        self.mock_bonus.return_value = 1

        s = salary.Salary(year=2017)

        assert s.calculation_salary() == 101
        self.mock_bonus.assert_called()

