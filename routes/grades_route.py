from fastapi import APIRouter, HTTPException
from controllers.get_grades import get_grades

router = APIRouter()

@router.post("/grades")
async def get_grades_route():
    try:
        image_path = "controllers/exam.jpg"  # Hardcoded path for now
        grades = get_grades(image_path)
        
        if grades is None:
            raise HTTPException(status_code=404, detail="Grades not found")
        
        return {"grades": grades}  # Or return JSONResponse(content=grades) if needed.
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
