import json
from openai import OpenAI

client = OpenAI(
    api_key="up_0xiZGIC9T6of93SeqWgJjTpirVr2n",
    base_url="https://api.upstage.ai/v1"
)

def extract_answers_from_context_with_solar(context_text):
    prompt = (
        "You are an expert exam parser.\n"
        "Given the following exam context text (parsed from OCR, so it may be noisy or messy), extract all exam questions and the student's actual answers.\n\n"
        "Important rules:\n"
        "- For multiple choice questions (MCQs), first try to extract the student's letter answer (A, B, C, or D) if present (e.g., 'Answer: B', 'B.', or 'B' after the question).\n"
        "- If no letter answer is explicitly given, but the student wrote a textual answer near the question (e.g., 'Mars'), compare it with the text of each choice (e.g., A. Earth, B. Mars, etc.) and pick the letter whose choice text is most similar to the student's answer.\n"
        "- Use approximate text matching to handle typos or spacing errors.\n"
        "- If no suitable match is found, assign the answer as null but try to do it rarely.\n"
        "- For non-MCQ questions, extract the full textual answer exactly as the student wrote it (including typos).\n"
        "- Do NOT take the official multiple choice options as the student's answer unless the student explicitly wrote them as the answer.\n\n"
        "Return the result as a JSON array of objects with these fields:\n"
        "- question_number (integer)\n"
        "- question (string)\n"
        "- answer (string or null)  # For MCQ answers, return letter A-D; for others, return full text or null.\n\n"
        "Example output:\n"
        '[{"question_number":1, "question":"What is 2+2?", "answer":"A"}, ...]\n\n'
        f"Context:\n{context_text}\n\nExtracted JSON:"
    )

    response = client.chat.completions.create(
        model="solar-pro",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )

    content = response.choices[0].message.content.strip()

    if content.startswith("```json"):
        content = content[len("```json"):].strip()
    if content.endswith("```"):
        content = content[:-3].strip()

    try:
        extracted = json.loads(content)
        return extracted
    except json.JSONDecodeError:
        return []
