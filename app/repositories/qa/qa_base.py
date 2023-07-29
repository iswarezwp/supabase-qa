# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
from typing import List
from abc import ABC, abstractmethod


class BaseQARepository(ABC):
    @abstractmethod
    def ask(self, question: str, matched_docs: List[any]) -> str:
        raise NotImplementedError()
