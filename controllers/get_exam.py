import json
from functions.summarizer import summarize_from_json_input
from functions.material_parser import parse_multiple_pdfs
from functions.generator import interactive_question_generation

def get_exam_questions(pdfs, detail_level="medium"):
    
    parsed = parse_multiple_pdfs(pdfs)
    
    summarized = summarize_from_json_input(parsed, detail_level=detail_level)

    question_data = interactive_question_generation(summarized)

    return question_data
