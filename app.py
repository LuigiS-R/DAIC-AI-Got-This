from fastapi import FastAPI
from routes.grades_route import router as grades_router
from routes.exam_route import router as exam_router

app = FastAPI()

app.include_router(grades_router)  # Register the router
app.include_router(exam_router)  # Register the router

@app.get("/")
def root():
    return {"message": "API is running"}
