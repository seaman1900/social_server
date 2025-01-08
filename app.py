import uvicorn
from fastapi import FastAPI
from routers.router_user import router as user_router

app = FastAPI()

# 挂载路由
app.include_router(user_router)

# 根路由
@app.get("/")
async def root():
    return {"message": "Welcome to Blue Print!"}

# uvicorn app:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)