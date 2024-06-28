# import pytest
#
# from lib.admin_lib import admin
#
#
# @pytest.fixture(scope='package', autouse=True)
# def st_emptyEnv():
#     # 登录
#     admin.login()
#     # 添加设备类型
#     devices_type = [['电瓶车充电站', 'type_a', '测试设备'],
#                     ['洗车站', 'type_a', '测试设备'],
#                     ['存储柜', 'type_a', '测试设备']]
#     for one in devices_type:
#         # 添加设备
#         admin.add_devices_type(device_type=one[0], devices_sn=one[1], devices_desc=one[2])
#     # 添加计费规则
#     'rules_type, rule_name, least_cost, expect_cost, charge_unit, unit_price,code'
#     admin.add_business_rule(rules_type='预付费-下发业务量', rule_name='全国-电瓶车充电费率1', least_cost='0.1',
#                             expect_cost='2', charge_unit='千瓦时', unit_price='1')
#     admin.add_business_rule(rules_type='预付费-下发费用', rule_name='南京-洗车机费率1', least_cost='2',
#                             expect_cost='10')
#     admin.add_business_rule(rules_type='后付费-上报业务量', rule_name='南京-存储柜费率1', charge_unit='小时',
#                             unit_price='2', code='业务码100L')
#     yield
#
#     admin.login()
#     for one in range(3):
#         admin.delete_rule()
#         admin.delete_device()
