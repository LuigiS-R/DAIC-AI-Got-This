import os
import requests

def parse_single_pdf(pdf_path, upload_number, api_key=None):
    """Parses a single PDF using the Upstage document parser API."""
    if not api_key:
        api_key = "up_0xiZGIC9T6of93SeqWgJjTpirVr2n"

    if not api_key:
        raise EnvironmentError("Missing UPSTAGE_API_KEY environment variable.")

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    url = "https://api.upstage.ai/v1/document-digitization"
    headers = {"Authorization": f"Bearer {api_key}"}

    with open(pdf_path, "rb") as file:
        files = {"document": file}
        data = {
            "ocr": "force",  # Ensure OCR even on scanned PDFs
            "base64_encoding": "['table']",
            "model": "document-parse"
        }

        response = requests.post(url, headers=headers, files=files, data=data)
        response.raise_for_status()

    html_content = response.json().get("content", {}).get("html", "")
    return {
        "upload_number": upload_number,
        "context": html_content
    }

def parse_multiple_pdfs(pdf_paths, api_key=None):
    if not api_key:
        api_key = "up_0xiZGIC9T6of93SeqWgJjTpirVr2n"

    """Parses multiple PDFs and returns a list of parsed results."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Goes from functions/ to root
    parsed_results = []
    for idx, path in enumerate(pdf_paths, start=1):
        abs_path = os.path.join(base_dir, path)
        result = parse_single_pdf(abs_path, upload_number=idx, api_key=api_key)
        parsed_results.append(result)
    return parsed_results
