from api.api_app import ApiApp
from tool.tool import Tool


class TestApp:
    # 1. 初始化
    def setup_class(self):
        # 获取ApiApp对象
        self.app = ApiApp()

    # 2. 登录测试接口
    def test_01app_login(self,email="byt825990802@163.com",pwd="zxcvbnmBYT821"):
        # 1. 调用登录接口
        r=self.app.api_app_login(email,pwd)
        print("登录的结果为：",r.text())
        # print("登录的结果为：", r.json())
        # 2. 提取token
        # Tool.common_token(r)
        # 3. 断言
        # Tool.common_assert(r,status_code=200)

    def test_02app_article(self):
        pass