# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
from pydoc import doc
from fastapi import APIRouter
from models.qa import QaRequest, QaResponse
from repositories.qa import get_qa_repo, BaseQARepository
from repositories.kb import get_kb_repo, KBRepository

router = APIRouter()

@router.post("/ask", response_model=QaResponse)
def answer_question(req: QaRequest):
    kb_repo: KBRepository= get_kb_repo()
    docs = kb_repo.search_docs(req.question)

    qa_repo: BaseQARepository = get_qa_repo()
    result = qa_repo.ask(req.question, docs)

    return {"result": result}
