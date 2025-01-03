from fastapi import FastAPI

#실행
#python -m uvicorn main:app --host 172.16.20.209 --port 81

# FastAPI 애플리케이션 생성
app = FastAPI()

from llm.RAG_LLM import getAnswer
from dto import *

# /getInfo 경로에 대한 GET 요청 처리
@app.get("/getInfo")
async def get_info():
    # 반환할 JSON 데이터
    return {
        "status": "success",
        "message": "This is your JSON response!",
        "data": "Defying Gravity"
    }

@app.post("/chat" , response_model=QueryResponse)
async def chat(request: QueryRequest):
    print(request.query)
    user_query = request.query
    answer = getAnswer(user_query)
    return QueryResponse(query=user_query, answer=answer)
    # print("hi")

