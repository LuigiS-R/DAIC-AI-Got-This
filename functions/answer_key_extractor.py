import os
import requests
import json
import re
from bs4 import BeautifulSoup

def detect_type(ans: str) -> str:
    ans_clean = ans.strip().lower()
    if re.fullmatch(r'[a-fA-F]', ans.strip()):
        return "mcq"
    if ans_clean in ["true", "false"]:
        return "tf"
    if re.fullmatch(r'[\d\s\.,%$+-]+', ans_clean):
        return "numerical"
    return "short"

def extract_answers_from_pdf(filename: str) -> list:
    """
    Extract answers from PDF using Upstage API.
    API key is read from environment variable UPSTAGE_API_KEY.

    Raises:
        EnvironmentError if API key is missing.
    """
    api_key = "up_0xiZGIC9T6of93SeqWgJjTpirVr2n"
    if not api_key:
        raise EnvironmentError("Missing UPSTAGE_API_KEY environment variable.")

    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} not found.")

    url = "https://api.upstage.ai/v1/document-digitization"
    headers = {"Authorization": f"Bearer {api_key}"}
    with open(filename, "rb") as file:
        files = {"document": file}
        data = {
            "ocr": "force",
            "base64_encoding": "['table']",
            "model": "document-parse"
        }
        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()
        result = response.json()

    html_content = result.get("content", {}).get("html", "")
    soup = BeautifulSoup(html_content, "html.parser")

    answers = []
    for row in soup.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) >= 2:
            answer_text = cols[1].text.strip()
            answer_type = detect_type(answer_text)
            answers.append({
                "question": len(answers) + 1,
                "answer": answer_text,
                "type": answer_type
            })

    return answers
