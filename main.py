import uvicorn

from fastapi import FastAPI, APIRouter

from src.handlers.user_handlers import data_router

app = FastAPI()
main_router = APIRouter()

main_router.include_router(data_router, prefix='/data', tags=['data'])
app.include_router(main_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
