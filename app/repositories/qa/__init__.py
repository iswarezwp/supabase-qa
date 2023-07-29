import os
from typing import Union
from .qa_base import BaseQARepository
from .baidu import BaiduQARepository
from .openai import OpenAIQARepository

baidu_qa = BaiduQARepository()
openai_qa = OpenAIQARepository()


def get_qa_repo(backend: Union[str, None] = None) -> BaseQARepository:
    if backend is None:
        backend = os.getenv("QA_BACKEND", "openai")

    if backend == "baidu":
        return baidu_qa
    elif backend == "openai":
        return openai_qa

    raise NotImplementedError(f"backend {backend} not supported")
