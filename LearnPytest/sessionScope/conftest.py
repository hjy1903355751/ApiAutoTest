"""
conftest.py session级别的fixture放到这个文件中，文件名字不能写错
第一次调用这个fixture执行前置，目录下所有文件执行完再执行后置
conftest.py文件作用域，对同级目录以及子目录生效
一个工程中可以有多个conftest.py文件
"""

import pytest


# 测试前置
@pytest.fixture(scope='session')
def login():
    print("系统登陆")  # yield之前的前置
    yield
    print("退出登录")  # yield之后的前置
