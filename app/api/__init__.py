import imp
from fastapi import APIRouter
from .v1 import qa

v1_router = APIRouter()

v1_router.include_router(qa.router, prefix="/qa", tags=["qa"])
