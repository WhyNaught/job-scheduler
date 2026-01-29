from fastapi import FastAPI
import uvicorn 

app = FastAPI()

from controllers.user_controller import router as userRouter 
from controllers.job_controller import router as jobRouter

app.include_router(userRouter)
app.include_router(jobRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)