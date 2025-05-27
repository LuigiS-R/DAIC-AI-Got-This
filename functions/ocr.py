import requests
import os
import json

API_KEY = "up_0xiZGIC9T6of93SeqWgJjTpirVr2n"
OCR_URL = "https://api.upstage.ai/v1/document-digitization"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def ocr_image(file_like):
    """
    file_like: an open file or file-like object (binary mode).
    Sends file to OCR API and returns the JSON response.
    """
    files = {
        "document": (getattr(file_like, 'name', 'file'), file_like)
    }
    data = {"model": "ocr"}
    response = requests.post(OCR_URL, headers=HEADERS, files=files, data=data)
    response.raise_for_status()
    return response.json()

def process_exam_images(image_dir, output_path):
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith((".png", ".jpg", ".jpeg", ".pdf"))]
    if not image_files:
        print("❌ No image files found in the directory.")
        return

    start_id = int(input("Enter starting student ID: "))
    results = []

    for i, file in enumerate(sorted(image_files)):
        file_path = os.path.join(image_dir, file)
        print(f"🔍 Processing {file}...")

        try:
            ocr_result = ocr_image(file_path)
            text_content = ocr_result.get("text", "").strip()

            results.append({
                "student_id": start_id + i,
                "context": text_content
            })

        except Exception as e:
            print(f"❌ Error processing {file}: {e}")
