import os
import requests
import re
from bs4 import BeautifulSoup
import json

def parse_exam_document(file_path):
    """
    Uploads a document file (e.g., PDF or DOCX) to Upstage Document Parser API
    and returns the parsed JSON response.
    API key is read from environment variable UPSTAGE_API_KEY.
    """
    api_key = "up_0xiZGIC9T6of93SeqWgJjTpirVr2n"
    if not api_key:
        raise EnvironmentError("Missing UPSTAGE_API_KEY environment variable.")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    DOC_URL = "https://api.upstage.ai/v1/document-digitization"
    headers = {"Authorization": f"Bearer {api_key}"}

    with open(file_path, "rb") as f:
        files = {"document": f}
        data = {
            "ocr": "false",
            "base64_encoding": "['table']",
            "model": "document-parse"
        }

        response = requests.post(DOC_URL, headers=headers, files=files, data=data)
        response.raise_for_status()
        return response.json()

def flatten_questions(parsed_json):
    html = parsed_json.get("content", {}).get("html", "")
    soup = BeautifulSoup(html, "html.parser")
    raw_text = soup.get_text(separator="\n").strip()

    lines = raw_text.split("\n")
    flat_questions = []
    current_question = ""
    current_choices = []
    question_number = 1
    in_question = False

    for line in lines:
        line = line.strip()

        if not line or re.match(r"^Answer[:：]|^\(True / False\)", line, re.IGNORECASE):
            continue

        if re.match(r"^[A-Da-d][\.\)]\s*", line):
            current_choices.append(line)
            continue

        if re.match(r"^\d+[\.\)]\s*", line):
            if current_question:
                question_obj = {
                    "number": question_number,
                    "question": current_question.strip()
                }
                if current_choices:
                    question_obj["choices"] = current_choices
                flat_questions.append(question_obj)
                question_number += 1
                current_choices = []
                current_question = ""

            current_question = re.sub(r"^\d+[\.\)]\s*", "", line)
            in_question = True

        elif in_question:
            if re.match(r"^Answer:|^\(True / False\)", line):
                continue

            current_question += " " + line
            current_question = current_question.strip()

            end_match = re.search(r"(.+?[?.:])(\s|$)", current_question)
            if end_match:
                question_text = end_match.group(1).strip()
                question_obj = {
                    "number": question_number,
                    "question": question_text
                }
                if current_choices:
                    question_obj["choices"] = current_choices
                flat_questions.append(question_obj)
                question_number += 1
                current_question = ""
                current_choices = []
                in_question = False

    if current_question:
        question_obj = {
            "number": question_number,
            "question": current_question.strip()
        }
        if current_choices:
            question_obj["choices"] = current_choices
        flat_questions.append(question_obj)

    return flat_questions