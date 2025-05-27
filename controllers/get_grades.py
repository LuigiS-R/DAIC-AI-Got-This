from functions.ocr import ocr_image
from functions.extractor import extract_answers_from_context_with_solar
from functions.grader import grade_exam


def get_grades(image_path):
    with open(image_path, "rb") as f:
        ocr_result = ocr_image(f)

    ocr_text = ocr_result.get("text", "").strip()

    print("OCR: ", ocr_text)

    extracted_answers = extract_answers_from_context_with_solar(ocr_text)

    model_answers = {
    1: {"answer": "B", "type": "mcq"},
    2: {"answer": "B", "type": "mcq"},
    3: {"answer": "B", "type": "mcq"},
    4: {"answer": "12", "type": "numerical"},
    5: {"answer": "7200", "type": "numerical"},
    6: {"answer": "30", "type": "numerical"},
    7: {"answer": "Financial crisis and social inequality", "type": "short"},
    8: {"answer": "Deoxyribonucleic acid", "type": "short"},
    9: {"answer": "It helps plants produce oxygen and glucose", "type": "short"},
    }


    print("Extracted answers:", extracted_answers)

    graded_results = grade_exam(extracted_answers, model_answers)

    return graded_results

if __name__ == "__main__":
    image_filename = "exam.jpg"
    results = get_grades(image_filename)
    print(results)
