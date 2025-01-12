import uvicorn
from fastapi import FastAPI
from routers.router_user import router as user_router
from routers.router_invest import router as invest_router
from routers.router_print import router as print_router
from routers.router_comment import router as comment_router
from routers.router_balance import router as balance_router
from routers.router_transaction import router as transaction_router

app = FastAPI()

# 挂载路由
app.include_router(user_router)
app.include_router(print_router)
app.include_router(invest_router)
app.include_router(comment_router)
app.include_router(balance_router)
app.include_router(transaction_router)

# 根路由
@app.get("/")
async def root():
    return {"message": "Welcome to Blue Print!"}

# uvicorn app:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True, workers=1)