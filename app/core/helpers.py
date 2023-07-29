# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
import os

DEFAULT_QA_BACKEND='openai'

def get_qa_backend() -> str:
    return os.getenv('QA_BACKEND', DEFAULT_QA_BACKEND)
