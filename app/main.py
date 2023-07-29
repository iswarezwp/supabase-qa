# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from postgrest.exceptions import APIError
from openai import OpenAIError

from api import v1_router

app = FastAPI()

app.include_router(v1_router, prefix="/api/v1")
app.mount('/', StaticFiles(directory='www', html=True), name='static')


@app.exception_handler(OpenAIError)
async def openai_exception_handler(request: Request, exc: OpenAIError):
    return JSONResponse(
        status_code=exc.http_status,
        content={'code': exc.code, 'message': exc.error},
    )
