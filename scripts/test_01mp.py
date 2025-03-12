import pytest

import api
from api.api_mp import ApiMp
from tool.read_yaml import read_yaml
from tool.tool import Tool
from tool.get_log import GetLog

log = GetLog.get_logger()


class TestMp:
    # 1. 初始化
    def setup_class(self):
        self.mp = ApiMp()

    # 2. 登录接口测试方法
    @pytest.mark.parametrize("mobile, code", read_yaml("mp_login.yaml"))
    def test_01mp_login(self, mobile, code):
        # 调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        # 打印输出结果
        print("登录的结果为：", r.json())
        try:
            # 提取token
            Tool.common_token(r)
            # 断言
            Tool.common_assert(r)
        except Exception as e:
            # 写日志
            log.error(e)
            # 抛异常
            raise

    # 发布文章测试接口方法
    def test_02mp_article(self, title="test_interface_001", content="1234114141", channel_id="7"):
        # 1. 调用发布文章接口
        r = self.mp.api_mp_article(title, content, channel_id)
        # 2. 提取id
        print(r)
        api.article_id = r.json().get("data").get("id")
        print("发布文章成功后的id值为：", api.article_id)
        # 3. 断言
        Tool.common_assert(r)
