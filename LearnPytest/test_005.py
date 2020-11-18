"""
fixture 可以带参数和返回值
"""
import pytest


# 测试前置：准备测试数据，在测试用例中使用测试数据，测试数据使用fixture的返回值来表示
@pytest.fixture()
def username_pwd():
    return {'username': "root", "pwd": 123456}


def test_login(username_pwd):
    print(f"测试数据为:", {username_pwd['username']})


# 相同的测试用例，只是每次输入的数据不同
@pytest.fixture(params=['root', 'admin', 'administrator', '123456'])
def data(request):
    return request.param  # request.param 是固定写法，取到每一组数据


@pytest.fixture(params=[
    {'cassedata': 'root', 'expect': "成功"},
    {'cassedata': 'admin', 'expect': "成功"}])  # 多组测试数据
def data1(request):  # request是固定写法
    return request.param  # request.param 是固定写法，取到每一组数据


def test_login2(data):
    print(f"使用户名{data}测试登录功能")


def test_login3(data1):
    print(f"使用户名{data1['cassedata']}测试登录功能,预期结果为{data1['expect']}")
