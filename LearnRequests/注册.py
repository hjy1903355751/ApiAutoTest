"""
登录接口测试用例
"""
import requests
import pytest


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


@pytest.fixture(params=[
    {"data": {"mobilephone": "18012345%$", "pwd": 123456, "regname": "hello"},
     "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
    {"data": {"mobilephone": "", "pwd": 123456, "regname": "hello"},
     "expect": {"status": 0, "code": "20103", "data": "None", "msg": "手机号码不能为空"}},
    {"data": {"mobilephone": "180123456789", "pwd": 123456, "regname": "hello"},
     "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
    {"data": {"mobilephone": "1801234", "pwd": 123456, "regname": "hello"},
     "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
    {"data": {"mobilephone": "180123X568", "pwd": 123456, "regname": "hello"},
     "expect": {"status": 0, "code": "20109", "data": "None", "msg": "手机号码格式不正确"}},
    {"data": {"mobilephone": "13745241111", "pwd": '123456abc', "regname": "hello"},
     "expect": {"status": 0, "code": "20110", "data": "None", "msg": "手"}}
])
def register_data(request):  # request是固定写法
    return request.param  # request.param 是固定写法，取到每一组数据


def test_register(register_data):
    real = register(register_data['data'])
    print(real.text)
    assert real.json()['msg'] == register_data['expect']['msg']
    assert real.json()['code'] == register_data['expect']['code']

# def test_login4(data2):
#     print(f"使用手机号码{data2['casedata']}测试注册功能,预期结果为{data2['expect']}")
