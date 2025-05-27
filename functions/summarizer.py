import re
from bs4 import BeautifulSoup
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor

# Initialize Solar AI client
client = OpenAI(
    api_key="up_0xiZGIC9T6of93SeqWgJjTpirVr2n",
    base_url="https://api.upstage.ai/v1"
)

def extract_text_from_html(html):
    """Extracts text from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def preprocess_slides(html_input):
    """Preprocess HTML into individual slides."""
    slides = html_input.split("</footer>")
    slides = [slide.strip() + "</footer>" for slide in slides if slide.strip()]
    return slides

def clean_text(text):
    """Cleans the extracted text to remove unnecessary characters."""
    text = re.sub(r'[^\x00-\x7F\uAC00-\uD7AF\u3130-\u318F\u1100-\u11FF]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def summarize_with_solar_batch(texts, detail_level="medium"):
    """Summarize multiple slides in a batch using Solar AI."""
    level_instruction = {
        "short": "Summarize briefly in 100 word.",
        "medium": "Summarize the content clearly and concisely in 100-250 words.",
        "detailed": "Summarize in detail with key points covered in 250-400 words."
    }
    instruction = level_instruction.get(detail_level.lower(), level_instruction["medium"])

    prompt = f"{instruction}\n\nContent:\n\"\"\"\n"
    prompt += "\n\n".join(texts)
    prompt += "\n\"\"\"\n\nSummary:"

    try:
        response = client.chat.completions.create(
            model="solar-pro",
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error summarizing: {str(e)}]"

def summarize_html_slides_batch(html_data: str, detail_level="medium", upload_number=1, batch_size=5):
    """Summarize HTML slide content using Solar AI in batches."""
    slides = preprocess_slides(html_data)
    summaries = []
    batch = []

    for idx, chunk in enumerate(slides, start=1):
        text = clean_text(extract_text_from_html(chunk))
        if len(text.strip()) > 20:
            print(f"🔹 Adding slide chunk {idx} to batch...")
            batch.append(text)
        if len(batch) >= batch_size or idx == len(slides):
            print(f"🔹 Summarizing {len(batch)} chunks at once...")
            batch_summary = summarize_with_solar_batch(batch, detail_level)
            summaries.append(batch_summary)
            batch.clear()

    combined_summary = " ".join(summaries)

    json_output = {
        "summaries": [
            {
                "upload_number": upload_number,
                "context": combined_summary
            }
        ]
    }

    return json_output, combined_summary

def summarize_from_json_input(json_input: list, detail_level="medium"):
    all_summaries = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda entry: summarize_html_slides_batch(entry["context"], detail_level, entry["upload_number"]), json_input)

    # Collect all results
    for result in results:
        all_summaries.extend(result[0]["summaries"])

    print("\n🎉 All documents summarized in parallel.")
    return {"summaries": all_summaries}
