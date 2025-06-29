# DAIC-Template
> **PNU x Upstage: DOCUMENT AI CHALLENGE 리포지토리 템플릿입니다. 아래 마크다운을 프로젝트 리포지토리 형식에 맞춰서 리드미를 작성해주시면 됩니다.**

* `>`로 작성된 부분은 없애고 작성해주시면 됩니다.
* 해당 리포지토리를 fork해서 그대로 사용해주시면 됩니다. fork시 리포지토리 이름은 `DAIC-[TEAM_NAME]`으로 해주세요.
* 제출 마감일 이전까지 GitHub 리포지토리 main 브랜치에 커밋이 반영되어 있어야 유효 제출로 간주됩니다.
* README.md는 심사 기준과 연결된 내용을 의식하여 작성하는 것이 중요합니다 (예: API 활용, 문제 해결 효과 등).

<br>

```md
# [프로젝트 이름]
Grade Genie

## 📌 개요
Document Parse과 AI 기술을 활용하여 강의 자료를 기반으로 학생이 작셩한 학교 시험 답안을 자동 평가하고 시험지를 자동 생성할 수 있는 서비스입니다.

## 🎯 문제 정의 및 기대 효과
> '어떤 문제를 해결하고자 했는가?', '해당 문제의 중요성과 필요성은 무엇인가?', '이 솔루션이 사용자 혹은 조직에 어떤 가치를 줄 수 있는가?' 등
> 해당하는 내용을 작성해주세요.
어떤 과목의 분반에 학생 수가 많고 교수님 일정이 바쁠 경우, 채점과 결과 제공이 지연되는 일이 자주 발생합니다.
이로 인해 다음 시험이 다가오면 학생들은 이전 시험의 결과를 모 채 준비해야 하는 상황이 생기며 효과적인 학습 방향을 잡기 어려워집니다.
본 서비스는 교수님의 채점 부담을 줄이는 동시에, 학생들에게는 더 빠르고 정확한 피드백을 제공하여 학습 효과를 극대화할 수 있도록 설계되었습니다.
또한 강의 자료를 기반으로 자동 요약 및 시험 문항을 생성할 수 있어, 교육자 입장에서는 평가 자료 준비에 드는 시간을 절약할 수 있으며, 학교 차원에서도 평가의 공정성과 효율성을 향상시킬 수 있습니다.

## ✅ Upstage API 활용
> 적용한 기술이나 Upstage API를 어떻게 적용했는지를 작성해주시면 됩니다.
Upstage Document Parser API는 학생 시험지, 강의 자료 등의 문서를 구조화된 데이터로 변환하는 데 사용되며, 이 데이터는 채점 모듈과 시험 생성 모듈 모두의 입력으로 활용됩니다.

## 🚀 주요 기능
> 프로젝트의 주요 기능을 구체적으로 설명해주세요. Application 내 구현된 부분을 이미지로 함께 첨부하셔도 좋습니다.
> 창의적인 접근 방식이나 기존 방법과의 차별점을 서술해주시면 좋습니다.

- ✨ 기능 1: 시험 답안 자동 채점 (Grader API)
  학생이 제출한 시험 답안과 정답을 비교하여 의미 유사도(Semantic Similarity), 자연어 추론(NLI), 핵심 키워드 일치율 등을 기반으로 자동으로 채점을 수행합니다. 채점 결과는 정답 여부와 함께 점수, 피드백(예: "부분 정답", "핵심 키워드 누락", "의미 충돌") 형태로 출력됩니다.
  - 장점: 교수님의 수작업 채점 부담을 줄이고, 학생에게 더 빠르고 정량적인 피드백 제공 가능.

- ✨ 기능 2: 강의 자료 요약 및 시험 문제 생성 (Summarizer API)
  PPT 또는 HTML로 변환된 강의 자료를 입력하면 핵심 내용을 자동으로 추출하 요약합니다. 사용자는 간단 / 보통 / 자세히 중 원하는 요약 수준을 선택할 수 있으며, 이어서 시험 문제 자동 생성 기능과도 연계될 수 있습니다.
  - 장점: 수업 내용을 빠르게 복습하거나, 시험 문제를 구성할 핵심 내용을 파악하는 데 유용함.

- ✨ 기능 3: 학생 및 시험 정보 저장 데이터베이스
  교수님은 로그인 후 본인의 시험 문제, 정답, 학생 목록, 채점 결과 등을 웹 기반 시스템에 저장하고 관리할 수 있습니다. 학생별 이름, 응시한 문제에 대한 정답률, 채점 결과 등을 테이블 구조로 관리하며, 향후 통계 분석이나 자동 리포트 기능으로 확장도 가능합니다.
  - 장점: 교수는 학생 성적 데이터를 체계적으로 저장하고 관리할 수 있으며, 장기적으로 학생별 학습 분석, 성적 분포 시각화 등의 기능으로 확장 가능.

## 🖼️ 데모
> 스크린샷이나 데모 영상(GIF 또는 구글 드라이브 링크 등)을 포함해주세요.
- Description of Scenario: This system is designed to be used in the education field, particulary at university.
1) It can be used to grade exams such as midterms or finals, the person in charge of grading the exam papers must upload the student's exam papers altogether with the answer key of the exam. Then all of these files are then uploaded to the website's backend server, and later they are send as input to our python grading module. The grading module will grade the each exam paper using certain logic combined with Upstage Solar LLM, and finally it returns the final score for each exam paper. The backend will then retrieve the output of the grading module, store the scores of each student in a database and finally it will display all this info in the website.

2) It can be used to generate exams, the person in charge of creating the exam has the option to submit the lecture materials to the website, then this materials (.pdf, .jpeg, .word) are then uploaded to the backend server where they will later be sent to Upstage Document Parse API so they can be summarized so they can be processed and converted into different questions that are going to be used to create the exam paper. Summarization and question generation process is done inside a exam_generator module developed in Python. After getting the questions, the person in charge can modify the given questions, or even add more if he wishes, to finally create the PDF file of the exam paper and allowing the user of the system to download it.


## 🔬 기술 구현 요약
> 사용한 AI 모델이나 파이프라인, 적용 기술을 작성해주세요.

- Exam Generation Pipeline
Document Parsing - The system uses Upstage Document Parsing tool to perform extraction of structured HTML content from the uploaded PDF lecture slides
HTML Preprocessing - HTML Content is additionally cleaned up using BeautifullSoup and then split into logical slide-like sections for further processing

Summarization – Each subsequent section is summarized using prompt-engineered calls to the Solar AI (solar-pro model). This summarization is batch-processed and executed asynchronously and in parallel using *ThreadPoolExecutor* and *asyncio*, reducing delays and enabling efficient document processing.

Question Generation with Dynamic Prompting - Based on the slide summary JSON, questions are dynamically generated using prompt-engineered calls to the Solar AI (solar-pro model). The result is a clean, type-consistent JSON output categorized into multiple-choice, true/false, short answer, and essay formats each paired with answers.

- Exam Grading Pipeline
Answer Key Extraction - The system uses Upstage Document Parsing tool to perform extraction of the answer keys provided by the professor. Answers are automatically categorized into 4 sections (MCQ, T/F, Numerical an Short Answer)

Student Answer Extracton - The system uses Upstage Document OCR in order to scan the image versions of the answers and convert into machine-readable JSON

Extraction of answers - Since the output may be unstructured or noisy, prompt engineering with solar-pro language model is used. Together, OCR and prompt-based structuring form a robust pipeline for convering messy student answers sheets into clean data.

AI-Powered Grading Logic -  Grading is automatically handled based on the type of answer:

MCQ & True/False: Evaluated through case-insensitive direct comparison.

Numerical: Supports value matching with tolerance. For example, if the correct answer is 12 but the OCR/extraction system reads it as 1 2, full credit is still awarded.

Short Answer: Graded using semantic similarity scoring via prompt-based evaluation with Solar AI. This returns a confidence score ranging from 0.0 to 1.0. The scoring leverages large language models (LLMs) that apply contextual understanding and natural language inference to assess the quality of the response.

## 🧰 기술 스택 및 시스템 아키텍처
> 사용한 언어 및 프레임워크를 작성하고 시스템 아키텍처 이미지를 첨부해주세요.

Frontend: HTML, CSS (pure/static)
Backend: Node.js (Express)
Database: SQLite3 (file-based local DB)
API Protocol: RESTful (handling GET and POST requests)
External Services: Upstage APIs (Document OCR & Parsing), OpenAI API (for Solar AI)
AI Models: Solar AI (accessed via Upstage's solar-pro model using Python)
Storage: Local file system (for PDFs, JSONs, cache)
AI Logic: Implemented in Python (FastAPI), integrated into Node.js backend
Concurrency: Asynchronous + parallel processing using asyncio and ThreadPoolExecutor
Prompt Engineering: Used extensively for summarization, question generation, answer parsing, and grading

[User (Browser)]
      ↓
 [HTML/CSS Frontend]
      ↓
  [Node.js Backend]
      ↓            ↘
[SQLite3 DB]   [Python AI Module]
      ↓          ↙          ↘        ↘
[Local File Storage]   [OpenAI API]   [Upstage API]
                             ↓
                        [Solar AI]

## 🔧 설치 및 사용 방법
> 리포지토리 클론 이후 application을 실행할 수 있는 명령어를 작성해주세요.
> 실행할 수 있는 환경이 제한되어 있는 경우, 이곳에 배포 환경을 알려주세요.
> 실제로 배포하고 있다면, 배포 중인 사이트를 알려주셔도 됩니다.
> 아래는 예시입니다.

\```bash
git clone https://github.com/LuigiS-R/DAIC-AI-Got-This.git
cd DAIC-AI-Got-This
pip install -r requirements.txt
npm install
npm start
\```

## 📁 프로젝트 구조
> 프로젝트 루트 디렉토리에서 주요 파일 및 폴더의 역할 및 목적을 작성해주세요.
> 필요없다고 생각되는 부분은 생략하셔도 됩니다.
> 아래는 예시입니다.

\```bash
DAIC-AI-GOT-THIS/
├── app.js                    # Main Node.js server for routing
├── database/                 # Node.js service for DB operations
│   └── server.js             # Database service entry point
├── db/
│   └── database.js           # SQLite database logic
├── exam-generator-api/       # FastAPI app for summarization & question generation
│   ├── generator.py          # Core logic for generation of exam
│   ├── main.py               # FastAPI entry point
│   └── render.yaml           # Deployment config for Render
├── exam-grader-api/          # FastAPI app for grading student answers
│   ├── exam_grader.py        # Grading logic
│   ├── main.py               # FastAPI entry point
│   └── render.yaml           # Deployment config for Render
├── exam_grader.py            # (Optional) Shared grading script or duplicate
├── myDatabase.db             # SQLite database file
├── package.json              # Node.js dependencies
├── public/                   # Static frontend files (HTML/CSS/JS)
│   ├── index.html            # Main UI
│   └── style.css, app.js     # Styling and interactivity
├── README.md                 # Project documentation
├── server.js                 # Main Express server for serving frontend/API
└── requirements.txt          # Python dependencies

\```

## 🧑‍🤝‍🧑 팀원 소개
> 각 팀원 소개 및 역할을 작성해주세요.
> 아래는 예시이고 자유롭게 작성해주시면 됩니다.

| 이름  | 역할          | GitHub                                       |
| --- | ----------- | -------------------------------------------- |
| 루이스  | 팀장 / 백엔드 개발  | [@developer1](https://github.com/LuigiS-R)     |
| 아딜렛  | AI 모델 개발       | [@developer2](https://github.com/equkid)     |
| 안드레아 | AI 모델 개발      | [@developer3](https://github.com/andreamna)     |
| 자르갈  | 프론트엔드 개발     | [@designer1](https://github.com/Tuvshinjargal03)       |

## 💡 참고 자료 및 아이디어 출처 (Optional)
> 프로젝트를 개발하면서 참고했던 논문 및 기타 문헌이 있으시다면 첨부해주세요.
> 아래는 예시입니다.

* [Upstage Document Parse](https://www.upstage.ai/products/document-parse)
* [Upstage Building end-to-end RAG system using Solar LLM and MongoDB Atlas](https://www.upstage.ai/blog/en/building-rag-system-using-solar-llm-and-mongodb-atlas)

```
