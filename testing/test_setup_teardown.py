# 模块级别，模块始末，全局的
def setup_module():
    print('setup_module:调用模块前执行')


def teardown_module():
    print('setup_module:调用模块后执行')


def test_a():
    print('执行时调模块的方法')


# 函数级别，只对函数用例生效
def setup_function():
    print('setup_function:函数执行前')


def teardown_function():
    print('teardown_function:函数执行后')


def test_b():
    print('执行函数的测试方法')


class TestDemo:
    # 类级别，在类中前后运行一次
    def setup_class(self):
        print('setup_class:类前执行前1')

    def teardown_class(self):
        print('teardown_class:类后执行后1')

    # 方法级别，开始于方法始末
    def setup_method(self):
        print('setup_method:方法执行前2')

    def teardown_method(self):
        print('teardown_method:方法执行后2')

    # 运行在调方法的前后
    def setup(self):
        print('setup:运行在调方法前3')

    def teardown(self):
        print('teardown:运行在调方法后3')

    def test_c(self):
        print('执行类中的测试方法')
