"""
发送请求
"""
import requests

# 接口地址是("http://www.baidu.com")
# 发送一个get请求，r是收到的响应
r = requests.get("http://www.baidu.com")
# 文本格式响应内容
print(r.text)
# 响应码
print(r.status_code)
assert r.status_code == 200
# ok
print(r.reason)
assert r.reason == 'OK'

# http://jy001:8081/futureloan/mvc/api/list
s = requests.get("http://jy001:8081/futureloan/mvc/api/member/list")
# print(s.text)
# print(s.json()["status"])
# print(s.json()['code'])
# 检查结果
assert s.status_code == 200
assert s.reason == 'OK'
assert s.json()["status"] == 1
assert s.json()['code'] == '10001'

# get请求带参数
# 方法一；拼接到ulr后面
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=180993310287&pwd=123456&hellword!"
t = requests.get(url)
print(t.text)

assert t.json()["status"] == 0
assert t.json()['code'] == '20109'
assert t.json()['msg'] == '手机号码格式不正确'
# 方法二；使用params传参数
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {'mobilephone': '', 'pwd': '123456', 'regname': ""}
r = requests.get(url, params=canshu)
print(r.text)
assert r.json()['status'] == 0
assert r.json()['code'] == "20103"

# get请求带请求头,设置User-Agent伪装成浏览器发送请求，避免服务器屏蔽自动化发送的请求
url = "http://www.httpbin.org/get?mobilephone=180993310287&pwd=123456&hellword!"  # 一个测试网站，get是接口名
r = requests.get(url)
print(r.text)
# User-Agent 包含浏览器的版本号，操作系统的版本号等信息
tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.102 Safari/537.36"}
r = requests.get(url, headers=tou)
print(r.text)
url = 'https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html'
r = requests.get(url, headers=tou)
print(r.text)
print('蜂群算法源代码' in r.text)
