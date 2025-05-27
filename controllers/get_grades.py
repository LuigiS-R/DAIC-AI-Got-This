from functions.ocr import ocr_image
from functions.student_answer_extractor import extract_answers_from_context_with_solar
from functions.grader import grade_exam
from functions.answer_key_extractor import extract_answers_from_pdf

def get_grades(image_path, model_answer_file):
    with open(image_path, "rb") as f:
        ocr_result = ocr_image(f)
    ocr_text = ocr_result.get("text", "").strip()
    print("OCR: ", ocr_text)

    extracted_answers = extract_answers_from_context_with_solar(ocr_text)

    model_answer_list = extract_answers_from_pdf(model_answer_file)

    model_answers = {
        item["question"]: {"answer": item["answer"], "type": item["type"]}
        for item in model_answer_list
    }

    graded_results = grade_exam(extracted_answers, model_answers)
    return graded_results