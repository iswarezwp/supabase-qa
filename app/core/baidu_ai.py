# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
import os
import requests
import json
import time
from typing import Dict, List, Any

# 百度文心千帆 API接口
# https://cloud.baidu.com/doc/WENXINWORKSHOP/s/flfmc9do2
# https://cloud.baidu.com/doc/WENXINWORKSHOP/s/4lilb2lpf

class BaiduAI(object):
    def __init__(self) -> None:
        self.model = os.getenv('BAIDU_MODEL')
        self.access_token = None
        self.access_token_expires_time = 0
        super().__init__()

    def get_access_token(self):
        if self.access_token is not None and time.time() < self.access_token_expires_time:
            return self.access_token

        api_key = os.getenv('BAIDU_API_KEY')
        api_secret = os.getenv('BAIDU_API_SECRET')

        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={api_secret}"

        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        self.access_token = response.json().get("access_token")
        return self.access_token

    def ask_baidu(self, messages: List[Dict[str, Any]]):
        if self.model == 'ERNIE-Bot-turbo':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + self.get_access_token()
        elif self.model == 'ERNIE-Bot':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + self.get_access_token()
        elif self.model == 'BLOOMZ-7B':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/bloomz_7b1?access_token=" + self.get_access_token()

        payload = json.dumps({
            "messages": messages
        })
        headers = {
            'Content-Type': 'application/json'
        }

        return requests.request("POST", url, headers=headers, data=payload).json()

