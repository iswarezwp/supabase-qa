## 如何运行
### linux 下运行
1. 安装依赖
```bash
pip install -r app/requirements.txt
```

2. 设置参数
```bash
export SUPABASE_URL="your-api-url"
export SUPABASE_KEY="your-service-role-key"
export OPENAI_API_KEY="your-openai-api-key"
```

3. 运行
```bash
uvicorn main:app --reload --host 0.0.0.0
```

### docker运行
```
docker build -t memfirecloud-qa:v1 .

docker run -p 8000:80 \
    -e SUPABASE_URL="your-api-url" \
    -e SUPABASE_KEY="your-service-role-key" \
    -e OPENAI_API_KEY="your-openai-api-key" \
    memfirecloud-qa:v1
```

### windows下运行（没测试）
与linux类似，设置相关环境变量，然后运行:
```bash
uvicorn main:app --reload --host 0.0.0.0
```

## 参数配置支持
```bash
# memfire cloud 应用的API URL和Service role key
export SUPABASE_URL="your-api-url"
export SUPABASE_KEY="your-service-role-key"

# 使用openai / baidu 的大模型
export QA_BACKEND="openai" # 默认值

# openai 相关配置（QA_BACKEND=openai是需要）
export OPENAI_ORGANIZATION="your-openai-organization"
export OPENAI_API_KEY="your-openai-api-key"
export OPENAI_MODEL="gpt-3.5-turbo"  # 默认值

# 百度相关配置（QA_BACKEND=baidu时需要）
export BAIDU_API_KEY="your-baidu-api-key"
export BAIDU_API_SECRET="your-baidu-api-secret"
export BAIDU_MODEL="ERNIE-Bot-turbo" # 默认值
```

## TODOS
- [ ] 不重复处理文档
- [ ] 程序运行中增量添加新文档
- [ ] 支持对话（目前只是QA）
- [ ] 支持文心一言
