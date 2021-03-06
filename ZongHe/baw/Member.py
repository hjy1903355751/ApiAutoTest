'''
用户模块的接口（注册、登录、充值、用户列表、取现...）
'''


def register(url, baserequests, data):
    '''
    发送注册接口
    :param url: http://jy001:8081/,从环境文件中读取
    :param baserequests: 是BaseRequests的一个实例
    :param data:注册接口的参数
    :return:响应信息
    '''

    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url, data=data)
    return r


def login(url,baserequests, data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r



def getList(url, baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.post(url)
    return r


# 测试代码，用完可以删除
if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BasaRequests

    baserequests = BasaRequests()
    canshu = {"mobilephone": 18012345678, "pwd": 123456}
    r = register("http://jy001:8081/", baserequests, canshu)
    print(r.text)
