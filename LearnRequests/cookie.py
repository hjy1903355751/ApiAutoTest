"""
cookie
"""

import requests

head = {
    "Cookie": 'MEIQIA_TRACK_ID=1juNheLIiykV3rdfmBdU08Qa5M0; __auc=551fe71e1759c99f2254072cb20; _ga=GA1.2.1677469665.1604650141; _gid=GA1.2.1733324507.1604650141; __asc=af1decc8175a1b64a2a70bf31df; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1604654288,1604654349,1604655562,1604735880; MEIQIA_VISIT_ID=1jxBV7BmG4Mq21S01RkEy0WOXJU; BAGSESSIONID=5c9cb14a-f99a-42cb-933a-a7afe82c3bd1; JSESSIONID=F4905A86863D2EFA259A45093D0B5908; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1604735888; _gat=1access_type=1&loginType=1&emailLoginWay=0&account=1903355751%40qq.com&password=chao09070621&imgVerifyCodeByEmailLogin=&remindmeBox=on&remindme=1&cell_phone=&geetest_challenge=&geetest_validate=&geetest_seccode=&sms_code=&returnPage='}
r = requests.get("https://www.bagevent.com/account/dashboar", headers=head)
print(r.text)
s = requests.session()  # 创建了一个session，通过session发送请求
print("登录之前的cookies", s.cookies)
'''
:returns中自动管理cookies机制
'''
canshu = {
    "access_type": 1,
    "loginType": 1,
    "emailLoginWay": 0,
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindeBox": "on",
    "remindem": 1
}

r = s.post("https://www.bagevent.com/user/login", data=canshu)
print("登录之后的cookies", s.cookies)
# print(r.text)
r = s.get("https://www.bagevent.com/account/dashboard")
print("<title>百格活动 - 账户总览</title>" in r.text)

# 获取调查列表
s.get("https://www.bagevent.com/account/myevents?published=1")
print(r.text)
# 查看某个调查详细信息
