from .kb_base import KBRepository
from .memfire import MemFireKBRepository

memfire = MemFireKBRepository()

def get_kb_repo() -> KBRepository:
    return memfire
