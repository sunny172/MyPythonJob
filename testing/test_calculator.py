import sys
import pytest
import yaml

# 退回到项目根目录便于命令行运行项目
sys.path.append('..')
# print(sys.path)

from pythoncode.Calculator import Calculator


# 获取yaml文件参数
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    return (datas['add']['datas'], datas['add']['ids'], datas['div']['datas'])


# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("计算结束")

    # 装饰器
    @pytest.mark.parametrize("a, b, result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("x, y, result", datas[2])
    def test_div(self, x, y, result):
        assert result == self.calc.divider(x, y)
