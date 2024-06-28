import pytest
from lib.admin_lib import admin


# 电瓶车充电站、洗车站、存储柜
# 预付费-下发业务量、预付费下发费用、后付费-上报业务量
class Test_add_devices:
    def setup_class(self):
        # 登录
        admin.login()
        # 添加设备类型
        devices_type = [['电瓶车充电站', 'type_a', '测试设备'],
                        ['洗车站', 'type_a', '测试设备'],
                        ['存储柜', 'type_a', '测试设备']]
        for one in devices_type:
            # 添加设备
            admin.add_devices_type(device_type=one[0], devices_sn=one[1], devices_desc=one[2])
        # 添加计费规则
        'rules_type, rule_name, least_cost, expect_cost, charge_unit, unit_price,code'
        admin.add_business_rule(rules_type='预付费-下发业务量', rule_name='全国-电瓶车充电费率1', least_cost='0.1',
                                expect_cost='2', charge_unit='千瓦时', unit_price='1')
        admin.add_business_rule(rules_type='预付费-下发费用', rule_name='南京-洗车机费率1', least_cost='2',
                                expect_cost='10')
        admin.add_business_rule(rules_type='后付费-上报业务量', rule_name='南京-存储柜费率1', charge_unit='小时',
                                unit_price='2', code='业务码100L')

    def teardown_class(self):
        admin.login()
        for one in range(3):
            admin.delete_rule()
            admin.delete_device()

    def setup_method(self):
        pass

    def teardown_method(self):
        admin.login()
        admin.delete_added_device()

    @pytest.mark.parametrize('add_device_info', [(['电瓶车充电站', 'type_a', '全国-电瓶车充电费率1', 'sn_001', '']),
                                                 (['洗车站', 'type_a', '全国-电瓶车充电费率1', 'sn_002', '']),
                                                 (['存储柜', 'type_a', '全国-电瓶车充电费率1', 'sn_003', ''])])
    def test_add_device(self, add_device_info):
        admin.login()
        admin.add_device(device_type=add_device_info[0], device_model=add_device_info[1], rule_id=add_device_info[2],
                         device_id=add_device_info[3])
        act_list = admin.get_added_device()
        assert sorted(act_list) == sorted(add_device_info)
