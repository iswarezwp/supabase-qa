# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from postgrest.exceptions import APIError
from openai import OpenAIError

from api import v1_router
from repositories.kb import get_kb_repo

# 加载数据到知识库
kb_repo = get_kb_repo()
kb_repo.load_dir(os.getenv("DOCS_PATH"))

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")
app.mount('/', StaticFiles(directory='www', html=True), name='static')


@app.exception_handler(OpenAIError)
async def openai_exception_handler(request: Request, exc: OpenAIError):
    return JSONResponse(
        status_code=exc.http_status,
        content={'code': exc.code, 'message': exc.error},
    )
