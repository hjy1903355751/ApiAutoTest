"""
测试的测试脚本（pytest）
"""
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


# 测试前置：获取测试数据，数据是列表，通过readyaml读取来的
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def file_data(request):  # 固定写法
    return request.param
# 注册失败
def test_register_fail(file_data, url, baserequestes):
    print(f"测试数据:{file_data['casedata']}")
    print(f"预期结果:{file_data['expect']}")
    # 发送请求
    r = Member.register(url, baserequestes, file_data['casedata'])
    print(r.text)
    # 检查结果
    assert str(r.json()['msg']) == str(file_data['expect']['msg'])
    assert str(r.json()['code']) == str(file_data['expect']['code'])
    assert str(r.json()['status']) == str(file_data['expect']['status'])


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_pass.yaml"))
def pass_data(request):  # 固定写法
    return request.param
# 注册成功
def test_register_pass(pass_data, url, db, baserequestes):
    print(f"测试数据:{pass_data['casedata']}")
    print(f"预期结果:{pass_data['expect']}")
    phone = pass_data["casedata"]["mobilephone"]
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequestes, pass_data['casedata'])
    # 检查响应结果
    assert str(r.json()['msg']) == str(pass_data['expect']['msg'])
    assert str(r.json()['code']) == str(pass_data['expect']['code'])
    assert str(r.json()['status']) == str(pass_data['expect']['status'])
    r = Member.getList(url, baserequestes)
    assert phone in r.text
    # 清理环境，根据手机号清除注册用户
    DbOp.deleteUser(db, phone)





@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def repeat_data(request):  # 固定写法
    return request.param
# 重复注册
def test_register_repeat(repeat_data, url, db, baserequestes):
    print(f"测试数据:{repeat_data['casedata']}")
    print(f"预期结果:{repeat_data['expect']}")
    phone = repeat_data["casedata"]["mobilephone"]
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # # # 发送请求
    r = Member.register(url, baserequestes, repeat_data['casedata'])
    # 检查结果
    assert str(r.json()['msg']) == str(repeat_data['expect']['msg'])
    assert str(r.json()['code']) == str(repeat_data['expect']['code'])
    assert str(r.json()['status']) == str(repeat_data['expect']['status'])
    r1 = Member.register(url, baserequestes, repeat_data['casedata'])
    assert str(r1.json()['msg']) == '手机号码已被注册'
