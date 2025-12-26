# AI Resume Analyzer & Job Matcher

A production-ready Flask web application that analyzes resumes and matches them with job descriptions using NLP-based skill extraction.

## 🚀 Features

- **Resume PDF Parsing**: Extract text from PDF resumes automatically
- **NLP-Based Skill Extraction**: Uses keyword matching with a comprehensive skill database
- **Job Description Analysis**: Extract required skills from job descriptions
- **Skill Matching**: Calculate match percentage and identify matched/missing skills
- **Responsive UI**: Modern, mobile-friendly interface with Bootstrap
- **Real-time Feedback**: Instant analysis with visual results
- **Error Handling**: Comprehensive error messages for better UX

## 📋 Requirements

- Python 3.8+
- pip (Python package manager)
- 50MB free disk space

## 🛠️ Tech Stack

- **Backend**: Python 3.8+ with Flask
- **PDF Parsing**: PyPDF2
- **NLP**: spaCy (prepared for future enhancements)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite (optional for future features)

## 📁 Project Structure

```
AI Resume Analyzer & Job Matcher/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/
│   └── index.html             # Main HTML template
│
├── static/
│   ├── style.css              # Styling
│   └── script.js              # Frontend JavaScript
│
├── utils/
│   ├── __init__.py            # Package initialization
│   ├── resume_parser.py       # PDF parsing module
│   ├── skill_extractor.py     # Skill extraction module
│   └── matcher.py             # Skill matching logic
│
└── uploads/                    # Temporary resume storage
```

## 🔧 Installation & Setup

### Step 1: Clone/Download the Project

```bash
cd "AI Resume Analyzer & Job Matcher"
```

### Step 2: Create Virtual Environment (Recommended)

