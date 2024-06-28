import time

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.support.select import Select

from cfo.cfo import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class admin:
    # 登录账号
    def login(self, username=None, password=None):
        self.wb = webdriver.Chrome()
        self.wb.get(local_url)
        self.wb.implicitly_wait(5)
        if username == None and password == None:
            self.send_keys(css='body #username', input_text='byhy')
            self.send_keys(css='body #password', input_text='sdfsdf')
        else:
            self.send_keys(css='body #username', input_text=username)
            self.send_keys(css='body #password', input_text=password)
        self.click_element(css='body #loginBtn')

    # 获取登录账号昵称
    def check_login_user(self):
        name = self.find_element(css='#top-right>a').text
        return name

    # 获取alert弹窗文本
    def get_alert_text(self):
        alert_hint = self.wb.switch_to.alert.text
        return alert_hint

    # 查找单个元素
    def find_element(self, css):
        element = self.wb.find_element(By.CSS_SELECTOR, css)
        return element

    def find_elements(self, css):
        elements = self.wb.find_elements(By.CSS_SELECTOR, css)
        return elements

    # 点击元素
    def click_element(self, css):
        self.find_element(css=css).click()

    # 元素中输入内容
    def send_keys(self, css, input_text):
        self.find_element(css=css).clear()
        self.find_element(css=css).send_keys(input_text)

    # 添加设备
    def add_devices_type(self, device_type, devices_sn, devices_desc):
        # 点击设备型号
        self.click_element(css='[href="#/devicemodel"]')
        # 点击添加按钮
        # try:
        btn = self.find_element(css='.add-one-area>.btn')
        if btn.text == '添加':
            btn.click()
        elif btn.text == '取消':
            pass
        # except NoSuchElementException:
        #     pass
        # 选择设备种类
        select = Select(self.find_element(css='#device-type'))
        select.select_by_visible_text(device_type)
        # 输入设备型号
        self.send_keys(css='#device-model', input_text=devices_sn)
        # 输入型号描述
        self.send_keys(css='#device-model-desc', input_text=devices_desc)
        # 点击提交按钮
        self.click_element(css='.add-one-submit-btn-div > span')

    # 获取刚刚添加&修改的设备信息
    def get_added_devices_type(self):
        # 获取最新的一条设备信息
        items = self.find_element(css='.result-list-item-info')
        time.sleep(1)
        # 在设备信息中查找关键字
        info = [one.text for one in items.find_elements(By.CSS_SELECTOR, '.field .field-value')]
        time.sleep(1)
        return info

    # 获取刚刚添加&修改的设备信息
    def get_added_devices1_type(self):
        # 获取最新的一条设备信息
        # if self.wb.find_element(By.CSS_SELECTOR,'.result-list-item-info'):
        try:
            self.find_element(css='.result-list-item-info')
            items = self.find_element(css='.result-list-item-info')
            time.sleep(1)
            # 在设备信息中查找关键字
            info = [one.text for one in items.find_elements(By.CSS_SELECTOR, '.field .field-value')]
            time.sleep(1)
            return info
        except NoSuchElementException:
            return None

    # 修改设备信息
    def alter_device_info(self, device_type, devices_sn, devices_desc):
        # 点击设备型号
        self.click_element(css='[href="#/devicemodel"]')
        # 点击修改按钮，修改刚刚创建的一条信息
        self.click_element(css='.result-list-item-btn-bar > span:nth-child(2)')
        # 选择设备种类
        if device_type != None:
            select = Select(self.find_element(css='.result-list #device-type'))
            select.select_by_visible_text(device_type)
        time.sleep(10)

        # 输入设备型号
        if devices_sn:
            self.send_keys(css='.result-list .field:nth-child(2) input', input_text=devices_sn)
        # 输入型号描述
        if devices_desc:
            self.send_keys(css='.result-list .field:nth-child(3) input', input_text=devices_desc)
        # 点击提交按钮
        time.sleep(1)
        self.click_element(css='.result-list-item-btn-bar span')

    # 删除设备
    def delete_device(self):
        # 点击设备型号
        self.click_element(css='[href="#/devicemodel"]')
        # 点击修改按钮，修改刚刚创建的一条信息
        self.click_element(css='.result-list-item-btn-bar > span')
        # 点击系统弹窗中的确认
        self.wb.switch_to.alert.accept()

    def add_business_rule(self, rules_type, rule_name, least_cost=None, expect_cost=None, charge_unit=None,
                          unit_price=None, code=None, ):
        # 点击业务规则
        self.click_element(css='[href="#/svcrule"]')
        # 点击添加
        btn = self.find_element(css='.add-one-area>.btn')
        if btn.text == '添加':
            btn.click()
        elif btn.text == '取消':
            pass
        # 获取select所有选项
        select = Select(self.find_element(css='#rule_type_id'))
        # 选中要选的选项
        select.select_by_visible_text(text=rules_type)
        # 输入规则名称
        self.send_keys(css='.field:nth-child(1) >input', input_text=rule_name)
        # 输入规则类型,根据不同类型进行输入
        if rules_type == '预付费-下发业务量':
            # 输入消费数量
            self.send_keys(css='.field:nth-child(3) >input', input_text=least_cost)
            self.send_keys(css='.field:nth-child(4) >input', input_text=expect_cost)
            # 输入消费数量单位
            self.send_keys(css='.fee-rate > [type="text"]', input_text=charge_unit)
            self.send_keys(css='.fee-rate > [type="number"]', input_text=unit_price)
        elif rules_type == '预付费-下发费用':
            # 输入消费数量
            self.send_keys(css='.field:nth-child(3) >input', input_text=least_cost)
            self.send_keys(css='.field:nth-child(4) >input', input_text=expect_cost)
        elif rules_type == '后付费-上报业务量':
            self.send_keys(css='.fee-rate>input:nth-child(2)', input_text=code)
            self.send_keys(css='.fee-rate>input:nth-child(4)', input_text=charge_unit)
            self.send_keys(css='.fee-rate>input:nth-child(6)', input_text=unit_price)

        # 点击确定
        self.click_element(css='.add-one-submit-btn-div>.btn')

    # 获取最近创建的一条业务规则
    def get_added_rules(self):
        # 点击业务规则
        self.click_element(css='[href="#/svcrule"]')
        # 查找到第一条item信息
        first_item = self.find_element(css='.result-list-item:nth-child(1)')
        css_words = ['.field:nth-child(1) .field-value', '.field:nth-child(2) .field-value',
                     '.field-value div:nth-child(1) .field-value', '.field-value div:nth-child(2) .field-value',
                     '.sub-field-value',
                     '.sub-field-value:nth-child(2)',
                     '.sub-field-value:nth-child(3)'
                     ]

        # act_rules_info = [self.find_element(css=one).text for one in css_words]
        act_rules_info = []
        # 在第一条信息中查找css_words的所有元素
        for one in css_words:
            try:
                res = first_item.find_element(By.CSS_SELECTOR, one).text
                # res = self.find_element(css=one).text
                if '：' not in res:
                    act_rules_info.append(res)
                else:
                    res_split = res.split('：')[1].strip()
                    act_rules_info.append(res_split)
            except NoSuchElementException:
                act_rules_info.append('')
                continue
        return act_rules_info

    # 删除设置的规则
    def delete_rule(self):
        # 点击业务规则
        self.click_element(css='[href="#/svcrule"]')
        # 点击删除按钮
        self.click_element(css='.result-list-item-btn-bar span')
        self.wb.switch_to.alert.accept()

    def add_device(self, device_type, device_model, rule_id, device_id):
        # 点击设备栏
        self.click_element(css='[href="#/device"]')
        # 点击添加按钮
        self.click_element(css='.add-one-area .btn')
        # 选择设备类型
        self.select_tag(select_id='#device-type', select_word=device_type)
        # 选择设备型号
        self.select_tag(select_id='#device-model', select_word=device_model)
        # 选择业务规则
        self.select_tag(select_id='#svc-rule-id', select_word=rule_id)
        # 输入业务编号
        self.send_keys(css='#device-sn',input_text=device_id)
        # 点击确认按钮，完成添加
        self.click_element(css='.add-one-submit-btn-div .btn')

    def get_added_device(self):
        # 点击设备栏
        self.click_element(css='[href="#/device"]')
        # 找到第一条item
        item_values = [one.text for one in admin.find_elements(css='.result-list-item:nth-child(1) .field-value')]
        item_values.pop(3)
        return item_values

    def delete_added_device(self):
        # 点击设备栏
        self.click_element(css='[href="#/device"]')
        # 点击删除按钮
        self.click_element(css='.result-list-item:nth-child(1) .btn-no-border')
        # 点击系统确认按钮
        self.wb.switch_to.alert.accept()

    # 选择标签
    # select的ID：select_id
    # 选项的text：select_word
    def select_tag(self, select_id, select_word):
        select = Select(self.find_element(css=select_id))
        select.select_by_visible_text(text=select_word)

    # 关闭网页
    def close_wb(self):
        self.wb.close()


admin = admin()
