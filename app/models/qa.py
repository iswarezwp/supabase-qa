# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
from pydantic import BaseModel
from typing import Union


class QaRequest(BaseModel):
    question: str

class QaResponse(BaseModel):
    result: str
