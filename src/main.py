from fastapi import FastAPI

app = FastAPI()

from src.controllers.user_controller import router as userRouter 

app.include_router(userRouter)