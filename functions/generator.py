import json
import re
from openai import OpenAI

client = OpenAI(
    api_key="up_0xiZGIC9T6of93SeqWgJjTpirVr2n",  # Replace with your actual key
    base_url="https://api.upstage.ai/v1"
)

def clean_json_response(text):
    # Remove triple backticks and optional 'json' label
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"```$", "", text)
    return text.strip()

def generate_section(context, count, section_type, start_q_number):
    base_prompt = f'''
You are an exam question generator. Based on the context below, generate {count} {section_type} exam questions.

Context:
\"\"\"{context}\"\"\"

Return the result as a valid JSON array where each item has these fields:
- question_number (starting from {start_q_number})
- context (the question text)
- answer (the correct answer)
- type (must be "{section_type}")

For Multiple Choice questions, also include a "choices" field with keys "A", "B", "C", "D".

Example format for Multiple Choice:
[
  {{
    "question_number": {start_q_number},
    "context": "Your question text here",
    "choices": {{
      "A": "Option 1",
      "B": "Option 2",
      "C": "Option 3",
      "D": "Option 4"
    }},
    "answer": "A",
    "type": "Multiple Choice"
  }}
]

Example format for True/False, Short Answer, Essay (no choices field):
[
  {{
    "question_number": {start_q_number},
    "context": "Your question text here",
    "answer": "Correct answer here",
    "type": "{section_type}"
  }}
]

Only return the JSON array. No explanations or additional text.
'''

    response = client.chat.completions.create(
        model="solar-pro",
        messages=[{"role": "user", "content": base_prompt}],
        stream=False,
    )

    raw_output = response.choices[0].message.content.strip()
    clean_output = clean_json_response(raw_output)

    try:
        questions = json.loads(clean_output)
        return questions
    except Exception as e:
        raise ValueError(f"Invalid JSON output: {e}\n\nReturned content:\n{raw_output}")

def interactive_question_generation(summaries_json):
    output_data = {"exam": []}

    for item in summaries_json.get("summaries", []):
        upload_num = item["upload_number"]
        context = item["context"]

        print(f"\n--- Upload #{upload_num} ---")
        print(f"Summary:\n{context[:300]}...\n")

        try:
            mcq = int(input("How many MCQs? "))
            tf = int(input("How many True/False? "))
            sa = int(input("How many Short Answer? "))
            es = int(input("How many Essay? "))
        except ValueError:
            print("Invalid input, skipping this upload.")
            continue

        all_questions = []
        current_q_num = 1

        try:
            if mcq > 0:
                questions = generate_section(context, mcq, "Multiple Choice", current_q_num)
                all_questions.extend(questions)
                current_q_num += mcq

            if tf > 0:
                questions = generate_section(context, tf, "True/False", current_q_num)
                all_questions.extend(questions)
                current_q_num += tf

            if sa > 0:
                questions = generate_section(context, sa, "Short Answer", current_q_num)
                all_questions.extend(questions)
                current_q_num += sa

            if es > 0:
                questions = generate_section(context, es, "Essay", current_q_num)
                all_questions.extend(questions)
                current_q_num += es

        except Exception as e:
            all_questions.append({"error": str(e)})

        output_data["exam"].append({
            "upload_number": upload_num,
            "questions": all_questions
        })

    return output_data


if __name__ == "__main__":
    with open("summaries.json", "r", encoding="utf-8") as f:
        summaries = json.load(f)

    question_data = interactive_question_generation(summaries)

    print("\nGenerated Questions JSON:\n")
    print(json.dumps(question_data, indent=2, ensure_ascii=False))
