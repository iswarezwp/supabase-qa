## 准备工作
- 在[MemFire Cloud](https://memfiredb.com)上创建应用，后面需要用到应用的API URL和Service Role Key。
可以在应用的`应用设置`->`API`页面找到响应的配置

- 创建应用后，在应用的`SQL执行器`页面执行如下脚本
```sql
-- Enable the pgvector extension to work with embedding vectors
create extension vector;

-- Create a table to store your documents
create table documents (
    id uuid primary key,
    content text, -- corresponds to Document.pageContent
    metadata jsonb, -- corresponds to Document.metadata
    embedding vector(1536) -- 1536 works for OpenAI embeddings, change if needed
);

CREATE FUNCTION match_documents(query_embedding vector(1536), match_count int)
   RETURNS TABLE(
       id uuid,
       content text,
       metadata jsonb,
       -- we return matched vectors to enable maximal marginal relevance searches
       embedding vector(1536),
       similarity float)
   LANGUAGE plpgsql
   AS $$
   # variable_conflict use_column
BEGIN
   RETURN query
   SELECT
       id,
       content,
       metadata,
       embedding,
       1 -(documents.embedding <=> query_embedding) AS similarity
   FROM
       documents
   ORDER BY
       documents.embedding <=> query_embedding
   LIMIT match_count;
END;
$$;
```

## 如何运行
### linux 下运行
1. 安装依赖
```bash
pip install -r app/requirements.txt
```

2. 设置参数
```bash
export DOCS_PATH=./docs
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
    -v ./docs:/docs \
    memfirecloud-qa:v1
```

### windows下运行（没测试）
与linux类似，设置相关环境变量，然后运行:
```bash
uvicorn main:app --reload --host 0.0.0.0
```

## 参数配置支持
```bash
# 本地文档路径
export DOCS_PATH=./docs

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
