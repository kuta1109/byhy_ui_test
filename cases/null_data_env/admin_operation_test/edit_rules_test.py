import pytest

from lib.admin_lib import admin


class Test_add_rules:
    def setup_method(self):
        pass

    def teardown_method(self):
        admin.login()
        admin.delete_rule()

    @pytest.mark.parametrize('rules_type, rule_name, least_cost, expect_cost, charge_unit, unit_price,code',
                             [('预付费-下发业务量', '全国-电瓶车充电费率1', '0.1', '2', '千瓦时', '1', ''),
                              ('预付费-下发费用', '南京-洗车机费率1', '2', '10', '', '', ''),
                              ('后付费-上报业务量', '南京-存储柜费率1', '', '', '小时', '2', '业务码100L'),
                              ('后付费-上报业务量', '南京-存储柜费率1', '', '', '小时', '1', '业务码50L'),
                              ('后付费-上报业务量', '南京-存储柜费率1', '', '', '小时', '0.5', '业务码10L')])
    def test_add_rules(self, rules_type, rule_name, least_cost, expect_cost, charge_unit, unit_price, code):
        admin.login()
        admin.add_business_rule(rules_type=rules_type, rule_name=rule_name, least_cost=least_cost,
                                expect_cost=expect_cost, charge_unit=charge_unit, unit_price=unit_price, code=code)
        act_list = admin.get_added_rules()
        assert sorted(act_list) == sorted(
            [rules_type, rule_name, least_cost, expect_cost, charge_unit, unit_price, code])
