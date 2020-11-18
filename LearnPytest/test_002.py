"""
测试前置和后置
类和方法级别
1.不够灵活，
"""

class Test002:

    def setup_class(self):
        print("测试前置:类的方法执行前调用")

    def teardown_class(self):
        print("测试后置:类的方法执行后调用")

    def setup_method(self):
        print("每一个方法前执行")

    def teardown_method(self):
        print("每个方法后执行")

    def test_001(self):
        print("用例一")

    def test_002(self):
        print("用例2")
