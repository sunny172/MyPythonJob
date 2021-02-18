## 项目介绍
Pytest练习作业
## Fixture作用
- Fixture是在测试函数运行前后，由pytest执行的外壳函数，代码可以定制，满足多变的测试需求，功能包括：
    - 定义传入测试中的数据集
    - 配置测试前系统的初始状态
    - 为批量测试提供数据源等
- Fixture 是pytest 用于将测试前后进行预备，清理工作的代码分离出核心测试逻辑的一种机制
## Fixture 用法
- Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法
    1. 类似 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活
    2. 直接通过函数名字调⽤或使用装饰器@pytest.mark.usefixtures(‘test1’)
    3. 允许使用多个Fixture
    4. 使用 autouse 自动应用，如果要返回值，需要传fixture函数名
    5. 作用域（session>module>class>function）
    6. 也可以提供测试数据，实现参数化的功能
    7. Fixture也可以调用Fixture
    8. -setup-show 回溯 fixture 的执行过程
## conftest.py 用法
- 数据共享的文件，名字是固定的，不能修改
- 可以存放fixture , hook 函数
- 就近生效（如果不在同一个文件夹下，离测试文件最近的conftest.py 生效）
- 当前目录一定要有__init__.py 文件，也就是要创建一个包