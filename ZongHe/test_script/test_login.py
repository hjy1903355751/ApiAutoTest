'''
登录测试脚本
'''
import pytest

from ZongHe.baw import Member
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param
# 登录成功
def test_login_pass(pass_data, url, baserequestes):
    print(f"测试数据:{pass_data['casedata']}")
    print(f"预期结果:{pass_data['expect']}")
    # 发送请求
    r = Member.login(url, baserequestes, pass_data['casedata'])
    # 检查响应结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])




# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
def file_data(request):  # 固定写法
    return request.param
# 登录失败
def test_login_fail(file_data, url, baserequestes):
    print(f"测试数据:{file_data['casedata']}")
    print(f"预期结果:{file_data['expect']}")
    # 发送请求
    r = Member.login(url, baserequestes, file_data['casedata'])
    print(r.text)
    # 检查结果
    assert str(r.json()['msg']) == str(file_data['expect']['msg'])
    assert str(r.json()['code']) == str(file_data['expect']['code'])
    assert str(r.json()['status']) == str(file_data['expect']['status'])