from fastapi import APIRouter, HTTPException
from controllers.get_grades import get_grades

router = APIRouter()

@router.post("/grades")
async def get_grades_route():
    try:
        image_path = "controllers/exam.jpg"
        model_answer_file = "functions/answer.pdf"
        grades = get_grades(image_path, model_answer_file)

        if grades is None:
            raise HTTPException(status_code=404, detail="Grades not found")
        
        return {"grades": grades}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
