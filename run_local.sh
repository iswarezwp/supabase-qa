export SUPABASE_URL="your-api-url"
export SUPABASE_KEY="your-service-role-key"

export OPENAI_API_KEY="your-openai-api-key"

cd app && uvicorn main:app --reload --host 0.0.0.0
