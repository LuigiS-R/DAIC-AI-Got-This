from fastapi import APIRouter, HTTPException
from controllers.get_exam import get_exam_questions
import os

router = APIRouter()

@router.post("/exam")
async def get_exam_route():
    """
    Hardcoded route for generating exam questions from predefined PDFs.
    
    Returns:
        dict: A dictionary with the generated questions.
    """
    try:
        # Hardcoded paths to existing PDFs
        file_paths = [
            "test_files/Investments_CH7.pdf",
            "test_files/Investments_CH8.pdf",
            "test_files/Investments_CH10.pdf"
        ]

        # Hardcoded detail level
        detail_level = 'short'

        # Call the exam question generator
        questions = get_exam_questions(file_paths, detail_level)

        # Optionally clean up the files after processing
        for file_path in file_paths:
            if os.path.exists(file_path):
                os.remove(file_path)

        return {"questions": questions}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
