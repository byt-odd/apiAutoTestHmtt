import requests as requests
import api
from tool.get_log import GetLog
log = GetLog.get_logger()

class ApiMp:
    # 1. 初始化
    def __init__(self):
        # 1. 登录接口url
        # self.url_login = api.host+"#/login"
        self.url_login = "https://api-toutiao-web.itheima.net/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url：{}".format(self.url_login))
        # 2. 发布文章接口
        # self.url_article = api.host+"/article/publish"
        self.url_article = "https://api-toutiao-web.itheima.net/mp/v1_0/articles?draft=false"
        log.info("正在初始化自媒体发布文章url：{}".format(self.url_article))
    # 2. 登录接口
    def api_mp_login(self,mobile,code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 1. 定义请求数据
        data = {"mobile":mobile,"code":code}
        log.info("正在调用自媒体登录接口，请求数据为：{}".format(data))
        # 2. 调用post方法
        return requests.post(url=self.url_login,json=data,headers=api.headers)
    # 3. 发布文章接口
    def api_mp_article(self,title,content,channel_id):
        """
        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道id
        :param cover: 封面 0:为自动
        :return: 响应对象
        """
        # 1. 定义请求数据
        data = {"title":title,"content":content,"channel_id":channel_id,"cover":{"type":0,"images":[]}}
        log.info("正在调用发布文章接口，请求数据为：{}".format(data))
        # 2. 调用post方法
        return requests.post(url=self.url_article,json=data,headers=api.headers)