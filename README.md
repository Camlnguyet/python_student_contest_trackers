# python_student_contest_trackers
# Student Contest Tracker

A web application to manage and analyze competitive programming students' contest results, built with Python.

## Live Demo
[👉 Click here to view the app](https://tracker-contest-duo.streamlit.app)

## 📌 Features
- Add and manage students, contests, and scores
- Automatic ranking and performance statistics (average, highest, lowest score)
- Interactive line chart tracking student progress over time
- Bar chart comparing average scores across students
- Export full report to Excel with one click

## 🛠️ Tech Stack
| Layer | Technology |
|---|---|
| Backend API | FastAPI + Uvicorn |
| Database | SQLite |
| Data Processing | Pandas |
| Visualization | Plotly |
| Frontend UI | Streamlit |

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/student-contest-tracker.git
cd student-contest-tracker
```

**2. Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the API**
```bash
uvicorn main:app --reload
```

**5. Run the Streamlit app** (new terminal)
```bash
streamlit run app.py
```

**6. Open in browser**
- Streamlit UI: http://localhost:8501
- API docs: http://localhost:8000/docs

## 📁 Project Structure
student_tracker/
├── main.py          # FastAPI endpoints
├── database.py      # SQLite setup & connection
├── models.py        # Pydantic data models
├── analytics.py     # Pandas & Plotly logic
├── app.py           # Streamlit UI
└── requirements.txt

## 👨‍💻 Author
Built as a portfolio project for MGM Technology Partners internship application.
