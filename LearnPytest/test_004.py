"""
fixture作用域
默认是function及级的，有function、module、class、session级别
"""

import pytest


# 测试前置
@pytest.fixture(scope='class')  # 每个类调用一次，在类中首次调用fixture这个方法执行前置，类方法执行完执行后置
def login():
    print("系统登陆")  # yield之前的前置
    yield
    print("退出登录")  # yield之后的前置


class TestQuery():
    def test_case1(self):
        print("测试查询")

    def test_case2(self, login):  # 执行前置
        print("测试查询2")

    def test_case3(self):  # 执行后置
        print("测试查询3")


class TestDelete():
    def test_case1(self, login):  # 执行前置
        print("测试删除1")

    def test_case2(self):
        print("测试删除2")

    def test_case3(self):  # 执行后置
        print("测试删除3")
