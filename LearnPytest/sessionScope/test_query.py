class TestQuery():
    def test_case1(self):
        print("测试查询")

    def test_case2(self, login):  # 执行前置
        print("测试查询2")

    def test_case3(self):  # 执行后置
        print("测试查询3")