**Windows (Command Prompt):**
```bash
python -m venv venv
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- Flask 3.0.0 - Web framework
- PyPDF2 4.0.1 - PDF parsing
- spaCy 3.7.2 - NLP library
- python-dotenv 1.0.0 - Environment variables
- Werkzeug 3.0.1 - WSGI utilities

### Step 4: Run the Application

```bash
python app.py
```

**Expected output:**
```
============================================================
AI Resume Analyzer & Job Matcher
============================================================
Starting Flask development server...
Navigate to: http://127.0.0.1:5000
============================================================
```

### Step 5: Open in Browser

Navigate to: **http://127.0.0.1:5000**

## 📖 How to Use

### Basic Workflow

1. **Upload Resume**: Click the upload button and select a PDF resume
2. **Enter Job Description**: Paste or type the job description in the text area
3. **Click Analyze**: Submit the form to start analysis
4. **View Results**: See matched skills, missing skills, and overall match score

### Sample Data

Click "Load sample job description" to populate a sample job posting for testing.

## 📊 How It Works

### 1. Resume Processing
- Extracts text from uploaded PDF files
- Cleans and normalizes the text
- Removes special characters and extra whitespace

### 2. Skill Extraction
- Uses a comprehensive database of 150+ technical skills
- Covers: programming languages, frameworks, databases, cloud platforms, tools
- Performs keyword matching with word boundaries
- Returns sorted, deduplicated skill lists

### 3. Skill Matching
- Compares resume skills with job requirements
- Calculates match percentage
- Identifies matched and missing skills
- Provides match level (Excellent, Good, Fair, Poor, Very Poor)

## 🎯 Supported Skills

The application recognizes skills across multiple categories:

### Programming Languages
Python, Java, JavaScript, TypeScript, C++, C#, PHP, Ruby, Go, Rust, Kotlin, Swift, R, MATLAB, Perl, Scala, and more

### Web Development
HTML, CSS, React, Vue, Angular, Flask, Django, FastAPI, Express, Node.js, ASP.NET, Laravel, Spring Boot, and more

### Databases
SQL, MySQL, PostgreSQL, MongoDB, Redis, SQLite, Oracle, Elasticsearch, Cassandra, DynamoDB, Firebase, and more

### Cloud & DevOps
AWS, Azure, GCP, Docker, Kubernetes, Jenkins, GitLab, GitHub, CI/CD, Terraform, Ansible, and more

### Data Science & ML
Machine Learning, Deep Learning, TensorFlow, PyTorch, Keras, scikit-learn, Pandas, NumPy, NLTK, spaCy, Computer Vision, and more

### Other Categories
Version Control (Git, SVN), Testing (Pytest, Jest, Selenium), APIs (REST, GraphQL), Agile (Scrum, Kanban), and more

## 🔍 Advanced Features

### Error Handling
- Validates file type (PDF only)
- Checks file size (max 16MB)
- Validates text inputs
- Provides user-friendly error messages

### Performance
- Fast PDF parsing
- Efficient skill matching algorithm
- Automatic temporary file cleanup
- Optimized for typical resume sizes

### Security
- File upload validation
- Secure filename handling
- No data persistence (privacy-first)
- XSS and CSRF protection ready

## 🎨 UI/UX Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Bootstrap 5**: Modern, professional styling
- **Font Awesome Icons**: Visual enhancements
- **Loading States**: Clear feedback during processing
- **Success/Error Messages**: Toast notifications for actions
- **Progress Bar**: Visual match percentage indicator
- **Color-coded Badges**: Green for matched, red for missing skills
- **Smooth Animations**: Professional transitions and effects

## 📝 API Endpoints

### POST /analyze
Analyze resume and job description

**Request:**
```
Content-Type: multipart/form-data
- resume: [PDF file]
- job_description: [text]
```

**Response:**
```json
{
  "success": true,
  "match_percentage": 75.5,
  "match_level": "Good Match",
  "matched_skills": ["python", "flask", "javascript"],
  "missing_skills": ["docker", "kubernetes"],
  "resume_skills_count": 12,
  "required_skills_count": 8,
  "matched_count": 6,
  "missing_count": 2
}
```

### GET /api/sample-data
Get sample job description for testing

**Response:**
```json
{
  "sample_job_description": "[Sample job posting text]"
}
```

## 🚨 Troubleshooting

### Issue: Port 5000 already in use
```bash
# Change port in app.py
# Change: app.run(..., port=5000)
# To:     app.run(..., port=5001)
```

### Issue: PDF parsing fails
- Ensure PDF is not corrupted
- Try converting PDF to text first
- Check file permissions

### Issue: Skills not recognized
- The app recognizes 150+ skills
- For custom skills, add them to `TECHNICAL_SKILLS` in `utils/skill_extractor.py`
- Ensure exact spelling (case-insensitive matching)

### Issue: Module not found errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 🔐 Security Notes

- Uploaded files are temporarily stored and automatically deleted
- No data is stored in a database by default
- All processing is done server-side
- File uploads are validated and sandboxed
- Input sanitization is applied

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production (using Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker
Create a Dockerfile:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:
```bash
docker build -t resume-analyzer .
docker run -p 5000:5000 resume-analyzer
```

## 📈 Future Enhancements

- [ ] SQLite database for job history
- [ ] User authentication system
- [ ] Resume export to PDF
- [ ] Advanced NLP with spaCy entity extraction
- [ ] Machine learning model for better matching
- [ ] Custom skill database per user
- [ ] Email resume upload
- [ ] API rate limiting
- [ ] Admin dashboard

## 📝 Code Quality

The application follows best practices:
- **Modular Architecture**: Separated concerns (parsing, extraction, matching)
- **Clear Documentation**: Docstrings and comments throughout
- **Error Handling**: Try-catch blocks with informative messages
- **Type Hints**: Function signatures with type annotations
- **PEP 8 Compliance**: Follows Python style guidelines
- **DRY Principle**: No code repetition
- **Security**: Input validation and sanitization

## 🤝 Contributing

To extend this application:

1. Add more skills to `TECHNICAL_SKILLS` in `skill_extractor.py`
2. Enhance matching algorithm in `matcher.py`
3. Add database integration for persistence
4. Implement user authentication
5. Add export functionality

## 📄 License

This project is open source and available for educational and commercial use.

## 👨‍💻 Author

Created as a production-ready full-stack application demonstrating:
- Python backend development
- Flask web framework
- NLP/text processing
- Frontend web technologies
- Software engineering best practices

## 💡 Tips for Best Results

1. **Resume Quality**: Use properly formatted PDF resumes
2. **Job Description**: Include detailed requirements and skills
3. **Exact Match**: Skills are matched with exact spelling
4. **Multiple Languages**: Include programming languages and frameworks
5. **Acronyms**: Include both full names and acronyms (e.g., "React" and "React.js")

## 🆘 Support

If you encounter issues:

1. Check the browser console for errors (F12)
2. Check Flask terminal output for server errors
3. Ensure all files are in correct directories
4. Verify Python version (3.8+)
5. Try reinstalling dependencies

## ✅ Tested Scenarios

- ✓ PDF resume parsing (various PDF types)
- ✓ Large resumes (50+ pages)
- ✓ Long job descriptions (5000+ words)
- ✓ Special characters and Unicode
- ✓ Mobile responsiveness
- ✓ Error handling and validation
- ✓ Browser compatibility (Chrome, Firefox, Safari, Edge)

---

**Version**: 1.0.0  
**Last Updated**: December 2024  
**Status**: Production Ready ✅
