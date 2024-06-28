import time

import pytest

from lib.admin_lib import admin


class Test_add:
    def setup_method(self):
        pass

    def teardown_method(self):
        admin.click_element(css='.result-list-item .btn-no-border')
        admin.wb.switch_to.alert.accept()
        time.sleep(1)
        admin.close_wb()

    @pytest.mark.parametrize('device_type,sn,desc', [
        ('存储柜', 'elife-canbinlocker-g22-10-20-40', '南京e生活存储柜-10大20中40小'),
        ('存储柜', 'test__sn001' * 10, '南京e生活存储柜-10大20中40小'),
        ('电瓶车充电站', 'bokpower-charger-g22-220v450w', '杭州bok 2022款450瓦 电瓶车充电站'),
        ('洗车站', 'njcw-carwasher-g22-2s', '南京e生活2022款洗车机 2个洗车位'),
        ('汽车充电站', 'yixun-charger-g22-220v7kw', '南京易迅能源2022款7千瓦汽车充电站')
    ])
    def test_add_devices_type(self, device_type, sn, desc):
        # 登录管理员账号
        admin.login()
        # 添加设备
        admin.add_devices_type(device_type=device_type, devices_sn=sn, devices_desc=desc)
        # 获取刚刚添加的设备信息（list）
        act_list = admin.get_added_devices_type()
        # 检查添加的内容是否正确
        assert act_list == [device_type, sn, desc]
        # admin.close_wb()


# 修改设备
class Test_alter_devices_type:
    def setup_method(self):
        # 登录管理员账号
        admin.login()
        # 添加测试数据
        admin.add_devices_type(device_type='存储柜', devices_sn='elife-canbinlocker-g22-10-20-40',
                               devices_desc='南京e生活存储柜-10大20中40小')
        admin.close_wb()

    def teardown_method(self):
        # 登录管理员账号
        admin.login()
        # 删除测试数据
        admin.delete_device()
        admin.close_wb()

    def test_alter_device_info(self):
        # 登录账号
        admin.login()
        # 修改创建的设备信息
        admin.alter_device_info(device_type='汽车充电站', devices_sn='测试sn', devices_desc='测试desc')
        # 获取修改后的设备信息
        devices_list = admin.get_added_devices1_type()
        print('实际列表数据：', devices_list)
        assert devices_list == ['汽车充电站', '测试sn', '测试desc']


# 删除设备
class Test_delete:
    def setup_method(self):
        # 登录管理员账号
        admin.login()
        # 添加测试数据
        admin.add_devices_type(device_type='存储柜', devices_sn='elife-canbinlocker-g22-10-20-40',
                               devices_desc='南京e生活存储柜-10大20中40小')
        admin.close_wb()

    def teardown_method(self):
        pass

    def test_delete_device(self):
        # 登录管理员账号
        admin.login()
        # 删除最近添加的一条设备信息
        admin.delete_device()
        # 获取设备信息
        res = admin.get_added_devices1_type()
        assert res == None
