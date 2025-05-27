from bs4 import BeautifulSoup
from openai import OpenAI
import re

# Initialize Solar AI client
client = OpenAI(
    api_key="up_0xiZGIC9T6of93SeqWgJjTpirVr2n",
    base_url="https://api.upstage.ai/v1"
)

def extract_text_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)

def preprocess_slides(html_input):
    slides = html_input.split("</footer>")
    slides = [slide.strip() + "</footer>" for slide in slides if slide.strip()]
    return slides

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F\uAC00-\uD7AF\u3130-\u318F\u1100-\u11FF]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()

def summarize_with_solar(text, detail_level="medium"):
    level_instruction = {
        "short": "Summarize briefly in 200 word.",
        "medium": "Summarize the content clearly and concisely in 300-400 words.",
        "detailed": "Summarize in detail with key points covered in 500+ words."
    }
    instruction = level_instruction.get(detail_level.lower(), level_instruction["medium"])

    prompt = f"{instruction}\n\nContent:\n\"\"\"\n{text}\n\"\"\"\n\nSummary:"

    try:
        response = client.chat.completions.create(
            model="solar-pro",
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error summarizing: {str(e)}]"

def summarize_html_slides(html_data: str, detail_level="medium", upload_number=1):
    """
    Summarizes HTML slide content using Solar AI.

    Parameters:
        html_data (str): Raw HTML content.
        detail_level (str): One of 'short', 'medium', or 'detailed'.
        upload_number (int): ID tag for the summary.

    Returns:
        tuple: (json_output_dict, plain_text_summary)
    """
    slides = preprocess_slides(html_data)
    summaries = []

    for chunk in slides:
        text = clean_text(extract_text_from_html(chunk))
        if len(text.strip()) > 20:
            summary = summarize_with_solar(text, detail_level)
            summaries.append(summary)

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
