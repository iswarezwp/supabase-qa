# -*- coding: utf-8 -*-
"""
Copyright (c) 2023, Nimblex Co .,Ltd.

@author: zhangwenping
"""
import logging
import os
from supabase import create_client, Client


url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
log_level: str = os.environ.get("LOG_LEVEL", "INFO")

logging.basicConfig(level=log_level)
client: Client = create_client(url, key)
