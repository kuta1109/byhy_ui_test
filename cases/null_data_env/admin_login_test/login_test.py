import time

import pytest

from lib.admin_lib import admin


class Test_admin_login:
    @pytest.mark.parametrize('username,password,check_word', [
        ('', 'sdfsdf', '请输入用户名'),
        ('byhy', '', '请输入密码'),
        ('byhy', 'sdfsdfs', '登录失败： 用户名或密码错误'),
        ('byhy', 'sdfsd', '登录失败： 用户名或密码错误'),
        ('byhy1', 'sdfsdf', '用户名不存在'),
        ('byh', 'sdfsdf', '用户名不存在')
    ])
    # 错误登录case
    def test_wrong_login(self, username, password, check_word):
        # 输入账号登录
        admin.login(username=username, password=password)
        time.sleep(1)
        # 检查弹窗信息
        assert admin.get_alert_text() == check_word

    # 正确登录case
    def test_right_login(self):
        # 输入正确账号登录
        admin.login()
        time.sleep(1)
        # 检查登录账号昵称
        assert admin.check_login_user() == '1号超级管理员'
