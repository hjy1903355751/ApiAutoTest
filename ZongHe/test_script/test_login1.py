"""
测试登录功能
"""
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_data.yaml"))
def login_data(request):
    return request.param


@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_setup.yaml"))
def setup_data(request):
    return request.param


# 测试前置和后置
@pytest.fixture()
def register(setup_data, url, baserequestes, db):
    # 注册
    phone = setup_data["casedata"]["mobilephone"]
    # 初始化环境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # 发送请求
    Member.register(url, baserequestes, setup_data['casedata'])
    yield
    # 删除用户
    DbOp.deleteUser(db, phone)


def test_login(register, login_data, url, baserequestes):
    # 登录
    # 检查登录结果
    # 发送请求
    r = Member.login(url, baserequestes, login_data['casedata'])
    print(r.text)
    assert str(r.json()['msg']) == str(login_data['expect']['msg'])
