import requests

import api

class ApiApp:
    # 1. 初始化
    def __init__(self):
        # 1. 登录url
        self.url_login = "https://reg.163.com/services/safeUserLoginForMob"
        # 2. 查询url
        self.url_article=""


    # 2. 登录
    def api_app_login(self,email,pwd):
        # 1. 请求参数
        data={"email":email,"pwd":pwd}
        # 2. 调用post方法
        return requests.post(url=self.url_login,json=data,headers=api.header)

    # 3. 查询频道下所有文章
    def api_app_article(self,channel_id):
        # 1. 请求参数
        data={"channelId":channel_id}
        # 2. 调用post方法
        return requests.post(url=self.url_article,json=data,headers=api.header)
