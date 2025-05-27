import re
import json

with open('raw_questions.json', 'r') as file:
    raw_data_from_file = json.load(file)

raw_data = {
    "raw_question_outputs": raw_data_from_file["raw_question_outputs"]
}
final_output = {
    "multiple_choice": [],
    "true_false": [],
    "short_answer": [],
    "essay": []
}

# Question number counters
counters = {
    "multiple_choice": 1,
    "true_false": 1,
    "short_answer": 1,
    "essay": 1
}

# Regex patterns
patterns = {
    "multiple_choice": re.compile(r"### Multiple Choice\n(.*?)(?=\n###|\Z)", re.DOTALL),
    "true_false": re.compile(r"### True/False\n(.*?)(?=\n###|\Z)", re.DOTALL),
    "short_answer": re.compile(r"### Short Answer\n(.*?)(?=\n###|\Z)", re.DOTALL),
    "essay": re.compile(r"### (Essay|Short Essay)\n(.*?)(?=\n###|\Z)", re.DOTALL),
    "qa": re.compile(r"\d+\.\s+(.*?)(?:\nA\..*?\n)*(?:Answer:|Sample answer:)\s*(.*?)(?=\n\d+\.|\n*$)", re.DOTALL)
}

for entry in raw_data["raw_question_outputs"]:
    raw = entry["raw_output"]

    for qtype, pattern in patterns.items():
        matches = pattern.findall(raw)
        for match in matches:
            # Some sections like Essay return a tuple
            block = match[1] if isinstance(match, tuple) else match
            qas = patterns["qa"].findall(block)
            for question, answer in qas:
                final_output[qtype].append({
                    "question_number": counters[qtype],
                    "question": question.strip(),
                    "answer": answer.strip()
                })
                counters[qtype] += 1

# Pretty print or save to file
print(json.dumps(final_output, indent=2))
