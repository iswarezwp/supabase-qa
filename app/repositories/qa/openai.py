# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
Created on 2023-07-19 17:50
"""
import os
import logging
import openai
from typing import List
from .qa_base import BaseQARepository


# openai documents
# https://platform.openai.com/docs/api-reference/completions


class OpenAIQARepository(BaseQARepository):
    prompt = "请根据提供的信息回答问题，请不要回答提供内容之外的问题。请使用中文回答。"

    def __init__(self) -> None:
        openai.organization = os.getenv('OPENAI_ORGANIZATION')
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
        super().__init__()

    def ask(self, question: str, matched_docs: List[str]) -> str:
        docs = '\n'.join([doc.page_content for doc in matched_docs])
        messages = [
            {"role": "system", "content": self.prompt},
            {"role": "user", "content": f"文章: {docs}\n问题: {question}"},
        ]

        response = openai.ChatCompletion.create(model=self.model, messages=messages, timeout=60)

        logging.info(f"tokens: {response['usage']}")
        return response['choices'][0]['message']['content']
