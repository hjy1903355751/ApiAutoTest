import mock
import requests


class QuXian:
    def quxians(self, data):
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data).json()
        return r

class TestQuXian:
    def test_quxian(self):
        quxian = QuXian()
        quxian.quxians = mock.Mock(return_value={"status":"0","code":"20109","msg":"手机格式不正确"})
        data = {"mobilephone":"1581111001","amount":"100"}
        expect = {"status": 0, "code": "20109","msg": "手机格式不正确"}
        real = quxian.quxians(data)
        print(real)
        assert real['code'] == expect['code']
        assert real['msg'] == expect['msg']