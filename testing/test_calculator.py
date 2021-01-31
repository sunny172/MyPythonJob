import sys
import pytest
import yaml

# 退回到项目根目录便于命令行运行项目
sys.path.append('..')
# print(sys.path)

from pythoncode.Calculator import Calculator


# 获取yaml文件参数
def get_datas(name):
    with open("./datas/calc.yml") as f:
        all_datas = yaml.safe_load(f)
    datas = all_datas[name]['datas']
    ids = all_datas[name]['ids']
    return (datas, ids)


# 测试类
class TestCalc:
    add_int_data = get_datas('add')
    div_int_data = get_datas('div')

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("计算结束")

    # 装饰器
    @pytest.mark.parametrize("a, b, result", add_int_data[0], ids=add_int_data[1])
    def test_add(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("x, y, result", div_int_data[0], ids=div_int_data[1])
    def test_div(self, x, y, result):
        if y == 0:
            with pytest.raises(ZeroDivisionError):
                assert result == self.calc.divider(x, y)
        else:
            assert result == self.calc.divider(x, y)
