from fastapi import FastAPI
from routes.grades_route import router

app = FastAPI()

app.include_router(router)  # Register the router

@app.get("/")
def root():
    return {"message": "API is running"}
