# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
import logging
from typing import List
from .qa_base import BaseQARepository
from core import baiduai


# 百度文心千帆 API接口
# https://cloud.baidu.com/doc/WENXINWORKSHOP/s/flfmc9do2
# https://cloud.baidu.com/doc/WENXINWORKSHOP/s/4lilb2lpf
class BaiduQARepository(BaseQARepository):
    prompt = "请根据提供的信息回答问题，请不要回答提供内容之外的问题。"

    def __init__(self) -> None:
        super().__init__()

    '''
    百度的接口要求
    （1）messages成员不能为空，1个成员表示单轮对话，多个成员表示多轮对话
    （2）最后一个message为当前请求的信息，前面的message为历史对话信息
    （3）必须为奇数个成员，成员中message的role必须依次为user、assistant
    （4）最后一个message的content长度（即此轮对话的问题）不能超过2000个字符；如果messages中content总长度大于2000字符，系统会依次遗忘最早的历史会话，直到content的总长度不超过2000个字符
    '''
    def ask(self, question: str, matched_docs: List[any]) -> str:
        # baidu的接口要求必须先问后答，所以需要把提示信息和问题全部放在一起
        docs = '\n'.join([doc.page_content for doc in matched_docs])
        messages=[
            {"role": "user", "content": f"{self.prompt}\n文章: {docs}\n问题: {question}"},
        ]

        response = baiduai.ask_baidu(messages)
        if 'error_msg' in response:
            return response['error_msg']

        logging.info(f"tokens: {response['usage']}")

        return response['result']
