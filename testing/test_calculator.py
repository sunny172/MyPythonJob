import sys

import allure
import pytest
import yaml

# 退回到项目根目录便于命令行运行项目
sys.path.append('..')
# print(sys.path)
from pythoncode.Calculator import Calculator


# 获取yaml文件参数
def get_datas(name):
    with open("./datas/calc.yml", encoding='utf-8') as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name]['datas']
    ids = all_datas[name]['ids']
    return (datas, ids)


# # 提供对象
# @pytest.fixture()
# def get_instance():
#     print("开始计算")
#     calc = Calculator()
#     yield calc
#     print("结束计算")

# 提供加法参数的fixture
@pytest.fixture(params=get_datas('add')[0], ids=get_datas('add')[1])
def get_add_datas_fixture(request):
    return request.param


# 提供除法参数的fixture
@pytest.fixture(params=get_datas('div')[0], ids=get_datas('div')[1])
def get_div_datas_fixture(request):
    return request.param


# 测试类
@allure.feature("计算器")
class TestCalc:
    # add_int_data = get_datas('add')
    # div_int_data = get_datas('div')

    # # 前置条件
    # def setup_class(self):
    #     print("开始计算")
    #     self.calc = Calculator()
    #
    # # 后置条件
    # def teardown_class(self):
    #     print("计算结束")

    # 装饰器
    # @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    # def test_add(self, get_instance, a, b, result):
    #     assert result == round(get_instance.add(a, b), 2)
    @allure.story("相加功能")
    def test_add(self, get_instance, get_add_datas_fixture):
        f = get_add_datas_fixture
        assert f[2] == round(get_instance.add(f[0], f[1]), 2)

    # @pytest.mark.parametrize("x, y, result", div_int_data[0], ids=div_int_data[1])
    # def test_div(self, get_instance, x, y, result):
    #     if y == 0:
    #         with pytest.raises(ZeroDivisionError):
    #             assert result == get_instance.divider(x, y)
    #     else:
    #         assert result == get_instance.divider(x, y)
    @allure.story("相除功能")
    def test_div(self, get_instance, get_div_datas_fixture):
        d = get_div_datas_fixture
        if d[1] == 0:
            with pytest.raises(ZeroDivisionError):
                print(f'{d[0]} / {d[1]}', '=', f'{d[2]}')
                assert d[2] == get_instance.divider(d[0], d[1])
        else:
            print(f'{d[0]} / {d[1]}', '=', f'{d[2]}')
            assert d[2] == get_instance.divider(d[0], d[1])
