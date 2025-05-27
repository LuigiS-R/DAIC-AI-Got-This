import re
from openai import OpenAI

client = OpenAI(
    api_key="up_0xiZGIC9T6of93SeqWgJjTpirVr2n",
    base_url="https://api.upstage.ai/v1"
)

def solar_score(student_ans, correct_ans):
    prompt = (
        f"You are an exam grading AI.\n"
        f"Sometimes the student's answer may contain spacing or formatting errors due to OCR or parsing mistakes.\n"
        f"Your job is to evaluate the actual meaning. If the student's answer is actually correct but formatted wrong (like '1 2' instead of '12'), treat it as correct.\n"
        f"Given the student's answer and the correct answer, return how accurate the student's answer is.\n"
        f"Only return a number from 0 to 100 (no % sign).\n\n"
        f"Correct Answer: {correct_ans}\n"
        f"Student Answer: {student_ans}\n\n"
        f"Score (0-100):"
    )

    response = client.chat.completions.create(
        model="solar-pro",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )

    content = response.choices[0].message.content.strip()
    match = re.search(r"(\d{1,3})(?!\d)", content)
    if match:
        score = int(match.group(1))
        return max(0, min(score, 100)) / 100.0
    else:
        return 0.0

def grade_question(student_ans, correct_ans, qtype="short"):
    if student_ans is None or student_ans == "" or correct_ans is None or correct_ans == "":
        return 0.0, "No answer provided"

    if qtype == "short":
        score = solar_score(student_ans, correct_ans)
        return score, f"{int(score * 100)}% similarity (via Solar AI)"
    
    elif qtype == "mcq":
        correct = student_ans.strip().upper() == correct_ans.strip().upper()
        return 1.0 if correct else 0.0, "Multiple choice match"

    elif qtype == "truefalse":
        correct = student_ans.strip().lower() == correct_ans.strip().lower()
        return 1.0 if correct else 0.0, "True/False match"

    elif qtype == "numerical":
        try:
            correct = abs(float(student_ans) - float(correct_ans)) <= 0.01
            return 1.0 if correct else 0.0, "Numerical match"
        except:
            return 0.0, "Invalid number format"

    else:
        return 0.0, "Unsupported question type"

def grade_exam(student_answers, model_answers):
    results = {}
    for answer in student_answers:
        try:
            qnum = int(answer["question_number"])
        except ValueError:
            continue

        student_ans = answer["answer"]

        if qnum not in model_answers:
            results[qnum] = {"score": 0.0, "reason": "No model answer"}
            continue

        correct_ans = model_answers[qnum]["answer"]
        qtype = model_answers[qnum].get("type", "short")

        score, reason = grade_question(student_ans, correct_ans, qtype)
        results[qnum] = {"score": round(score, 2), "reason": reason}
    return results
