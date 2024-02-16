import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from mangum import Mangum
from app.api.v1.router import api_router

#API definition
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

lambda_handler=Mangum(app)

@app.get("/",tags=["Home Page"])
def home():
    return {"Welcome": "Welcome to the CI CD Testing FastAPI"}


app.include_router(api_router, prefix="/api")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=10052)